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
    # Catálogo de respaldo local por si se corta internet en la empresa
    REPORTE_CONTINGENCIA = [
        ReporteHoras(id_empleado=1, id_proyecto=101, horas_trabajadas=8.0, fecha="2026-11-01", periodo_mes="2026-11", fecha_generacion="2026-11-11"),
        ReporteHoras(id_empleado=2, id_proyecto=102, horas_trabajadas=7.5, fecha="2026-11-01", periodo_mes="2026-11", fecha_generacion="2026-11-11"),
        ReporteHoras(id_empleado=3, id_proyecto=103, horas_trabajadas=9.0, fecha="2026-11-02", periodo_mes="2026-11", fecha_generacion="2026-11-11")
    ]

    @classmethod
    def probar_conectividad(cls) -> Tuple[bool, str]:
        """Verifica si la API externa está accesible."""
        if not REQUESTS_AVAILABLE:
            return (False, "Librería 'requests' no instalada. Ejecute 'pip install requests'.")

        try:
            resp = requests.get(
                Settings.API_BASE_URL,
                params={"limit": 1},
                timeout=Settings.REQUEST_TIMEOUT
            )
            if resp.status_code in (200, 404):
                return (True, f"Conexión exitosa con {Settings.API_BASE_URL} (Código HTTP: {resp.status_code})")
            return (False, f"El servidor respondió con código HTTP: {resp.status_code}")
        except requests.exceptions.Timeout:
            return (False, "Timeout al contactar el servicio.")
        except requests.exceptions.ConnectionError:
            return (False, "Sin conexión de red hacia el servidor.")
        except Exception as e:
            return (False, f"Error de red: {str(e)}")

    @staticmethod
    def sanitizar_periodo(periodo: str) -> str:
        """Valida que el periodo cumpla con el formato YYYY-MM y no contenga caracteres maliciosos."""
        if not periodo or not isinstance(periodo, str):
            raise ValueError("El periodo de búsqueda debe ser un texto válido.")
        
        limpio = periodo.strip()
        if not re.match(r"^\d{4}-\d{2}$", limpio):
            raise ValueError("El periodo contiene un formato no permitido (Use YYYY-MM).")

        return limpio

    @classmethod
    def _manejar_contingencia(cls, periodo: str, mensaje_error: str) -> Tuple[List[ReporteHoras], str]:
        """Retorna datos de respaldo locales cuando la API no está disponible o falla."""
        filtrados = [r for r in cls.REPORTE_CONTINGENCIA if r.periodo_mes == periodo]
        resultado = filtrados if filtrados else cls.REPORTE_CONTINGENCIA
        return resultado, f"Modo Contingencia Activo: {mensaje_error}"

    @classmethod
    def buscar_reportes_externos(cls, periodo: str) -> Tuple[List[ReporteHoras], str]:
        """Consulta la API externa de horas con el periodo solicitado."""
        periodo_seguro = cls.sanitizar_periodo(periodo)

        if not REQUESTS_AVAILABLE:
            return cls._manejar_contingencia(
                periodo_seguro,
                "Librería 'requests' no instalada en el entorno."
            )

        headers = {
            "Accept": "application/json",
            "User-Agent": "EmpresaControlHorasApp/1.0"
        }

        # Inyección segura de token si existe
        if hasattr(Settings, "API_KEY") and Settings.API_KEY:
            headers["Authorization"] = f"Bearer {Settings.API_KEY}"

        params = {
            "periodo": periodo_seguro,
            "limit": 10
        }

        try:
            url = getattr(Settings, "API_BASE_URL", "https://api.empresa-control-horas.com/v1/reportes")
            response = requests.get(url, headers=headers, params=params, timeout=getattr(Settings, "REQUEST_TIMEOUT", 5))

            if response.status_code == 200:
                data = response.json()
                reportes = []
                
                # Mapeo de la respuesta JSON externa al modelo de dominio ReporteHoras
                for item in data.get("resultados", []):
                    reporte = ReporteHoras(
                        id_empleado=item.get("id_empleado"),
                        id_proyecto=item.get("id_proyecto"),
                        horas_trabajadas=item.get("horas_trabajadas"),
                        fecha=item.get("fecha"),
                        periodo_mes=item.get("periodo_mes"),
                        fecha_generacion=item.get("fecha_generacion"),
                        id_reporte=item.get("id_reporte")
                    )
                    reportes.append(reporte)
                
                return reportes, "Consulta exitosa desde la API externa."
            else:
                return cls._manejar_contingencia(
                    periodo_seguro,
                    f"Error HTTP del servidor externo: {response.status_code}"
                )

        except Exception as e:
            return cls._manejar_contingencia(
                periodo_seguro,
                f"Fallo de conexión o timeout: {str(e)}"
            )