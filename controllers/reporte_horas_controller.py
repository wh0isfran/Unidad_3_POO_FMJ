from services.reporte_horas_services import ReporteHorasService


class ReporteHorasController:

    def __init__(self, view):
        self.view = view

    def consultar_reportes_externos(self):
        periodo = self.view.pedir_periodo()

        if not periodo:
            return

        try:
            reportes, mensaje = (
                ReporteHorasService.buscar_reportes_externos(periodo)
            )

            self.view.mostrar_mensaje(mensaje)

            if reportes:
                self.view.mostrar_listado_local(reportes)
            else:
                self.view.mostrar_mensaje(
                    "No se encontraron reportes."
                )

        except ValueError as e:
            self.view.mostrar_mensaje(str(e))

        except Exception as e:
            self.view.mostrar_error(
                f"Error inesperado al consultar la API: {e}"
    )

    def probar_conectividad(self):
        correcto, mensaje = (
            ReporteHorasService.probar_conectividad()
        )

        self.view.mostrar_mensaje(mensaje)

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()

            if opcion == 1:
                self.consultar_reportes_externos()

            elif opcion == 2:
                self.probar_conectividad()

            elif opcion == 0:
                break

            else:
                self.view.mostrar_error(
                    "Opción no válida. Intente nuevamente."
                )