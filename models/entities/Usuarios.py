from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, login_user

class User(UserMixin):
    def __init__(self, id, id_empresa, usuario, nombre, password, email="", is_bloked=False, id_empleado=None):
        self.id = id
        self.id_empresa = id_empresa
        self.usuario = usuario
        self.nombre = nombre
        self.password = password
        self.email = email
        self.is_bloked = is_bloked
        self.id_empleado = id_empleado

    @classmethod
    def check_pass(self,hashed_password,password):
        return check_password_hash(hashed_password,password)

    
    def hash_password(password):
        return generate_password_hash(password)

    print(hash_password("Bauart@2024$"))
        
        