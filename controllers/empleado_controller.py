from models.empleado import Empleado
from models.empleado_dao import EmpleadoDAO
from views.empleado_view import EmpleadoView

class EmpleadoController:
    def __init__(self):
        self.view = EmpleadoView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_empleado()
            elif opcion == 2:
                self.editar_empleado()
            elif opcion == 3:
                self.eliminar_empleado()
            elif opcion == 4:
                self.imprimir_empleado()
            elif opcion == 5:
                self.imprimir_empleados()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestión de empleados.")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")

    def agregar_empleado(self) -> None:
        datos = self.view.formulario_nuevo_empleado()
        try:
            nuevo_empleado = Empleado(
                datos['nombre'], datos['apellido_paterno'], datos['apellido_materno'],
                datos['edad'], datos['direccion'], datos['telefono'], datos['correo']
            )
            exito = EmpleadoDAO.crear(nuevo_empleado)
            if exito:
                self.view.mostrar_mensaje(f"Empleado agregado exitosamente con ID {nuevo_empleado.id_empleado}.")
            else:
                self.view.mostrar_mensaje("Error al guardar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos ingresados: {e}")

    def editar_empleado(self) -> None:
        id_emp = self.view.solicitar_id()
        empleado = EmpleadoDAO.obtener_por_id(id_emp)
        if not empleado:
            self.view.mostrar_mensaje("Empleado no encontrado.")
            return

        datos_nuevos = self.view.formulario_editar_empleado(empleado)
        try:
            empleado.nombre = datos_nuevos['nombre']
            empleado.apellido_paterno = datos_nuevos['apellido_paterno']
            empleado.apellido_materno = datos_nuevos['apellido_materno']
            empleado.edad = datos_nuevos['edad']
            empleado.direccion = datos_nuevos['direccion']
            empleado.telefono = datos_nuevos['telefono']
            empleado.correo = datos_nuevos['correo']

            exito = EmpleadoDAO.actualizar(empleado)
            if exito:
                self.view.mostrar_mensaje("Empleado actualizado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al actualizar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos modificados: {e}")

    def eliminar_empleado(self) -> None:
        id_emp = self.view.solicitar_id()
        empleado = EmpleadoDAO.obtener_por_id(id_emp)
        if not empleado:
            self.view.mostrar_mensaje("Empleado no encontrado.")
            return

        if self.view.confirmar_eliminacion(empleado.nombre):
            exito = EmpleadoDAO.eliminar(id_emp)
            if exito:
                self.view.mostrar_mensaje("Empleado eliminado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al eliminar en la base de datos.")
        else:
            self.view.mostrar_mensaje("Operación cancelada.")

    def imprimir_empleado(self) -> None:
        id_emp = self.view.solicitar_id()
        empleado = EmpleadoDAO.obtener_por_id(id_emp)
        if empleado:
            self.view.mostrar_empleado(empleado)
        else:
            self.view.mostrar_mensaje("Empleado no encontrado.")

    def imprimir_empleados(self) -> None:
        empleados = EmpleadoDAO.obtener_todos()
        self.view.mostrar_lista_empleados(empleados)