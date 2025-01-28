class Clientes:
    
    def __init__(self, id, id_empresa, razon_social, rfc, cp, estado, ciudad, municipio, pais, calle, no_exterior,
                 regimen_fiscal_id, uso_cfdi_id, condicion_pago, forma_pago_id, fecha_registro=None, usuario=None, is_blocked=False) -> None:

        self.id = id
        self.id_empresa = id_empresa
        self.razon_social = razon_social
        self.rfc = rfc
        self.cp = cp
        self.estado = estado
        self.ciudad = ciudad
        self.municipio = municipio
        self.pais = pais
        self.calle = calle
        self.no_exterior = no_exterior
        self.regimen_fiscal_id = regimen_fiscal_id
        self.uso_cfdi_id = uso_cfdi_id
        self.condicion_pago = condicion_pago
        self.forma_pago_id = forma_pago_id
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked