
class Especialidades:

    def __init__(self, id, nombre,fecha_registro = None,usuario=None, is_blocked=False) -> None:

        self.id = id
        self.nombre = nombre
        self.fecha_registro = fecha_registro
        self.usuaruio = usuario
        self.is_blocked = is_blocked