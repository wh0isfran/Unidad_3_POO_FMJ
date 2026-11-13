
from services.cambio_moneda_service import CambioMonedaService


class CambioMonedaController:

    @staticmethod
    def ejecutar():
        print("\n===== CONSULTA DE TIPO DE CAMBIO =====")

        origen = input("Moneda de origen (ej. USD): ")
        destino = input("Moneda de destino (ej. CLP): ")

        resultado, mensaje = CambioMonedaService.consultar_tipo_cambio(
            origen, destino
        )

        print(f"\n{mensaje}")

        if resultado is not None:
            print(f"Fecha: {resultado['fecha']}")
            print(f"Moneda origen: {resultado['origen']}")
            print(f"Moneda destino: {resultado['destino']}")
            print(
                f"1 {resultado['origen']} = "
                f"{resultado['valor']:.2f} "
                f"{resultado['destino']}"
            )
