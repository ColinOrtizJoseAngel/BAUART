class CuentasEmpresas():

     def __init__(self,id_dato_banco,empresa,banco,numero_cuenta,cable,is_blocked = False) -> None:
        
            self.id_dato_banco = id_dato_banco
            self.empresa = empresa
            self.banco = banco
            self.numero_cuenta = numero_cuenta
            self.cable = cable
            self.is_blocked = is_blocked