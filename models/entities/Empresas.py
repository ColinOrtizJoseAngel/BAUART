class Empresas:
    def __init__(self, id, razon_social, rfc, repse, regimen_fiscal_id, 
                 nombre_representante1, apellido_representante1, telefono_representante1, correo_representante1,
                 nombre_representante2="", apellido_representante2="", telefono_representante2="", correo_representante2="",
                 nombre_apoderado="", apellido_apoderado="", telefono_apoderado="", correo_apoderado="",
                 cp="", estado="", ciudad="",municipio="", pais="", calle = "", direccion="",no_exterior="",no_interior="", usuario=None,
                 fecha_registro=None, is_blocked=False) -> None:
        
        self.id = id
        self.razon_social = razon_social
        self.rfc = rfc
        self.repse = repse
        self.regimen_fiscal_id = regimen_fiscal_id
        self.nombre_representante1 = nombre_representante1
        self.apellido_representante1 = apellido_representante1
        self.telefono_representante1 = telefono_representante1
        self.correo_representante1 = correo_representante1
        self.nombre_representante2 = nombre_representante2
        self.apellido_representante2 = apellido_representante2
        self.telefono_representante2 = telefono_representante2
        self.correo_representante2 = correo_representante2
        self.nombre_apoderado = nombre_apoderado
        self.apellido_apoderado = apellido_apoderado
        self.telefono_apoderado = telefono_apoderado
        self.correo_apoderado = correo_apoderado
        self.cp = cp
        self.estado = estado
        self.ciudad = ciudad
        self.municipio = municipio
        self.pais = pais
        self.calle = calle
        self.no_exterior = no_exterior
        self.no_interior = no_interior
        self.direccion = direccion
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked