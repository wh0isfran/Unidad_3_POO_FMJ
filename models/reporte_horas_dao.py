import sqlite3
from typing import List, Optional
from config.database import Database
from models.reporte_horas import ReporteHoras

class ReporteHorasDAO:
    def __init__(self):
        self.db = Database()

    def insertar(self, reporte: ReporteHoras) -> Optional[int]:
        """Guarda un nuevo reporte de horas y devuelve el ID generado."""
        sql = """
            INSERT INTO reporte_horas (
                id_empleado, 
                id_proyecto, 
                horas_trabajadas, 
                fecha, 
                periodo_mes, 
                fecha_generacion
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                sql,
                (
                    reporte.id_empleado,
                    reporte.id_proyecto,
                    reporte.horas_trabajadas,
                    reporte.fecha,
                    reporte.periodo_mes,
                    reporte.fecha_generacion
                )
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error al registrar reporte de horas en BD: {e}")
            return None
        finally:
            conn.close()

    def obtener_por_empleado(self, id_empleado: int) -> List[ReporteHoras]:
        """Obtiene el historial de reportes de horas de un empleado específico."""
        sql = """
            SELECT id_reporte, id_empleado, id_proyecto, horas_trabajadas, fecha, periodo_mes, fecha_generacion
            FROM reporte_horas
            WHERE id_empleado = ?
            ORDER BY id_reporte DESC
        """
        conn = self.db.get_connection()
        reportes = []
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_empleado,))
            for fila in cursor.fetchall():
                reportes.append(ReporteHoras(
                    id_reporte=fila["id_reporte"],
                    id_empleado=fila["id_empleado"],
                    id_proyecto=fila["id_proyecto"],
                    horas_trabajadas=fila["horas_trabajadas"],
                    fecha=fila["fecha"],
                    periodo_mes=fila["periodo_mes"],
                    fecha_generacion=fila["fecha_generacion"]
                ))
        except sqlite3.Error as e:
            print(f"Error al consultar reportes de horas: {e}")
        finally:
            conn.close()
        return reportes

    def listar_todas(self) -> List[ReporteHoras]:
        """Lista todos los reportes de horas emitidos en el sistema."""
        sql = """
            SELECT id_reporte, id_empleado, id_proyecto, horas_trabajadas, fecha, periodo_mes, fecha_generacion
            FROM reporte_horas
            ORDER BY id_reporte DESC
        """
        conn = self.db.get_connection()
        reportes = []
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            for fila in cursor.fetchall():
                reportes.append(ReporteHoras(
                    id_reporte=fila["id_reporte"],
                    id_empleado=fila["id_empleado"],
                    id_proyecto=fila["id_proyecto"],
                    horas_trabajadas=fila["horas_trabajadas"],
                    fecha=fila["fecha"],
                    periodo_mes=fila["periodo_mes"],
                    fecha_generacion=fila["fecha_generacion"]
                ))
        except sqlite3.Error as e:
            print(f"Error al listar reportes de horas: {e}")
        finally:
            conn.close()
        return reportes