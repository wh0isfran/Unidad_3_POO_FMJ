from views.utils import leer_numero
from models.usuario import Usuario

class MainView:
    @staticmethod
    def mostrar_menu(usuario_actual: Usuario | None = None) -> int:
        print("\n" + "=" * 55)
        print("     EMPRESA ECHOTECH SOLUTIONS - MENÚ PRINCIPAL")
        if usuario_actual:
            print(f"     Sesión activa: {usuario_actual.username} ({usuario_actual.rol})")
        print("=" * 55)
        print("1.- Gestión de Administradores de Recursos Humanos")
        print("2.- Gestión de Departamentos")
        print("3.- Gestión de Empleados")
        print("4.- Gestión de Proyectos")
        print("5.- Gestión de Registros de Tiempo")
        print("6.- Gestión de Informes")
        print("7.- Reporte de horas trabajadas (Consumo de API)")
        print("9.- Cerrar sesión (cambiar de usuario)")
        print("0.- Salir del Sistema")
        print("=" * 55)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[SISTEMA] {mensaje}")