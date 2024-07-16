
class Empresas():

    def __init__(self,id,repse,razon_social,rfc,noregis1,
                 nombre_representante1,apellido_representante1,telefono_representante1,correo_representante1,cp,reg_fiscal,
                 nombre_representante2 = "",apellido_representante2="",telefono_representante2 = "",correo_representante2 = "",
                 nombre_apoderado = "",apellido_apoderado = "",telefono_apoderado = "",correo_apoderado = "",noregis2 ="",
                 noregis3="",noregis4="",estado="",ciudad = "",direccion = "",is_blocked = False) -> None:
        
            self.id = id
            self.repse = repse
            self.razon_social = razon_social
            self.rfc = rfc
            self.noregis1 = noregis1
            self.nombre_representante1 = nombre_representante1
            self.apellido_representante1 = apellido_representante1
            self.telefono_representante1 = telefono_representante1
            self.correo_representante1 = correo_representante1
            self.cp = cp
            self.reg_fiscal = reg_fiscal
            self.nombre_representante2 = nombre_representante2
            self.apellido_representante2 = apellido_representante2
            self.telefono_representante2 = telefono_representante2
            self.correo_representante2 = correo_representante2
            self.nombre_apoderado = nombre_apoderado
            self.apellido_apoderado = apellido_apoderado
            self.telefono_apoderado = telefono_apoderado
            self.correo_apoderado = correo_apoderado
            self.noregis2 = noregis2
            self.noregis3 = noregis3
            self.noregis4 = noregis4
            self.estado = estado
            self.ciudad = ciudad
            self.direccion = direccion
            self.is_blocked = is_blocked


      