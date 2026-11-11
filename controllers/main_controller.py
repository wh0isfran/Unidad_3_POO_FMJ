from views.main_view import MainView
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.admin_rrhh_controller import Admin_rrhhController 
from controllers.informe_controller import InformeController
from controllers.registro_tiempo_controller import RegistroTiempoController
from controllers.proyecto_controller import ProyectoController
from controllers.reporte_horas_controller import ReporteHorasController

class MainController:
    def __init__(self, usuario_actual=None):
        self.view = MainView()
        self.admin_rrhh_controller = Admin_rrhhController()
        self.departamento_controller = DepartamentoController()
        self.empleado_controller = EmpleadoController()
        self.proyecto_controller = ProyectoController()
        self.registro_tiempo_controller = RegistroTiempoController()
        self.informe_controller = InformeController()
        self.reporte_horas_controller = ReporteHorasController()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu() 
            
            if opcion == 1:
                self.admin_rrhh_controller.ejecutar()
            elif opcion == 2:
                self.departamento_controller.ejecutar()
            elif opcion == 3:
                self.empleado_controller.ejecutar()
            elif opcion == 4:
                self.proyecto_controller.ejecutar()
            elif opcion == 5:
                self.registro_tiempo_controller.ejecutar()
            elif opcion == 6:
                self.informe_controller.ejecutar()
            elif opcion == 7:
                self.reporte_horas_controller.ejecutar()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo del Sistema de Echotech Solutions. ¡Hasta luego!")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida. Por favor, intente nuevamente.")