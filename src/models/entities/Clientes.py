
class Clientes():
    
    def __init__(self,id,razon_social,rfc,empresa,cp,estado,municipio,pais,calle,nombre_contacto,apellido_contacto,telefono_contacto,
                correo_contacto,responsable_proyecto,telfono_responsable_proyecto,correo_responsable_proyecto, contacto_emergencia,
                puesto_empresa,regimen_fiscal,uso_cfdi,forma_pago, dias_credito,banco, cuenta_banco,clabe,no_Exterior = "",no_Interior = "",is_blocked=False) -> None:

        self.id = id
        self.razon_social = razon_social
        self.rfc = rfc
        self.empresa = empresa
        self.cp = cp
        self.estado = estado
        self.municipio = municipio
        self.pais = pais
        self.calle = calle
        self.nombre_contacto = nombre_contacto
        self.apellido_contacto = apellido_contacto
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto
        self.responsable_proyecto = responsable_proyecto
        self.telfono_responsable_proyecto = telfono_responsable_proyecto
        self.correo_responsable_proyecto = correo_responsable_proyecto
        self.contacto_emergencia = contacto_emergencia
        self.puesto_empresa = puesto_empresa
        self.regimen_fiscal = regimen_fiscal
        self.uso_cfdi = uso_cfdi
        self.forma_pago = forma_pago
        self.dias_credito = dias_credito
        self.banco = banco
        self.cuenta_banco = cuenta_banco
        self.clabe = clabe
        self.no_Exterior = no_Exterior
        self.no_Interior = no_Interior
        self.is_blocked = is_blocked
