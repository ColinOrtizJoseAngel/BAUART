class Banco():

    def __init__(self,id_banco,banco,is_blocked = False) -> None:
        
            self.id_banco = id_banco
            self.banco = banco
            self.is_blocked = is_blocked