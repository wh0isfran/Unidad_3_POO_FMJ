from views.utils import leer_numero, confirmar
from models.admin_rrhh import AdminRRHH 

class AdminRrhhView:
    
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("GESTIÓN DE RECURSOS HUMANOS (RRHH)")
        print("-" * 30)
        print("1.- Agregar administrador")
        print("2.- Editar administrador")
        print("3.- Eliminar administrador")
        print("4.- Imprimir un administrador")
        print("5.- Imprimir todos los administradores")
        print("0.- Volver al menú principal")
        print("-" * 30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo_admin () -> dict:
        print("\n--- Agregar Nuevo Admin RRHH ---")
        nombre = input("Ingrese el nombre: ")
        apellido_paterno = input("Ingrese el apellido paterno: ")
        apellido_materno = input("Ingrese el apellido materno: ")

        return {
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno
        }

    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("Ingrese el ID del admin: ")

    @staticmethod
    def mostrar_admin(admin_rrhh: AdminRRHH) -> None:
        print("\n--- Datos del Admin RRHH ---")
        print(admin_rrhh)
        print("-" * 30)

    @staticmethod
    def mostrar_lista_admin(lista_admin: list[AdminRRHH]) -> None:
        print("\n--- Lista de Admin RRHH ---")
        if not lista_admin:
            print("No hay admin RRHH registrado.")
        else:
            for p in lista_admin:
                print(p)
            print("-" * 30)

    @staticmethod
    def formulario_editar_admin(admin_rrhh: AdminRRHH) -> dict:
        print(f"\n--- Editando Admin RRHH [ID: {admin_rrhh.id_admin}] ---")
        print("Deje en blanco si no desea modificar el campo de texto.")

        nuevo_nombre = input(f"Nombre actual ({admin_rrhh.nombre}): ")
        if not nuevo_nombre.strip():
            nuevo_nombre = admin_rrhh.nombre

        nuevo_apellido_paterno = input(f"Apellido paterno actual ({admin_rrhh.apellido_paterno}): ")
        if not nuevo_apellido_paterno.strip():
            nuevo_apellido_paterno = admin_rrhh.apellido_paterno

        nuevo_apellido_materno = input(f"Apellido materno actual ({admin_rrhh.apellido_materno}): ")
        if not nuevo_apellido_materno.strip():
            nuevo_apellido_materno = admin_rrhh.apellido_materno

        return {
            "id_admin": admin_rrhh.id_admin,
            "nombre": nuevo_nombre,
            "apellido_paterno": nuevo_apellido_paterno,
            "apellido_materno": nuevo_apellido_materno
        }

    @staticmethod
    def confirmar_eliminacion(nombre: str) -> bool:
        return confirmar(f"¿Está seguro que desea eliminar al admin '{nombre}'?")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[RRHH] {mensaje}")