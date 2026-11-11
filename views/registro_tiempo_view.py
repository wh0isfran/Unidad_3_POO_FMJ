from views.utils import leer_numero, leer_texto, confirmar
from models.registro_tiempo import RegistroTiempo

class RegistroTiempoView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("GESTIÓN DE REGISTRO DE TIEMPO")
        print("-" * 30)
        print("1.- Registrar tiempo")
        print("2.- Editar registro de tiempo")
        print("3.- Eliminar registro de tiempo")
        print("4.- Consultar registro por ID")
        print("5.- Listar todos los registros")
        print("0.- Volver al menú principal")
        print("-" * 30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo_registro() -> dict:
        print("\n--- Registrar Nuevo Tiempo ---")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        hora = input("Ingrese la hora (HH:MM): ")
        descripcion = leer_texto("Ingrese la descripción: ")
        return {
            "fecha": fecha,
            "hora": hora,
            "descripcion": descripcion
        }

    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("Ingrese el ID del registro de tiempo: ")

    @staticmethod
    def mostrar_registro(registro: RegistroTiempo) -> None:
        print("\n--- Datos del Registro de Tiempo ---")
        print(registro)
        print("-" * 30)

    @staticmethod
    def mostrar_lista_registros(registros: list[RegistroTiempo]) -> None:
        print("\n--- Lista de Registros de Tiempo ---")
        if not registros:
            print("No hay registros de tiempo guardados.")
        else:
            for r in registros:
                print(r)
        print("-" * 30)

    @staticmethod
    def formulario_editar_registro(registro: RegistroTiempo) -> dict:
        print(f"\n--- Editando Registro de Tiempo [ID: {registro.id_registro}] ---")
        print("Deje en blanco si no desea modificar el campo de texto.")

        nueva_fecha = input(f"Fecha actual ({registro.fecha}): ")
        if not nueva_fecha.strip():
            nueva_fecha = registro.fecha

        nueva_hora = input(f"Hora actual ({registro.hora}): ")
        if not nueva_hora.strip():
            nueva_hora = registro.hora

        nueva_desc = input(f"Descripción actual ({registro.descripcion}): ")
        if not nueva_desc.strip():
            nueva_desc = registro.descripcion

        return {
            "id_registro": registro.id_registro,
            "fecha": nueva_fecha,
            "hora": nueva_hora,
            "descripcion": nueva_desc
        }

    @staticmethod
    def confirmar_eliminacion(id_reg: str) -> bool:
        return confirmar(f"¿Está seguro que desea eliminar el registro de tiempo ID '{id_reg}'?")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[REGISTRO TIEMPO] {mensaje}")