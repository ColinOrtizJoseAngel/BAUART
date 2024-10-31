class CuentasClientes:

    def __init__(self, id, id_cliente, id_banco, numero_cuenta, clabe, fecha_registro=None, usuario=None, is_blocked=False) -> None:
        self.id = id
        self.id_cliente = id_cliente
        self.id_banco = id_banco
        self.numero_cuenta = numero_cuenta
        self.clabe = clabe
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked