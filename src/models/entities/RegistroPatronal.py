class ResgistroPatronal():

    def __init__(self,id_registro,registro_patronal,empresa,estado,is_blocked = False) -> None:
        
            self.id_registro = id_registro
            self.registro_patronal = registro_patronal
            self.empresa = empresa
            self.estado = estado
            self.is_blocked = is_blocked