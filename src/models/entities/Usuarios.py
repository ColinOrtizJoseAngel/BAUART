from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__ (self, id,id_empresa,usuario, password,email = "", ) -> None:
        self.id = id
        
        self.usuario = usuario
        self.password = password
        self.email = email


    @classmethod
    def check_pass(self,hashed_password,password):
        return check_password_hash(hashed_password,password)


print(generate_password_hash("admin123"))

        
        