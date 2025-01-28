class Categoria():

    def __init__(self,idCategoria,categoria,_is_blocked = False) -> None:
        
            self.idCategoria = idCategoria
            self.categoria = categoria
            self._is_blocked = _is_blocked