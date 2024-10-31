from .entities.Usuarios import User

class ModelUser():

    @classmethod
    def login(self,db,user):
        try:
            cursor = db.cursor()

            query = f"""SELECT ID, ID_EMPRESA, NOMBRE_USUARIO, NOMBRE, CONTRASENA,CORREO,IS_BLOCKED FROM Usuarios
              WHERE USUARIOS = '{user.usuario}'"""
            cursor.execute(query)
            row = cursor.fetchone()

            if row:
                user = User(row[0], row[1], User.check_pas(row[2],user.password),row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor = db.cursor()
            query = f"SELECT Id, usuario, Email FROM Usuarios WHERE id = '{id}'"
            cursor.execute(query)
            row = cursor.fetchone()
            print(f"Este es la consulta: {row}")
            if row:
                return  User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
