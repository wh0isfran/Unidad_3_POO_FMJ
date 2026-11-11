from models.reporte_horas import ReporteHoras
import sqlite3

class ReporteHorasDAO:
    def __init__(self, db_connection: sqlite3.Connection):
        self.conn = db_connection

    def insertar(self, reporte: ReporteHoras) -> int:
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO reporte_horas (
                id_empleado, 
                id_proyecto, 
                horas_trabajadas, 
                fecha, 
                periodo_mes, 
                fecha_generacion
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            reporte.id_empleado,
            reporte.id_proyecto,
            reporte.horas_trabajadas,
            reporte.fecha,
            reporte.periodo_mes,
            reporte.fecha_generacion
        ))
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_reporte: int) -> ReporteHoras | None:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id_reporte, id_empleado, id_proyecto, horas_trabajadas, 
                   fecha, periodo_mes, fecha_generacion 
            FROM reporte_horas 
            WHERE id_reporte = ?
        """, (id_reporte,))
        
        fila = cursor.fetchone()
        if fila:
            return ReporteHoras(
                id_reporte=fila[0],
                id_empleado=fila[1],
                id_proyecto=fila[2],
                horas_trabajadas=fila[3],
                fecha=fila[4],
                periodo_mes=fila[5],
                fecha_generacion=fila[6]
            )
        return None

    def obtener_todos_por_empleado(self, id_empleado: int) -> list[ReporteHoras]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id_reporte, id_empleado, id_proyecto, horas_trabajadas, 
                   fecha, periodo_mes, fecha_generacion 
            FROM reporte_horas 
            WHERE id_empleado = ?
        """, (id_empleado,))
        
        filas = cursor.fetchall()
        reportes = []
        for fila in filas:
            reporte = ReporteHoras(
                id_reporte=fila[0],
                id_empleado=fila[1],
                id_proyecto=fila[2],
                horas_trabajadas=fila[3],
                fecha=fila[4],
                periodo_mes=fila[5],
                fecha_generacion=fila[6]
            )
            reportes.append(reporte)
        return reportes

    def eliminar(self, id_reporte: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM reporte_horas WHERE id_reporte = ?", (id_reporte,))
        self.conn.commit()
        return cursor.rowcount > 0