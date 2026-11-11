from views.reporte_horas_view import ReporteHorasView
from services.reporte_horas_service import ReporteHorasService
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
        periodo = self.view.pedir_periodo_busqueda()
        if not periodo:
            return

        try:
            reportes, estado = self.service.buscar_reportes_externos(periodo)
            self.view.mostrar_mensaje(estado)
            
            if not reportes:
                return

            self.view.mostrar_reportes_externos(reportes)
            rep_seleccionado = self.view.seleccionar_reporte(reportes)
            if not rep_seleccionado:
                return

            datos_extra = self.view.pedir_datos_reporte()
            if not datos_extra:
                return

            # Crear el objeto final combinando datos de la API y formularios validados
            nuevo_reporte = ReporteHoras(
                id_empleado=datos_extra["id_empleado"],
                id_proyecto=datos_extra["id_proyecto"],
                horas_trabajadas=datos_extra["horas_trabajadas"],
                fecha=datos_extra["fecha"],
                periodo_mes=datos_extra["periodo_mes"],
                fecha_generacion=datos_extra["fecha_generacion"]
            )

            # Persistencia en SQLite
            id_generado = self.reporte_dao.insertar(nuevo_reporte)
            if id_generado:
                nuevo_reporte.id_reporte = id_generado
                self.view.mostrar_mensaje(
                    f"Reporte #{id_generado} emitido y guardado con éxito en SQLite!\n"
                    f"Empleado ID: {nuevo_reporte.id_empleado} | Proyecto ID: {nuevo_reporte.id_proyecto} | Horas: {nuevo_reporte.horas_trabajadas}h"
                )
            else:
                self.view.mostrar_error("No se pudo guardar el reporte en la base de datos.")

        except ValueError as e:
            self.view.mostrar_error(str(e))
        except Exception as e:
            self.view.mostrar_error(f"Error al emitir reporte: {str(e)}")

    def consultar_reportes_empleado(self) -> None:
        id_emp = self.view.pedir_id_empleado()
        if not id_emp:
            return
        reportes = self.reporte_dao.obtener_todos_por_empleado(id_emp)
        self.view.mostrar_listado_local(reportes)

    def listar_todos_reportes(self) -> None:
        # Asumiendo que el DAO tiene un método para listar todos, o puedes adaptarlo según tus necesidades
        reportes = getattr(self.reporte_dao, "obtener_todos", lambda: [])()
        self.view.mostrar_listado_local(reportes)

    def diagnosticar_conexion(self) -> None:
        self.view.mostrar_mensaje("Verificando conectividad con el servicio externo...")
        exito, detalle = self.service.probar_conectividad()
        if exito:
            self.view.mostrar_mensaje(f"[ONLINE] {detalle}")
        else:
            self.view.mostrar_error(f"[OFFLINE] {detalle}")