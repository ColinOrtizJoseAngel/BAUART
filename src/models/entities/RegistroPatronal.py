class RegistroPatronal:

    def __init__(self, id_registro, id_empresa, numero_registro_patronal, estado, fecha_registro=None, usuario=None, is_blocked=False) -> None:
        self.id_registro = id_registro
        self.id_empresa = id_empresa
        self.numero_registro_patronal = numero_registro_patronal
        self.estado = estado
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked