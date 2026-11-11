from models.admin_rrhh import AdminRRHH
from models.admin_rrhh_dao import AdminRrhhDAO
from views.admin_rrhh_view import AdminRrhhView

class Admin_rrhhController:
    def __init__(self):
        self.view = AdminRrhhView()
        self.AdminRrhhDAO = AdminRrhhDAO() 

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
        datos = self.view.formulario_nuevo_admin()
        try:
            nuevo_admin_rrhh = AdminRRHH(datos['nombre'], datos['apellido_paterno'], datos['apellido_materno'])
            exito = self.AdminRrhhDAO.insertar(nuevo_admin_rrhh) 
            if exito:
                self.view.mostrar_mensaje(f"Administrador agregado exitosamente con ID {nuevo_admin_rrhh.id_admin}.")
            else:
                self.view.mostrar_mensaje(f"Error al guardar en base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos ingresados: {e}")
            
        
    def editar_admin_rrhh(self) -> None:
        id_admin_rrhh = self.view.solicitar_id()
        Admin_rrhh = AdminRrhhDAO.obtener_por_id(id_admin_rrhh)
        if not Admin_rrhh:
            self.view.mostrar_mensaje("Administrador no encontrado.")
            return

        datos_nuevos = self.view.formulario_editar_admin_rrhh(Admin_rrhh)
        try:
            Admin_rrhh.nombre = datos_nuevos['nombre']
            Admin_rrhh.apellido_paterno = datos_nuevos['apellido paterno']
            Admin_rrhh.apellido_materno = datos_nuevos['apellido materno']
            
            exito = AdminRrhhDAO.actualizar(Admin_rrhh)
            if exito:
                self.view.mostrar_mensaje("Administrador actualizado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al actualizar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos modificados: {e}")

    def eliminar_admin_rrhh(self) -> None:
        id_admin = self.view.solicitar_id()
        admin_rrhh = AdminRrhhDAO.obtener_por_id(id_admin)
        if not admin_rrhh:
            self.view.mostrar_mensaje("Administrador no encontrado.")
            return

        if self.view.confirmar_eliminacion(admin_rrhh.nombre):
            exito = AdminRrhhDAO.eliminar(id_admin)
            if exito:
                self.view.mostrar_mensaje("Administrador eliminado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al eliminar en la base de datos.")
        else:
            self.view.mostrar_mensaje("Operación cancelada.")

    def imprimir_admin_rrhh(self) -> None:
        id_admin = self.view.solicitar_id()
        admin_rrhh = AdminRrhhDAO.obtener_por_id(id_admin)
        if admin_rrhh:
            self.view.mostrar_admin_rrhh(admin_rrhh)
        else:
            self.view.mostrar_mensaje("Administrador no encontrado.")

    def imprimir_admin_rrhh(self) -> None:
        admin_rrhh = AdminRrhhDAO.obtener_todos()
        self.view.mostrar_lista_administradores(admin_rrhh)              