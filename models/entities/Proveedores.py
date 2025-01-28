class Proveedores:
    def __init__(self, id, id_empresa, razon_social, regimen_fiscal_id, tipo_id, rfc, pais, estado, 
                 cp, municipio, colonia, calle, numero_exterior, numero_interior, 
                 fecha_registro = None, usuario = None, is_blocked=False) -> None:
        
        self.id = id
        self.id_empresa = id_empresa
        self.razon_social = razon_social
        self.regimen_fiscal_id = regimen_fiscal_id
        self.tipo_id = tipo_id
        self.rfc = rfc
        self.pais = pais
        self.estado = estado
        self.cp = cp
        self.municipio = municipio
        self.colonia = colonia
        self.calle = calle
        self.numero_exterior = numero_exterior
        self.numero_interior = numero_interior
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked
