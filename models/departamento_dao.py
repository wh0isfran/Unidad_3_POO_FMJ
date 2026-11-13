from sqlite3 import Cursor
from config.database import Database
from models.departamento import Departamento

class DepartamentoDAO:
    @staticmethod
    def crear(departamento: Departamento) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO departamento (nombre, gerente_id) VALUES (?, ?)",
                (departamento.nombre, departamento.gerente_id)
            )
            conn.commit()
            departamento.id_departamento = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear departamento en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos() -> list[Departamento]:
        conn = Database().get_connection()
        departamentos = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_departamento, nombre, gerente_id FROM departamento")
            filas = cursor.fetchall()
            for fila in filas:
                departamentos.append(Departamento(fila['nombre'], fila['gerente_id'], fila['id_departamento']))
        except Exception as e:
            print(f"Error al obtener departamentos: {e}")
        finally:
            conn.close()
        return departamentos

    @staticmethod
    def obtener_por_id(id_departamento: int) -> Departamento | None:
        conn = Database().get_connection()
        departamento = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_departamento, nombre, gerente_id FROM departamento WHERE id_departamento = ?", (id_departamento,))
            fila = cursor.fetchone()
            if fila:
                departamento = Departamento(fila['nombre'], fila['gerente_id'], fila['id_departamento'])
        except Exception as e:
            print(f"Error al obtener el departamento: {e}")
        finally:
            conn.close()
        return departamento

    @staticmethod
    def actualizar(departamento: Departamento) -> bool:
        if departamento.id_departamento is None:
            return False
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "UPDATE departamento SET nombre = ?, gerente_id = ? WHERE id_departamento = ?",
                (departamento.nombre, departamento.gerente_id, departamento.id_departamento)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar departamento: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_departamento: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM departamento WHERE id_departamento = ?", (id_departamento,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar departamento: {e}")
            return False
        finally:
            conn.close()


    @staticmethod
    def buscar_gerente_por_nombre(nombre: str):
        conn = Database().get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id_empleado, nombre,
                    apellido_paterno, apellido_materno
                FROM empleado
                WHERE LOWER(TRIM(nombre)) = LOWER(TRIM(?))
                OR LOWER(TRIM(
                    nombre || ' ' || apellido_paterno || ' ' ||
                    apellido_materno
                )) = LOWER(TRIM(?))
                """,
                (nombre, nombre)
            )

            return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def existe_nombre(nombre: str) -> bool:
        conn = Database().get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT 1 FROM departamento
                WHERE LOWER(TRIM(nombre)) = LOWER(TRIM(?))
                LIMIT 1
                """,
                (nombre,)
            )

            return cursor.fetchone() is not None

        finally:
            conn.close()
