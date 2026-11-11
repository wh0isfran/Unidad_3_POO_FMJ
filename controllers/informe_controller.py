from models.informe import Informe
from models.informe_dao import InformeDAO
from views.informe_view import InformeView

class InformeController:
    def __init__(self):
        self.view = InformeView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_informe()
            elif opcion == 2:
                self.editar_informe()
            elif opcion == 3:
                self.eliminar_informe()
            elif opcion == 4:
                self.imprimir_informe()
            elif opcion == 5:
                self.imprimir_informes()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestión de informes.")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")

    def agregar_informe(self) -> None:
        datos = self.view.formulario_nuevo_informe()
        try:
            nuevo_informe = Informe(datos['titulo'], datos['fecha'], datos['contenido'])
            exito = InformeDAO.crear(nuevo_informe)
            if exito:
                self.view.mostrar_mensaje(f"Informe agregado exitosamente con ID {nuevo_informe.id_informe}.")
            else:
                self.view.mostrar_mensaje("Error al guardar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos ingresados: {e}")

    def editar_informe(self) -> None:
        id_inf = self.view.solicitar_id()
        informe = InformeDAO.obtener_por_id(id_inf)
        if not informe:
            self.view.mostrar_mensaje("Informe no encontrado.")
            return

        datos_nuevos = self.view.formulario_editar_informe(informe)
        try:
            informe.titulo = datos_nuevos['titulo']
            informe.fecha = datos_nuevos['fecha']
            informe.contenido = datos_nuevos['contenido']

            exito = InformeDAO.actualizar(informe)
            if exito:
                self.view.mostrar_mensaje("Informe actualizado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al actualizar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos modificados: {e}")

    def eliminar_informe(self) -> None:
        id_inf = self.view.solicitar_id()
        informe = InformeDAO.obtener_por_id(id_inf)
        if not informe:
            self.view.mostrar_mensaje("Informe no encontrado.")
            return

        if self.view.confirmar_eliminacion(informe.titulo):
            exito = InformeDAO.eliminar(id_inf)
            if exito:
                self.view.mostrar_mensaje("Informe eliminado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al eliminar en la base de datos.")
        else:
            self.view.mostrar_mensaje("Operación cancelada.")

    def imprimir_informe(self) -> None:
        id_inf = self.view.solicitar_id()
        informe = InformeDAO.obtener_por_id(id_inf)
        if informe:
            self.view.mostrar_informe(informe)
        else:
            self.view.mostrar_mensaje("Informe no encontrado.")

    def imprimir_informes(self) -> None:
        informes = InformeDAO.obtener_todos()
        self.view.mostrar_lista_informes(informes)