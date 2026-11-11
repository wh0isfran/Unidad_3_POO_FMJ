from typing import List, Optional
from views.utils import leer_numero, confirmar
from models.reporte_horas import ReporteHoras

class ReporteHorasView:
    """
    Vista de consola para el módulo de Reportes de Horas y Sincronización API.
    """

    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "="*50)
        print("          MÓDULO DE REPORTE DE HORAS Y API")
        print("="*50)
        print("1. Consultar reportes en API externa")
        print("2. Registrar reporte de horas en BD")
        print("3. Ver reportes de un empleado (por ID)")
        print("4. Listar todos los reportes guardados")
        print("5. Diagnosticar conexión con API externa")
        print("0. Volver al menú principal")
        print("="*50)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def pedir_periodo_busqueda() -> str:
        print("\n--- BÚSQUEDA EN SERVICIO EXTERNO ---")
        return input("Ingrese periodo a consultar (ej. 2026-11): ").strip()

    @staticmethod
    def mostrar_reportes_externos(reportes: List[ReporteHoras]) -> None:
        if not reportes:
            print("\n[INFO] No hay reportes para mostrar.")
            return

        print(f"\n--- REPORTES OBTENIDOS ({len(reportes)}) ---")
        for i, rep in enumerate(reportes, start=1):
            print(f"[{i}] ID Empleado: {rep.id_empleado}")
            print(f"    - ID Proyecto    : {rep.id_proyecto}")
            print(f"    - Horas Trabajadas: {rep.horas_trabajadas} hrs")
            print(f"    - Fecha          : {rep.fecha}")
            print(f"    - Periodo Mes    : {rep.periodo_mes}")
            print("-" * 45)

    @staticmethod
    def seleccionar_reporte(reportes: List[ReporteHoras]) -> Optional[ReporteHoras]:
        if not reportes:
            return None
        while True:
            opc = leer_numero("\nSeleccione el número del reporte a guardar (0 para cancelar): ")
            if opc == 0:
                return None
            if 1 <= opc <= len(reportes):
                return reportes[opc - 1]
            print(f"Por favor, ingrese un número entre 1 y {len(reportes)}.")

    @staticmethod
    def pedir_datos_reporte() -> Optional[dict]:
        print("\n--- REGISTRO MANUAL DE REPORTE DE HORAS ---")
        try:
            id_empleado = int(input("Ingrese ID del Empleado: ").strip())
            id_proyecto = int(input("Ingrese ID del Proyecto: ").strip())
            horas_trabajadas = float(input("Ingrese horas trabajadas (ej. 8.5): ").strip())
        except ValueError:
            print("Error: Los valores numéricos de ID u horas no son válidos.")
            return None

        fecha = input("Ingrese fecha (YYYY-MM-DD): ").strip()
        if not fecha:
            print("Error: La fecha es obligatoria.")
            return None

        periodo_mes = input("Ingrese periodo del mes (ej. 2026-11): ").strip()
        if not periodo_mes:
            print("Error: El periodo del mes es obligatorio.")
            return None

        fecha_generacion = input("Ingrese fecha de generación (YYYY-MM-DD): ").strip()
        if not fecha_generacion:
            print("Error: La fecha de generación es obligatoria.")
            return None

        if not confirmar("¿Confirma la emisión y guardado de este reporte de horas?"):
            print("Operación cancelada.")
            return None

        return {
            "id_empleado": id_empleado,
            "id_proyecto": id_proyecto,
            "horas_trabajadas": horas_trabajadas,
            "fecha": fecha,
            "periodo_mes": periodo_mes,
            "fecha_generacion": fecha_generacion
        }

    @staticmethod
    def pedir_id_empleado() -> int:
        return leer_numero("\nIngrese el ID del empleado a consultar: ")

    @staticmethod
    def mostrar_listado_local(reportes: List[ReporteHoras]) -> None:
        if not reportes:
            print("\n[INFO] No se registraron reportes locales para el empleado.")
            return

        print(f"\n--- HISTORIAL DE REPORTES LOCALES ({len(reportes)}) ---")
        for r in reportes:
            print(f"• Reporte #{r.id_reporte} | Fecha: {r.fecha}")
            print(f"  Empleado ID : {r.id_empleado}")
            print(f"  Proyecto ID : {r.id_proyecto}")
            print(f"  Horas       : {r.horas_trabajadas} hrs")
            print(f"  Periodo     : {r.periodo_mes}")
            print("-" * 40)

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[SISTEMA] {mensaje}")

    @staticmethod
    def mostrar_error(error: str) -> None:
        print(f"\n[ERROR] {error}")