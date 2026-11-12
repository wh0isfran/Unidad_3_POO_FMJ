from typing import List, Optional
from views.utils import leer_numero, confirmar
from models.reporte_horas import ReporteHoras

class ReporteHorasView:
    """
    Vista de consola para el módulo de Reportes de Horas y Sincronización API.
    """

    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "=" * 50)
        print("       MÓDULO DE INTEGRACIÓN API")
        print("=" * 50)
        print("1. Consultar reportes desde API externa (DATOS FICTICIOS)")
        print("2. Probar conectividad con API")
        print("0. Volver al menú principal")
        print("=" * 50)

        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def pedir_periodo() -> str:
        while True:
            periodo = input(
                "\nIngrese el período (AAAA-MM): "
            ).strip()

            if not periodo:
                return ""
            import re

            if re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", periodo):
                return periodo
            print("Error: ingrese un período válido. Ejemplo: 2026-11")

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