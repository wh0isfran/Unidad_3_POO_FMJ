from views.utils import leer_numero, leer_texto, confirmar
from models.usuario import Usuario

class UsuarioView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("GESTIÓN DE USUARIOS")
        print("-" * 30)
        print("1.- Crear usuario")
        print("2.- Editar usuario")
        print("3.- Eliminar usuario")
        print("4.- Consultar usuario por ID")
        print("5.- Listar todos los usuarios")
        print("0.- Volver al menú principal")
        print("-" * 30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo_usuario() -> dict:
        print("\n--- Crear Nuevo Usuario ---")
        usuario = input("Ingrese el nombre de usuario: ")
        tipo_usuario = input("Ingrese el tipo de usuario (empleado o admin): ")
        return {
            "usuario": usuario,
            "tipo_usuario": tipo_usuario
        }

    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("Ingrese el ID del usuario: ")

    @staticmethod
    def mostrar_usuario(usuario: Usuario) -> None:
        print("\n--- Datos del Usuario ---")
        print(usuario)
        print("-" * 30)

    @staticmethod
    def mostrar_lista_usuarios(usuarios: list[Usuario]) -> None:
        print("\n--- Lista de Usuarios ---")
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            for u in usuarios:
                print(u)
        print("-" * 30)

    @staticmethod
    def formulario_editar_usuario(usuario: Usuario) -> dict:
        print(f"\n--- Editando Usuario [ID: {usuario.id_usuario}] ---")
        print("Deje en blanco si no desea modificar el campo de texto.")

        nuevo_usuario = input(f"Usuario actual ({usuario.username}): ")
        if not nuevo_usuario.strip():
            nuevo_usuario = usuario.username

        nuevo_tipo_usuario = input(f"Tipo de usuario actual ({usuario.tipo_usuario}): ")
        if not nuevo_tipo_usuario.strip():
            nuevo_tipo_usuario = usuario.tipo_usuario

        return {
            "id_usuario": usuario.id_usuario,
            "usuario": nuevo_usuario,
            "tipo_usuario": nuevo_tipo_usuario
        }

    @staticmethod
    def confirmar_eliminacion(username: str) -> bool:
        return confirmar(f"¿Está seguro que desea eliminar al usuario '{username}'?")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[USUARIOS] {mensaje}")