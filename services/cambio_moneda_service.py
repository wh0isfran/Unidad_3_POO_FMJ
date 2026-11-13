
import re
import requests

from config.settings import Settings


class CambioMonedaService:

    @staticmethod
    def consultar_tipo_cambio(origen="USD", destino="CLP"):
        origen = origen.strip().upper()
        destino = destino.strip().upper()

        patron = r"[A-Z]{3}"

        if not re.fullmatch(patron, origen):
            return None, "Moneda de origen inválida."

        if not re.fullmatch(patron, destino):
            return None, "Moneda de destino inválida."

        if origen == destino:
            return None, "Selecciona dos monedas diferentes."

        try:
            url = (
                f"{Settings.API_BASE_URL.rstrip('/')}"
                f"/{origen}/{destino}"
            )

            response = requests.get(
                url,
                headers={"Accept": "application/json"},
                timeout=Settings.REQUEST_TIMEOUT
            )

            response.raise_for_status()
            datos = response.json()

            if not isinstance(datos, dict):
                return None, "Respuesta JSON inválida."

            if not all(
                clave in datos
                for clave in ("date", "base", "quote", "rate")
            ):
                return None, "Faltan datos en la respuesta."

            resultado = {
                "fecha": datos["date"],
                "origen": datos["base"],
                "destino": datos["quote"],
                "valor": float(datos["rate"])
            }

            return resultado, "Consulta exitosa."

        except requests.Timeout:
            return None, "La API tardó demasiado en responder."

        except requests.RequestException as error:
            return None, f"Error de conexión con la API: {error}"

        except (ValueError, TypeError):
            return None, "La API devolvió datos inválidos."
