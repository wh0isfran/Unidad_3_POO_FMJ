from views.utils import leer_numero, leer_texto, confirmar
from models.proyecto import Proyecto

class ProyectoView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("GESTIÓN DE PROYECTOS")
        print("-" * 30)
        print("1.- Crear proyecto")
        print("2.- Editar proyecto")
        print("3.- Eliminar proyecto")
        print("4.- Consultar proyecto por ID")
        print("5.- Listar todos los proyectos")
        print("0.- Volver al menú principal")
        print("-" * 30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo_proyecto() -> dict:
        print("\n--- Crear Nuevo Proyecto ---")
        nombre_proyecto = leer_texto("Ingrese el nombre del proyecto: ")
        descripcion = leer_texto("Ingrese la descripción: ")
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        return {
            "nombre_proyecto": nombre_proyecto,
            "descripcion": descripcion,
            "fecha_inicio": fecha_inicio
        }

    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("Ingrese el ID del proyecto: ")

    @staticmethod
    def mostrar_proyecto(proyecto: Proyecto) -> None:
        print("\n--- Datos del Proyecto ---")
        print(proyecto)
        print("-" * 30)

    @staticmethod
    def mostrar_lista_proyectos(proyectos: list[Proyecto]) -> None:
        print("\n--- Lista de Proyectos ---")
        if not proyectos:
            print("No hay proyectos registrados.")
        else:
            for p in proyectos:
                print(p)
        print("-" * 30)

    @staticmethod
    def formulario_editar_proyecto(proyecto: Proyecto) -> dict:
        print(f"\n--- Editando Proyecto [ID: {proyecto.id_proyecto}] ---")
        print("Deje en blanco si no desea modificar el campo de texto.")

        nuevo_nombre = input(f"Nombre actual ({proyecto.nombre_proyecto}): ")
        if not nuevo_nombre.strip():
            nuevo_nombre = proyecto.nombre_proyecto

        nueva_desc = input(f"Descripción actual ({proyecto.descripcion}): ")
        if not nueva_desc.strip():
            nueva_desc = proyecto.descripcion

        nueva_fecha = input(f"Fecha de inicio actual ({proyecto.fecha_inicio}): ")
        if not nueva_fecha.strip():
            nueva_fecha = proyecto.fecha_inicio

        return {
            "id_proyecto": proyecto.id_proyecto,
            "nombre_proyecto": nuevo_nombre,
            "descripcion": nueva_desc,
            "fecha_inicio": nueva_fecha
        }

    @staticmethod
    def confirmar_eliminacion(nombre: str) -> bool:
        return confirmar(f"¿Está seguro que desea eliminar el proyecto '{nombre}'?")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[PROYECTOS] {mensaje}")