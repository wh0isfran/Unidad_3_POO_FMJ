from models.proyecto import Proyecto
from models.proyecto_dao import ProyectoDAO
from views.proyecto_view import ProyectoView

class ProyectoController:
    def __init__(self):
        self.view = ProyectoView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_proyecto()
            elif opcion == 2:
                self.editar_proyecto()
            elif opcion == 3:
                self.eliminar_proyecto()
            elif opcion == 4:
                self.imprimir_proyecto()
            elif opcion == 5:
                self.imprimir_proyectos()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestión de proyectos.")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")

    def agregar_proyecto(self) -> None:
        datos = self.view.formulario_nuevo_proyecto()
        try:
            nuevo_proyecto = Proyecto(datos['nombre_proyecto'], datos['descripcion'], datos['fecha_inicio'])
            exito = ProyectoDAO.crear(nuevo_proyecto)
            if exito:
                self.view.mostrar_mensaje(f"Proyecto agregado exitosamente con ID {nuevo_proyecto.id_proyecto}.")
            else:
                self.view.mostrar_mensaje("Error al guardar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos ingresados: {e}")

    def editar_proyecto(self) -> None:
        id_proy = self.view.solicitar_id()
        proyecto = ProyectoDAO.obtener_por_id(id_proy)
        if not proyecto:
            self.view.mostrar_mensaje("Proyecto no encontrado.")
            return

        datos_nuevos = self.view.formulario_editar_proyecto(proyecto)
        try:
            proyecto.nombre_proyecto = datos_nuevos['nombre_proyecto']
            proyecto.descripcion = datos_nuevos['descripcion']
            proyecto.fecha_inicio = datos_nuevos['fecha_inicio']

            exito = ProyectoDAO.actualizar(proyecto)
            if exito:
                self.view.mostrar_mensaje("Proyecto actualizado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al actualizar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos modificados: {e}")

    def eliminar_proyecto(self) -> None:
        id_proy = self.view.solicitar_id()
        proyecto = ProyectoDAO.obtener_por_id(id_proy)
        if not proyecto:
            self.view.mostrar_mensaje("Proyecto no encontrado.")
            return

        if self.view.confirmar_eliminacion(proyecto.nombre_proyecto):
            exito = ProyectoDAO.eliminar(id_proy)
            if exito:
                self.view.mostrar_mensaje("Proyecto eliminado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al eliminar en la base de datos.")
        else:
            self.view.mostrar_mensaje("Operación cancelada.")

    def imprimir_proyecto(self) -> None:
        id_proy = self.view.solicitar_id()
        proyecto = ProyectoDAO.obtener_por_id(id_proy)
        if proyecto:
            self.view.mostrar_proyecto(proyecto)
        else:
            self.view.mostrar_mensaje("Proyecto no encontrado.")

    def imprimir_proyectos(self) -> None:
        proyectos = ProyectoDAO.obtener_todos()
        self.view.mostrar_lista_proyectos(proyectos)