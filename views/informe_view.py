from views.utils import leer_numero, leer_texto, confirmar
from models.informe import Informe

class InformeView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("GESTIÓN DE INFORMES")
        print("-" * 30)
        print("1.- Crear informe")
        print("2.- Editar informe")
        print("3.- Eliminar informe")
        print("4.- Consultar informe por ID")
        print("5.- Listar todos los informes")
        print("0.- Volver al menú principal")
        print("-" * 30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo_informe() -> dict:
        print("\n--- Crear Nuevo Informe ---")
        titulo = leer_texto("Ingrese el título del informe: ")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        contenido = leer_texto("Ingrese el contenido del informe: ")
        return {
            "titulo": titulo,
            "fecha": fecha,
            "contenido": contenido
        }

    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("Ingrese el ID del informe: ")

    @staticmethod
    def mostrar_informe(informe: Informe) -> None:
        print("\n--- Datos del Informe ---")
        print(informe)
        print("-" * 30)

    @staticmethod
    def mostrar_lista_informes(informes: list[Informe]) -> None:
        print("\n--- Lista de Informes ---")
        if not informes:
            print("No hay informes registrados.")
        else:
            for inf in informes:
                print(inf)
        print("-" * 30)

    @staticmethod
    def formulario_editar_informe(informe: Informe) -> dict:
        print(f"\n--- Editando Informe [ID: {informe.id_informe}] ---")
        print("Deje en blanco si no desea modificar el campo de texto.")

        nuevo_titulo = input(f"Título actual ({informe.titulo}): ")
        if not nuevo_titulo.strip():
            nuevo_titulo = informe.titulo

        nueva_fecha = input(f"Fecha actual ({informe.fecha}): ")
        if not nueva_fecha.strip():
            nueva_fecha = informe.fecha

        nuevo_contenido = input(f"Contenido actual ({informe.contenido}): ")
        if not nuevo_contenido.strip():
            nuevo_contenido = informe.contenido

        return {
            "id_informe": informe.id_informe,
            "titulo": nuevo_titulo,
            "fecha": nueva_fecha,
            "contenido": nuevo_contenido
        }

    @staticmethod
    def confirmar_eliminacion(titulo: str) -> bool:
        return confirmar(f"¿Está seguro que desea eliminar el informe '{titulo}'?")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[INFORMES] {mensaje}")