class MaterialesFamilia:
    def __init__(self, id, id_familia, material,unidad_medida,familia=None, fecha_registro=None, usuario=None, is_blocked=0):
        self.id = id
        self.id_familia = id_familia
        self.material = material
        self.unidad_medida = unidad_medida
        self.familia=familia
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked