from sqlite3 import Cursor
from config.database import Database
from models.informe import Informe

class InformeDAO:
    @staticmethod
    def crear(informe: Informe) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO informe (titulo, fecha, contenido) VALUES (?, ?, ?)",
                (informe.titulo, informe.fecha, informe.contenido)
            )
            conn.commit()
            informe.id_informe = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear informe en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos() -> list[Informe]:
        conn = Database().get_connection()
        informes = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_informe, titulo, fecha, contenido FROM informe")
            filas = cursor.fetchall()
            for fila in filas:
                informes.append(Informe(fila['titulo'], fila['fecha'], fila['contenido'], fila['id_informe']))
        except Exception as e:
            print(f"Error al obtener informes: {e}")
        finally:
            conn.close()
        return informes

    @staticmethod
    def obtener_por_id(id_informe: int) -> Informe | None:
        conn = Database().get_connection()
        informe = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_informe, titulo, fecha, contenido FROM informe WHERE id_informe = ?", (id_informe,))
            fila = cursor.fetchone()
            if fila:
                informe = Informe(fila['titulo'], fila['fecha'], fila['contenido'], fila['id_informe'])
        except Exception as e:
            print(f"Error al obtener el informe: {e}")
        finally:
            conn.close()
        return informe

    @staticmethod
    def actualizar(informe: Informe) -> bool:
        if informe.id_informe is None:
            return False
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "UPDATE informe SET titulo = ?, fecha = ?, contenido = ? WHERE id_informe = ?",
                (informe.titulo, informe.fecha, informe.contenido, informe.id_informe)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar informe: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_informe: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM informe WHERE id_informe = ?", (id_informe,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar informe: {e}")
            return False
        finally:
            conn.close()