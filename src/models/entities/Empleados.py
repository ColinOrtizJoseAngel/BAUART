class Empleados:
    def __init__(self, id, nombre, apellido, id_empresa, puesto,
                 tipo_empleado, tipo_nomina, sueldo_imss, monedero, nomina, banco,
                 numero_cuenta, clabe, alta_empleado="", baja_empleado="", fecha_registro="", is_blocked=False,
                 categoria="", no_imss="", curp="", ine="", rfc="", cedula_profesional="",
                 estado_civil="", fecha_nacimiento="", telefono_contacto="", domicilio="",
                 tope_horas_extra=0, foto_base64="", tipo_sangre="", lugar_nacimiento="",
                 sexo="", calle="", manzana="", lote="", numero_exterior="", numero_interior="",
                 colonia="", codigo_postal="", estado="", telefono_domicilio="", cuenta_correo="",
                 salario_diario_integrado=0.0, numero_credito_infonavit="", tipo_descuento_infonavit="",
                 factor_infonavit=0.0, fecha_ingreso="", turno="", tipo_contrato="", contacto_accidente="",
                 alergias="", enfermedades_controladas="", edificio="", alcaldia="", municipio="",
                 registro_patronal="", cuenta="", motivo_baja="", id_monedero="") -> None:

        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.id_empresa = id_empresa
        self.puesto = puesto
        self.tipo_empleado = tipo_empleado
        self.tipo_nomina = tipo_nomina
        self.sueldo_imss = sueldo_imss
        self.monedero = monedero
        self.nomina = nomina
        self.banco = banco
        self.numero_cuenta = numero_cuenta
        self.clabe = clabe
        self.alta_empleado = alta_empleado
        self.baja_empleado = baja_empleado
        self.fecha_registro = fecha_registro
        self.is_blocked = is_blocked
        self.categoria = categoria
        self.no_imss = no_imss
        self.curp = curp
        self.ine = ine
        self.rfc = rfc
        self.cedula_profesional = cedula_profesional
        self.estado_civil = estado_civil
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono_contacto = telefono_contacto
        self.domicilio = domicilio
        self.tope_horas_extra = tope_horas_extra
        self.foto_base64 = foto_base64
        self.tipo_sangre = tipo_sangre
        self.lugar_nacimiento = lugar_nacimiento
        self.sexo = sexo
        self.calle = calle
        self.manzana = manzana
        self.lote = lote
        self.numero_exterior = numero_exterior
        self.numero_interior = numero_interior
        self.colonia = colonia
        self.codigo_postal = codigo_postal
        self.estado = estado
        self.telefono_domicilio = telefono_domicilio
        self.cuenta_correo = cuenta_correo
        self.salario_diario_integrado = salario_diario_integrado
        self.numero_credito_infonavit = numero_credito_infonavit
        self.tipo_descuento_infonavit = tipo_descuento_infonavit
        self.factor_infonavit = factor_infonavit
        self.fecha_ingreso = fecha_ingreso
        self.turno = turno
        self.tipo_contrato = tipo_contrato
        self.contacto_accidente = contacto_accidente
        self.alergias = alergias
        self.enfermedades_controladas = enfermedades_controladas
        self.edificio = edificio
        self.alcaldia = alcaldia
        self.municipio = municipio
        self.registro_patronal = registro_patronal
        self.cuenta = cuenta
        self.motivo_baja = motivo_baja
        self.id_monedero = id_monedero
