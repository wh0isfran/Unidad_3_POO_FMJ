import re
from typing import List, Tuple

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    requests = None
    REQUESTS_AVAILABLE = False

from config.settings import Settings
from models.reporte_horas import ReporteHoras

class ReporteHorasService:
    #Código de respaldo
    REPORTE_CONTINGENCIA = [
        ReporteHoras(id_empleado=1, id_proyecto=101, horas_trabajadas=8.0, fecha="2026-11-01", periodo_mes="2026-11", fecha_generacion="2026-11-11"),
        ReporteHoras(id_empleado=2, id_proyecto=102, horas_trabajadas=7.5, fecha="2026-11-01", periodo_mes="2026-11", fecha_generacion="2026-11-11"),
        ReporteHoras(id_empleado=3, id_proyecto=103, horas_trabajadas=9.0, fecha="2026-11-02", periodo_mes="2026-11", fecha_generacion="2026-11-11")
    ]

    @classmethod
    def probar_conectividad(cls):
        if not REQUESTS_AVAILABLE:
            return False, "La librería requests no está instalada."

        try:
            response = requests.get(
                Settings.API_BASE_URL,
                params={"_limit": 1},
                headers={"Accept": "application/json"},
                timeout=Settings.REQUEST_TIMEOUT
            )

            response.raise_for_status()

            datos = response.json()

            if not isinstance(datos, list):
                return False, "La API respondió, pero el formato de datos no es el esperado."

            return True, "Conexión correcta con la API externa."

        except requests.exceptions.Timeout:
            return False, "Se agotó el tiempo de espera."

        except requests.exceptions.RequestException as e:
            return False, f"Error de conexión: {e}"

        except ValueError as e:
            return False, f"Respuesta JSON inválida: {e}"

    @staticmethod
    def sanitizar_periodo(periodo: str) -> str:
        from datetime import datetime

        if not isinstance(periodo, str) or not periodo.strip():
            raise ValueError("Debe ingresar un período válido.")

        limpio = periodo.strip()

        try:
            datetime.strptime(limpio, "%Y-%m")
        except ValueError:
            raise ValueError(
                "Período inválido. Utilice el formato YYYY-MM."
            )

        return limpio

    @classmethod
    def _manejar_contingencia(cls, periodo: str, mensaje_error: str):
        if not Settings.ENABLE_OFFLINE_FALLBACK:
            return [], f"API no disponible: {mensaje_error}"

        filtrados = [
            reporte
            for reporte in cls.REPORTE_CONTINGENCIA
            if reporte.periodo_mes == periodo
        ]

        if not filtrados:
            return [], (
                f"API no disponible: {mensaje_error}. "
                f"No existen datos locales para {periodo}."
            )

        return filtrados, (
            f"Modo contingencia activo: {mensaje_error}. "
            f"Se muestran datos locales de {periodo}."
        )

    @classmethod
    def buscar_reportes_externos(cls, periodo: str):
        from datetime import date

        periodo_seguro = cls.sanitizar_periodo(periodo)

        if not REQUESTS_AVAILABLE:
            return cls._manejar_contingencia(
                periodo_seguro,
                "La librería requests no está instalada."
            )

        try:
            response = requests.get(
                Settings.API_BASE_URL,
                params={"_limit": 10},
                headers={"Accept": "application/json"},
                timeout=Settings.REQUEST_TIMEOUT
            )

            response.raise_for_status()

            datos = response.json()

            if not isinstance(datos, list):
                raise ValueError("La respuesta de la API no es una lista.")

            reportes = []

            for item in datos:
                id_empleado = int(item["userId"])
                id_proyecto = int(item["id"])

                if id_empleado <= 0 or id_proyecto <= 0:
                    raise ValueError("Se recibió un identificador inválido.")

                reporte = ReporteHoras(
                    id_empleado=id_empleado,
                    id_proyecto=id_proyecto,
                    horas_trabajadas=float((id_proyecto % 8) + 1),
                    fecha=f"{periodo_seguro}-01",
                    periodo_mes=periodo_seguro,
                    fecha_generacion=date.today().isoformat(),
                    id_reporte=id_proyecto
                )

                reportes.append(reporte)

            return reportes, (
                "Consulta exitosa. Datos demostrativos obtenidos desde la API."
            )

        except requests.exceptions.Timeout:
            return cls._manejar_contingencia(
                periodo_seguro,
                "Tiempo de espera agotado."
            )

        except requests.exceptions.HTTPError as e:
            return cls._manejar_contingencia(
                periodo_seguro,
                f"Error HTTP: {e}"
            )

        except requests.exceptions.RequestException as e:
            return cls._manejar_contingencia(
                periodo_seguro,
                f"Error de conexión: {e}"
            )

        except (ValueError, KeyError, TypeError) as e:
            return cls._manejar_contingencia(
                periodo_seguro,
                f"Error al interpretar los datos: {e}"
            )
        