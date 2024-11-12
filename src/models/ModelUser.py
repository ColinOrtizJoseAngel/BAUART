from .entities.Usuarios import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            with db.cursor() as cursor:
                # Primera consulta para seleccionar el usuario
                query = """SELECT ID, ID_EMPRESA, NOMBRE_USUARIO, NOMBRE, CONTRASENA, CORREO, IS_BLOCKED, ID_EMPLEADO
                        FROM USUARIOS WHERE NOMBRE_USUARIO = ?"""
                cursor.execute(query, (user.usuario,))
                row = cursor.fetchone()
                
                if row:
                    
                    login_user = User(row[0], user.id_empresa, row[2], row[3], User.check_pass(row[4], user.password), row[5], row[6], row[7])
                    return login_user
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_id(cls, db, id):
        try:
            with db.cursor() as cursor:
                # Accedemos a `user.id` si `user` es un objeto de la clase `User`
                query = "SELECT ID, ID_EMPRESA, NOMBRE_USUARIO, NOMBRE, CONTRASENA, CORREO, IS_BLOCKED, ID_EMPLEADO FROM USUARIOS WHERE ID = ?"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                
                if row:
                    return User(row[0], row[1], row[2], row[3], None, row[5], row[6], row[7])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)
