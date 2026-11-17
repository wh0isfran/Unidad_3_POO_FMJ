from typing import ClassVar

import requests

from config.settings import Settings
from models.clima import Clima


class ClimaService:

    CIUDADES: ClassVar[dict[str, tuple[str, float, float]]] = {
        "1": ("Santiago", -33.45, -70.65),
        "2": ("Valparaíso", -33.05, -71.62),
        "3": ("Concepción", -36.83, -73.05)
    }


    @staticmethod
    def consultar_clima(opcion: str):
        if opcion not in ClimaService.CIUDADES:
            return None, "Ciudad no válida."

        ciudad, latitud, longitud = (
            ClimaService.CIUDADES[opcion]
        )

        try:
            response = requests.get(
                Settings.API_CLIMA_URL,
                params={
                    "latitude": latitud,
                    "longitude": longitud,
                    "current": (
                        "temperature_2m,"
                        "relative_humidity_2m,"
                        "wind_speed_10m"
                    ),
                    "timezone": "auto"
                },
                timeout=Settings.REQUEST_TIMEOUT
            )

            response.raise_for_status()
            datos = response.json()
            actual = datos["current"]

            clima = Clima(
                ciudad=ciudad,
                temperatura=float(
                    actual["temperature_2m"]
                ),
                humedad=float(
                    actual["relative_humidity_2m"]
                ),
                viento=float(
                    actual["wind_speed_10m"]
                ),
                fecha_consulta=actual["time"]
            )

            return clima, "Clima obtenido correctamente."

        except requests.RequestException as error:
            return None, f"Error al consultar API: {error}"

        except (KeyError, TypeError, ValueError):
            return None, "Respuesta meteorológica inválida."
