from models.admin_rrhh import Admin_rrhh 
from models.admin_rrhh_dao import Admin_rrhhDAO
from views.admin_rrhh_view import Admin_rrhhView

class Admin_rrhhController:
    def __init__(self):
        self.view = Admin_rrhhView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_admin_rrhh()
            elif opcion == 2:
                self.editar_admin_rrhh()
            elif opcion == 3:
                self.eliminar_admin_rrhh()
            elif opcion == 4:
                self.imprimir_admin_rrhh()
            elif opcion == 5:
                self.imprimir_admin_rrhh()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestión de Administradores de RRHH.")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")
    
    def agregar_admin_rrhh(self) -> None:
        datos = self.view.formulario_nuevo_admin_rrhh()
        try:
            nuevo_admin_rrhh = Admin_rrhh(datos['nombre'], datos['apellido_paterno'], datos['apellido_materno'])
            exito = Admin_rrhhDAO.crear(nuevo_admin_rrhh)
            if exito:
                self.view.mostrar_mensaje(f"Administrador agregado exitosamente con ID {nuevo_admin_rrhh.id_admin}.")
            else:
                self.view.mostrar_mensaje(f"Error al guardar en base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos ingresados: {e}")
            
    def editar_admin_rrhh(self) -> None:
        
    