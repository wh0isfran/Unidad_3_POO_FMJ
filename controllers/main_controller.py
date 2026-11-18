from controllers.admin_rrhh_controller import AdminRrhhController
from controllers.auth_controller import AuthController
from controllers.cambio_moneda_controller import CambioMonedaController
from controllers.departamento_controller import DepartamentoController
from controllers.empleado_controller import EmpleadoController
from controllers.informe_controller import InformeController
from controllers.proyecto_controller import ProyectoController
from controllers.registro_tiempo_controller import RegistroTiempoController
from models.usuario import Usuario
from views.main_view import MainView


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
        self.cambio_moneda_controller = CambioMonedaController()
        self.usuario_actual: Usuario | None = None

    def tiene_permiso(self, opcion: int) -> bool:
        if self.usuario_actual is None:
            return False   

        permisos = {
            "Administrador RRHH": set(range(1,9)), # Acceso a todas las opciones
            "Operador": {2, 3, 4, 5, 6, 7}, # Acceso a opciones 2-7
            "Empleado": {7}
        }

        return opcion in permisos.get(self.usuario_actual.rol, set())

    def ejecutar(self) -> None:
        
        self.usuario_actual = self.auth_controller.iniciar_sesion()
        if not self.usuario_actual:
            self.view.mostrar_mensaje("El programa ha finalizado debido a credenciales inválidas.")
            return

        while True:
            opcion = self.view.mostrar_menu(self.usuario_actual)
            if opcion not in (0,9) and not self.tiene_permiso(opcion):
                self.view.mostrar_mensaje("Acceso denegado. No tiene permiso para acceder a esta opción.")
                continue
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
                self.cambio_moneda_controller.ejecutar()
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