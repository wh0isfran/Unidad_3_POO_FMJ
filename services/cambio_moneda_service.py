
import re

import requests

from config.settings import Settings


class CambioMonedaService:

    @staticmethod
    def consultar_tipo_cambio(origen: str, destino: str):
        origen = origen.strip().upper()
        destino = destino.strip().upper()

        if not re.fullmatch(r"[A-Z]{3}", origen):
            return None, "Moneda de origen inválida."

        if not re.fullmatch(r"[A-Z]{3}", destino):
            return None, "Moneda de destino inválida."

        if origen == destino:
            return 1.0, "Ambas monedas son iguales."

        try:
            url = (
                f"{Settings.API_MONEDA_URL.rstrip('/')}"
                f"/rate/{origen.lower()}/{destino.lower()}"
            )

            response = requests.get(
                url,
                timeout=Settings.REQUEST_TIMEOUT
            )

            response.raise_for_status()
            datos = response.json()

            tasa = float(datos["rate"])

            if tasa <= 0:
                raise ValueError("Tipo de cambio inválido.")

            return tasa, (
                f"Tipo de cambio obtenido correctamente. "
                f"Fecha: {datos['date']}"
            )

        except (requests.RequestException, ValueError, KeyError, TypeError) as error:
            return None, f"No se pudo consultar el tipo de cambio: {error}"
