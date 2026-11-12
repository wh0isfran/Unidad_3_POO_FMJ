from sqlite3 import Cursor
from config.database import Database
from models.registro_tiempo import RegistroTiempo

class RegistroTiempoDAO:
    @staticmethod
    def crear(registro: RegistroTiempo) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO registro_tiempo (fecha, hora, descripcion, id_empleado, id_proyecto) VALUES (?, ?, ?, ?, ?)",
                (registro.fecha, registro.hora, registro.descripcion, registro.id_empleado, registro.id_proyecto)
            )
            conn.commit()
            registro.id_registro = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear registro de tiempo en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos() -> list[RegistroTiempo]:
        conn = Database().get_connection()
        registros = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_registro, fecha, hora, descripcion, id_empleado, id_proyecto FROM registro_tiempo")
            filas = cursor.fetchall()
            for fila in filas:
                registros.append(RegistroTiempo(
                    fecha=fila['fecha'],
                    hora=fila['hora'],
                    descripcion=fila['descripcion'],
                    id_registro=fila['id_registro'],
                    id_empleado=fila['id_empleado'],
                    id_proyecto=fila['id_proyecto']
                ))
        except Exception as e:
            print(f"Error al obtener registros de tiempo: {e}")
        finally:
            conn.close()
        return registros

    @staticmethod
    def obtener_por_id(id_registro: int) -> RegistroTiempo | None:
        conn = Database().get_connection()
        registro = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_registro, fecha, hora, descripcion, id_empleado, id_proyecto FROM registro_tiempo WHERE id_registro = ?", (id_registro,))
            fila = cursor.fetchone()
            if fila:
                registro = RegistroTiempo(
                    fecha=fila['fecha'],
                    hora=fila['hora'],
                    descripcion=fila['descripcion'],
                    id_registro=fila['id_registro'],
                    id_empleado=fila['id_empleado'],
                    id_proyecto=fila['id_proyecto']
                )
        except Exception as e:
            print(f"Error al obtener el registro de tiempo: {e}")
        finally:
            conn.close()
        return registro

    @staticmethod
    def actualizar(registro: RegistroTiempo) -> bool:
        if registro.id_registro is None:
            return False
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "UPDATE registro_tiempo SET fecha = ?, hora = ?, descripcion = ?, id_empleado = ?, id_proyecto = ? WHERE id_registro = ?",
                (registro.fecha, registro.hora, registro.descripcion, registro.id_empleado, registro.id_proyecto, registro.id_registro)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar registro de tiempo: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_registro: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM registro_tiempo WHERE id_registro = ?", (id_registro,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar registro de tiempo: {e}")
            return False
        finally:
            conn.close()