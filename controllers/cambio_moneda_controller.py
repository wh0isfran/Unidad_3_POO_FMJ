
from services.cambio_moneda_service import CambioMonedaService
from views.cambio_moneda_view import CambioMonedaView


class CambioMonedaController:

    def __init__(self):
        self.view = CambioMonedaView()

    def ejecutar(self) -> None:
        print("\n===== CONSULTA DE CAMBIO DE MONEDA =====")

        origen = self.view.solicitar_moneda(
            "Seleccione número de moneda de ORIGEN: "
        )

        destino = self.view.solicitar_moneda(
            "Seleccione número de moneda de DESTINO: "
        )

        resultado, mensaje = CambioMonedaService.consultar_tipo_cambio(
            origen, destino
        )

        if resultado is not None:
            self.view.mostrar_resultado(
                origen, destino, resultado, mensaje
            )
        else:
            self.view.mostrar_mensaje(mensaje)
