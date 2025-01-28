class CuentasProveedor:

    def __init__(self, id, id_proveedor, id_banco, numero_cuenta, clabe,usuario=None, fecha_registro=None, is_blocked=False) -> None:
        
        self.id = id
        self.id_proveedor = id_proveedor
        self.id_banco = id_banco
        self.numero_cuenta = numero_cuenta
        self.clabe = clabe
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked