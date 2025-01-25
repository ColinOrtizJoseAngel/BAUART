class Monedero:
    def __init__(self, id=None, banco=None, numero_tarjeta=None, id_banco=None, estatus="ACTIVO", id_empleado=None):
        """
        Clase que representa la entidad Monedero.
        
        Args:
            id (int, optional): Identificador único del monedero.
            banco (str, optional): Nombre del banco asociado.
            numero_tarjeta (str, optional): Número de tarjeta asociada al monedero.
            id_banco (int, optional): Identificador del banco.
            estatus (str, optional): Estatus del monedero, por defecto "ACTIVO".
            id_empleado (int, optional): Identificador del empleado asociado, si aplica.
        """
        self.id = id
        self.banco = banco
        self.numero_tarjeta = numero_tarjeta
        self.id_banco = id_banco
        self.estatus = estatus
        self.id_empleado = id_empleado  # Campo opcional para el empleado asociado

    def __str__(self):
        """
        Representación en string del objeto Monedero.
        """
        return (f"Monedero(id={self.id}, banco='{self.banco}', numero_tarjeta='{self.numero_tarjeta}', "
                f"id_banco={self.id_banco}, estatus='{self.estatus}', id_empleado={self.id_empleado})")
