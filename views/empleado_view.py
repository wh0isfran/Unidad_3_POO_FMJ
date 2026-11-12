from views.utils import leer_numero, leer_texto, confirmar
from models.empleado import Empleado

class EmpleadoView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("GESTIÓN DE EMPLEADOS")
        print("-" * 30)
        print("1.- Agregar empleado")
        print("2.- Editar empleado")
        print("3.- Eliminar empleado")
        print("4.- Imprimir un empleado")
        print("5.- Imprimir todos los empleados")
        print("0.- Volver al menú principal")
        print("-" * 30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo_empleado() -> dict:
        print("\n--- Agregar Nuevo Empleado ---")
        rut = input("Ingrese el RUT del empleado: ")
        nombre = leer_texto("Ingrese el nombre del empleado: ")
        apellido_paterno = leer_texto("Ingrese el apellido paterno del empleado: ")
        apellido_materno = leer_texto("Ingrese el apellido materno del empleado: ")
        edad = leer_numero("Ingrese la edad del empleado: ")
        direccion = leer_texto("Ingrese la dirección del empleado: ")
        telefono = input("Ingrese el teléfono del empleado: ")
        correo = input("Ingrese el correo electrónico: ")
        return {
            "rut": rut,
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "edad": edad,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo
        }

    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("Ingrese el ID del empleado: ")

    @staticmethod
    def mostrar_empleado(empleado: Empleado) -> None:
        print("\n--- Datos del Empleado ---")
        print(empleado)
        print("-" * 30)

    @staticmethod
    def mostrar_lista_empleados(empleados: list[Empleado]) -> None:
        print("\n--- Lista de Empleados ---")
        if not empleados:
            print("No hay empleados registrados.")
        else:
            for e in empleados:
                print(e)
        print("-" * 30)

    @staticmethod
    def formulario_editar_empleado(empleado: Empleado) -> dict:
        print(f"\n--- Editando Empleado [ID: {empleado.id_empleado}] ---")
        print("Deje en blanco si no desea modificar el campo de texto.")

        nuevo_nombre = input(f"Nombre actual ({empleado.nombre}): ")
        if not nuevo_nombre.strip():
            nuevo_nombre = empleado.nombre

        nuevo_apellido_paterno = input(f"Apellido paterno actual ({empleado.apellido_paterno}): ")
        if not nuevo_apellido_paterno.strip():
            nuevo_apellido_paterno = empleado.apellido_paterno

        nuevo_apellido_materno = input(f"Apellido materno actual ({empleado.apellido_materno}): ")
        if not nuevo_apellido_materno.strip():
            nuevo_apellido_materno = empleado.apellido_materno

        nueva_edad_input = input(f"Edad actual ({empleado.edad}): ")
        try:
            nueva_edad = int(nueva_edad_input) if nueva_edad_input.strip() else empleado.edad
        except ValueError:
            nueva_edad = empleado.edad

        nuevo_correo = input(f"Correo actual ({empleado.correo}): ")
        if not nuevo_correo.strip():
            nuevo_correo = empleado.correo

        return {
            "id_empleado": empleado.id_empleado,
            "nombre": nuevo_nombre,
            "apellido_paterno": nuevo_apellido_paterno,
            "apellido_materno": nuevo_apellido_materno,
            "edad": nueva_edad,
            "direccion": nueva_direccion,
            "telefono": nuevo_telefono,
            "correo": nuevo_correo
        }

    @staticmethod
    def confirmar_eliminacion(nombre: str) -> bool:
        return confirmar(f"¿Está seguro que desea eliminar al empleado '{nombre}'?")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[EMPLEADOS] {mensaje}")