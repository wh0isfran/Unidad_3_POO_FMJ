from sqlite3 import Cursor
from config.database import Database
from models.proyecto import Proyecto

class ProyectoDAO:
    @staticmethod
    def crear(proyecto: Proyecto) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO proyecto (nombre_proyecto, descripcion, fecha_inicio) VALUES (?, ?, ?)",
                (proyecto.nombre_proyecto, proyecto.descripcion, proyecto.fecha_inicio)
            )
            conn.commit()
            proyecto.id_proyecto = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear proyecto en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos() -> list[Proyecto]:
        conn = Database().get_connection()
        proyectos = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_proyecto, nombre_proyecto, descripcion, fecha_inicio FROM proyecto")
            filas = cursor.fetchall()
            for fila in filas:
                proyectos.append(Proyecto(fila['nombre_proyecto'], fila['descripcion'], fila['fecha_inicio'], fila['id_proyecto']))
        except Exception as e:
            print(f"Error al obtener proyectos: {e}")
        finally:
            conn.close()
        return proyectos

    @staticmethod
    def obtener_por_id(id_proyecto: int) -> Proyecto | None:
        conn = Database().get_connection()
        proyecto = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_proyecto, nombre_proyecto, descripcion, fecha_inicio FROM proyecto WHERE id_proyecto = ?", (id_proyecto,))
            fila = cursor.fetchone()
            if fila:
                proyecto = Proyecto(fila['nombre_proyecto'], fila['descripcion'], fila['fecha_inicio'], fila['id_proyecto'])
        except Exception as e:
            print(f"Error al obtener el proyecto: {e}")
        finally:
            conn.close()
        return proyecto

    @staticmethod
    def actualizar(proyecto: Proyecto) -> bool:
        if proyecto.id_proyecto is None:
            return False
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "UPDATE proyecto SET nombre_proyecto = ?, descripcion = ?, fecha_inicio = ? WHERE id_proyecto = ?",
                (proyecto.nombre_proyecto, proyecto.descripcion, proyecto.fecha_inicio, proyecto.id_proyecto)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar proyecto: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_proyecto: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM proyecto WHERE id_proyecto = ?", (id_proyecto,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar proyecto: {e}")
            return False
        finally:
            conn.close()