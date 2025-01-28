
class Materiales:
    
    def __init__(self, id, clave_id, unidad_medida, descripcion,
                 fecha_registro = None, usuario = None, is_blocked = False) -> None:
        
        self.id = id
        self.clave_id = clave_id
        self.unidad_medida = unidad_medida
        self.descripcion = descripcion
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked