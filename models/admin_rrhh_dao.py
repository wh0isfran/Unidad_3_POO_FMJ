from sqlite3 import Cursor
from config.database import Database
from models.admin_rrhh import AdminRRHH

class AdminRrhhDAO:
    @staticmethod
    def crear(admin_rrhh: AdminRRHH) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO admin_rrhh (nombre, apellido_paterno, apellido_materno) VALUES (?, ?, ?)",
                (admin_rrhh.nombre, admin_rrhh.apellido_paterno, admin_rrhh.apellido_materno)
            )
            conn.commit()
            admin_rrhh.id_admin = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear admin_rrhh en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos() -> list[AdminRRHH]:
        conn = Database().get_connection()
        admins = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_admin, nombre, apellido_paterno, apellido_materno FROM admin_rrhh")
            filas = cursor.fetchall()
            for fila in filas:
                admins.append(AdminRRHH(
                    fila['nombre'], fila['apellido_paterno'], fila['apellido_materno'], fila['id_admin']
                ))
        except Exception as e:
            print(f"Error al obtener administradores de RRHH: {e}")
        finally:
            conn.close()
        return admins

    @staticmethod
    def obtener_por_id(id_admin: int) -> AdminRRHH | None:
        conn = Database().get_connection()
        admin_rrhh = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_admin, nombre, apellido_paterno, apellido_materno FROM admin_rrhh WHERE id_admin = ?", (id_admin,))
            fila = cursor.fetchone()
            if fila:
                admin_rrhh = AdminRRHH(
                    fila['nombre'], fila['apellido_paterno'], fila['apellido_materno'], fila['id_admin']
                )
        except Exception as e:
            print(f"Error al obtener el administrador de RRHH: {e}")
        finally:
            conn.close()
        return admin_rrhh

    @staticmethod
    def actualizar(admin_rrhh: AdminRRHH) -> bool:
        if admin_rrhh.id_admin is None:
            return False
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "UPDATE admin_rrhh SET nombre = ?, apellido_paterno = ?, apellido_materno = ? WHERE id_admin = ?",
                (admin_rrhh.nombre, admin_rrhh.apellido_paterno, admin_rrhh.apellido_materno, admin_rrhh.id_admin)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar administrador de RRHH: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_admin: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM admin_rrhh WHERE id_admin = ?", (id_admin,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar administrador de RRHH: {e}")
            return False
        finally:
            conn.close()