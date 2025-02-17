from .entities.Usuarios import User
from datetime import datetime

class ModelUser():

    @classmethod
    def login(cls, db, user):
        try:
            with db.cursor() as cursor:
                # Consulta para seleccionar el usuario con Nivel_Acceso incluido
                query = """SELECT ID, ID_EMPRESA, NOMBRE_USUARIO, NOMBRE, CONTRASENA, CORREO, IS_BLOCKED, ID_EMPLEADO, Nivel_Acceso
                        FROM USUARIOS WHERE NOMBRE_USUARIO = ?"""
                cursor.execute(query, (user.usuario,))
                row = cursor.fetchone()
                
                if row:
                    return User(
                        row[0], row[1], row[2], row[3], 
                        User.check_pass(row[4], user.password), row[5], row[6], 
                        row[7], int(row[8]) if row[8] is not None else 1  # Asegurar que Nivel_Acceso sea int
                    )
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def actualizar_empresa(cls, db, nombre_usuario, nueva_empresa_id):
        try:
            with db.cursor() as cursor:
                query = "UPDATE USUARIOS SET ID_EMPRESA = ? WHERE NOMBRE_USUARIO = ?"
                cursor.execute(query, (nueva_empresa_id, nombre_usuario))
                db.commit()
            return True
        except Exception as ex:
            db.rollback()
            print(f"Error al actualizar la empresa: {ex}")
            return False

    @classmethod
    def get_by_id(cls, db, id):
        try:
            with db.cursor() as cursor:
                # Consulta con Nivel_Acceso incluido
                query = """SELECT ID, ID_EMPRESA, NOMBRE_USUARIO, NOMBRE, CONTRASENA, CORREO, IS_BLOCKED, ID_EMPLEADO, Nivel_Acceso 
                        FROM USUARIOS WHERE ID = ?"""
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                
                if row:
                    return User(
                        row[0], row[1], row[2], row[3], None, row[5], 
                        row[6], row[7], int(row[8]) if row[8] is not None else 1
                    )
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def register(cls, db, user):
        try:
            with db.cursor() as cursor:
                query = """INSERT INTO USUARIOS (ID_EMPRESA, NOMBRE_USUARIO, NOMBRE, CONTRASENA, CORREO, IS_BLOCKED, ID_EMPLEADO, FECHA_REGISTRO)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                fecha_registro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 🔥 Formato correcto para SQL Server
                cursor.execute(query, (
                    user.id_empresa,
                    user.usuario,
                    user.nombre,
                    user.password,
                    user.email,
                    user.is_bloked,
                    user.id_empleado,
                    fecha_registro
                ))
                db.commit()
                return True
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def get_by_username(cls, db, username):
        try:
            with db.cursor() as cursor:
                query = "SELECT ID FROM USUARIOS WHERE NOMBRE_USUARIO = ?"
                cursor.execute(query, (username,))
                row = cursor.fetchone()
                return row is not None  # Retorna True si el usuario ya existe, False si no
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def asignar_proceso(cls, db, usuario, id_proceso):
        """ Asigna un proceso a un usuario si no lo tiene asignado. """
        try:
            with db.cursor() as cursor:
                # Verificar si el usuario ya tiene asignado el proceso
                query_check = "SELECT COUNT(*) FROM PERMISOS WHERE usuario = ? AND id_proceso = ?"
                cursor.execute(query_check, (usuario, id_proceso))
                existe = cursor.fetchone()[0]

                if existe:
                    return False  # Ya existe, no hace nada

                # Insertar la asignación si no existe
                query_insert = "INSERT INTO PERMISOS (usuario, id_proceso) VALUES (?, ?)"
                cursor.execute(query_insert, (usuario, id_proceso))
                db.commit()
                return True
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al asignar proceso: {ex}")

    @classmethod
    def desasignar_proceso(cls, db, usuario, id_proceso):
        """ Elimina la asignación de un proceso para un usuario. """
        try:
            with db.cursor() as cursor:
                query = "DELETE FROM PERMISOS WHERE usuario = ? AND id_proceso = ?"
                cursor.execute(query, (usuario, id_proceso))
                db.commit()
                return True
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al desasignar proceso: {ex}")