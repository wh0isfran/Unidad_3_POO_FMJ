from sqlite3 import Cursor
from config.database import Database
from models.empleado import Empleado

class EmpleadoDAO:
    """
    Data Access Object para la entidad Empleado.
    Maneja las operaciones CRUD en la base de datos.
    """

    @staticmethod
    def crear(empleado: Empleado) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO empleado (nombre, apellido_paterno, apellido_materno, edad, direccion, telefono, correo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (empleado.nombre, empleado.apellido_paterno, empleado.apellido_materno, empleado.edad, empleado.direccion, empleado.telefono, empleado.correo)
            )
            conn.commit()
            empleado.id_empleado = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear empleado en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos() -> list[Empleado]:
        conn = Database().get_connection()
        empleados = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_empleado, nombre, apellido_paterno, apellido_materno, edad, direccion, telefono, correo FROM empleado")
            filas = cursor.fetchall()
            for fila in filas:
                empleados.append(Empleado(
                    fila['nombre'], fila['apellido_paterno'], fila['apellido_materno'],
                    fila['edad'], fila['direccion'], fila['telefono'], fila['correo'], fila['id_empleado']
                ))
        except Exception as e:
            print(f"Error al obtener empleados: {e}")
        finally:
            conn.close()
        return empleados

    @staticmethod
    def obtener_por_id(id_empleado: int) -> Empleado | None:
        conn = Database().get_connection()
        empleado = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_empleado, nombre, apellido_paterno, apellido_materno, edad, direccion, telefono, correo FROM empleado WHERE id_empleado = ?", (id_empleado,))
            fila = cursor.fetchone()
            if fila:
                empleado = Empleado(
                    fila['nombre'], fila['apellido_paterno'], fila['apellido_materno'],
                    fila['edad'], fila['direccion'], fila['telefono'], fila['correo'], fila['id_empleado']
                )
        except Exception as e:
            print(f"Error al obtener el empleado: {e}")
        finally:
            conn.close()
        return empleado

    @staticmethod
    def actualizar(empleado: Empleado) -> bool:
        if empleado.id_empleado is None:
            return False
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "UPDATE empleado SET nombre = ?, apellido_paterno = ?, apellido_materno = ?, edad = ?, direccion = ?, telefono = ?, correo = ? WHERE id_empleado = ?",
                (empleado.nombre, empleado.apellido_paterno, empleado.apellido_materno, empleado.edad, empleado.direccion, empleado.telefono, empleado.correo, empleado.id_empleado)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_empleado: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM empleado WHERE id_empleado = ?", (id_empleado,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False
        finally:
            conn.close()