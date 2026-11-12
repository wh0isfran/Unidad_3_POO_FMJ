from views.main_view import MainView
from controllers.auth_controller import AuthController
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.admin_rrhh_controller import AdminRrhhController 
from controllers.informe_controller import InformeController
from controllers.registro_tiempo_controller import RegistroTiempoController
from controllers.proyecto_controller import ProyectoController
from controllers.reporte_horas_controller import ReporteHorasController
from models.usuario import Usuario


class MainController:
    def __init__(self):
        self.view = MainView()
        self.auth_controller = AuthController()
        self.admin_rrhh_controller = AdminRrhhController()
        self.departamento_controller = DepartamentoController()
        self.empleado_controller = EmpleadoController()
        self.proyecto_controller = ProyectoController()
        self.registro_tiempo_controller = RegistroTiempoController()
        self.informe_controller = InformeController()
        self.reporte_horas_controller = ReporteHorasController()
        self.usuario_actual: Usuario | None = None

    def ejecutar(self) -> None:
        
        self.usuario_actual = self.auth_controller.iniciar_sesion()
        if not self.usuario_actual:
            self.view.mostrar_mensaje("El programa ha finalizado debido a credenciales inválidas.")
            return

        while True:
            opcion = self.view.mostrar_menu(self.usuario_actual)
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
            elif opcion == 8:
                self.auth_controller.ejecutar(self.usuario_actual)
            elif opcion == 9:
                self.view.mostrar_mensaje(f"Cerrando sesión de '{self.usuario_actual.username}'...")
                self.usuario_actual = self.auth_controller.iniciar_sesion()
                if not self.usuario_actual:
                    self.view.mostrar_mensaje("El programa ha finalizado debido a credenciales inválidas.")
                    break
            elif opcion == 0:
                self.view.mostrar_mensaje("Gracias por usar el sistema de la Empresa. ¡Hasta luego!")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida. Por favor, intente nuevamente.")