class Empleados:
    def __init__(self, id, nombre,apellido, id_empresa,puesto,
                tipo_empleado,tipo_nomina,sueldo_imss,monedero,nomina,banco,
                numero_cuenta,clabe,alta_empleado = "",baja_empleado="",fecha_registro="",is_blocked=False) -> None:

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
        