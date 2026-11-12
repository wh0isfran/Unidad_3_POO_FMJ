from views.reporte_horas_view import ReporteHorasView
from models.reporte_horas import ReporteHoras
from services.reporte_horas_services import ReporteHorasService
from models.reporte_horas_dao import ReporteHorasDAO

class ReporteHorasController:
    def __init__(self):
        self.view = ReporteHorasView()
        self.service = ReporteHorasService()
        self.reporte_dao = ReporteHorasDAO()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.consultar_reportes_externos()
            elif opcion == 2:
                self.registrar_reporte_horas()
            elif opcion == 3:
                self.consultar_reportes_empleado()
            elif opcion == 4:
                self.listar_todos_reportes()
            elif opcion == 5:
                self.diagnosticar_conexion()
            elif opcion == 0:
                break
            else:
                self.view.mostrar_error("Opción no válida. Intente nuevamente.")

    def consultar_reportes_externos(self) -> None:
        periodo = self.view.pedir_periodo_busqueda()
        if not periodo:
            return
        
        try:
            reportes, estado = self.service.buscar_reportes_externos(periodo)
            self.view.mostrar_mensaje(estado)
            self.view.mostrar_reportes_externos(reportes)
        except ValueError as e:
            self.view.mostrar_error(str(e))
        except Exception as e:
            self.view.mostrar_error(f"Error inesperado: {str(e)}")

    def registrar_reporte_horas(self) -> None:
        datos_extra = self.view.pedir_datos_reporte()

        if not datos_extra:
            return

        try:
            nuevo_reporte = ReporteHoras(
                id_empleado=datos_extra["id_empleado"],
                id_proyecto=datos_extra["id_proyecto"],
                horas_trabajadas=datos_extra["horas_trabajadas"],
                fecha=datos_extra["fecha"],
                periodo_mes=datos_extra["periodo_mes"],
                fecha_generacion=datos_extra["fecha_generacion"]
            )

            id_generado = self.reporte_dao.insertar(nuevo_reporte)

            if id_generado:
                self.view.mostrar_mensaje(
                    f"Reporte #{id_generado} guardado correctamente."
                )
            else:
                self.view.mostrar_error(
                    "No se pudo guardar el reporte."
                )

        except ValueError as e:
            self.view.mostrar_error(str(e))

        except Exception as e:
            self.view.mostrar_error(
                f"Error al registrar el reporte: {e}"
            )

    def consultar_reportes_empleado(self) -> None:
        id_emp = self.view.pedir_id_empleado()

        if not id_emp:
            return

        reportes = self.reporte_dao.obtener_por_empleado(id_emp)
        self.view.mostrar_listado_local(reportes)

    def listar_todos_reportes(self) -> None:
        reportes = self.reporte_dao.listar_todas()
        self.view.mostrar_listado_local(reportes)

    def diagnosticar_conexion(self) -> None:
        self.view.mostrar_mensaje("Verificando conectividad con el servicio externo...")
        exito, detalle = self.service.probar_conectividad()
        if exito:
            self.view.mostrar_mensaje(f"[ONLINE] {detalle}")
        else:
            self.view.mostrar_error(f"[OFFLINE] {detalle}")