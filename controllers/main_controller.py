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
        self.usuario_actual = usuario_actual
        self.reporte_horas_controller = ReporteHorasController()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu(self.usuario_actual)
            
            if opcion == 1:
                self.view.mostrar_mensaje("Módulo de Administradores de RRHH")
            elif opcion == 2:
                self.view.mostrar_mensaje("Módulo de Departamentos")
            elif opcion == 3:
                self.view.mostrar_mensaje("Módulo de Empleados")
            elif opcion == 4:
                self.view.mostrar_mensaje("Módulo de Proyectos")
            elif opcion == 5:
                self.view.mostrar_mensaje("Módulo de Registros de Tiempo")
            elif opcion == 6:
                self.view.mostrar_mensaje("Módulo de Informes")
            elif opcion == 7:
                self.view.mostrar_mensaje("Módulo de Usuarios ")
            elif opcion == 8:
                self.reporte_horas_controller.ejecutar()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo del Sistema de Echotech Solutions. ¡Hasta luego!")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida. Por favor, intente nuevamente.")