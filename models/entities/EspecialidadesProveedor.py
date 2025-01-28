class EspecialidadesProveedor:

    def __init__(self,id,id_especialidad,id_proveedor,descripcion = None,
                 fecha_registro = None,usuario = None, is_blocked = False) -> None:
        
        self.id = id
        self.id_especialidad = id_especialidad
        self.id_proveedor = id_proveedor
        self.descripcion = descripcion
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked
    
