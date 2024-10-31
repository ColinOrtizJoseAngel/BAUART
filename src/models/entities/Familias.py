
class Familias:

    def __init__(self, id, familia, fecha_registro = None, usuario = None, is_blocked = False) -> None:
        
        self.id = id
        self.familia = familia
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked