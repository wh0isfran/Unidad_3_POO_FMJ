from views.main_view import MainView
from controllers.usuario_controller import UsuarioController 
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.admin_rrhh_controller import Admin_rrhhController 
from controllers.informe_controller import InformeController
from controllers.registro_tiempo_controller import RegistrotiempoController

class MainController:
    def __init__(self):
        self.view = MainView()
        self.usuario_controller = UsuarioController()
        self.empleado_controller = EmpleadoController()
        self.departamento_controller = DepartamentoController()
        self.admin_rrhh_controller = Admin_rrhhController()
        self.informe_controller = InformeController()
        self.registro_tiempo_controller = RegistrotiempoController()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.usuario_controller.ejecutar()
            elif opcion == 2:
                self.empleado_controller.ejecutar()
            elif opcion == 3:
                self.departamento_controller.ejecutar()
            elif opcion == 4:
                self.admin_rrhh_controller.ejecutar()
            elif opcion == 5:
                self.informe_controller.ejecutar()
            elif opcion == 6:
                self.registro_tiempo_controller.ejecutar()
            elif opcion == 0:
                self.view.mostrar_mensaje("Gracias por usar el sistema de la empresa. ¡Hasta luego!")
                break
            else:
                self.view.mostrar_mensaje("Opción ingresada inválida, intente nuevamente")