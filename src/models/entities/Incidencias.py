class Incidencia:
    def __init__(self, idIncidencia, idEmpleado, tipoIncidencia, fechaInicial, 
                 fechaFinal=None, diasSolicitados=0, comentarios=None, fechaRegistro=None, 
                 esIncidencia=False):
        """
        Clase para representar una incidencia.
        
        Args:
            idIncidencia (int): Identificador único de la incidencia.
            idEmpleado (int): Identificador del empleado asociado a la incidencia.
            tipoIncidencia (str): Tipo de incidencia (Ej: A, F, I, etc.).
            fechaInicial (date): Fecha inicial de la incidencia.
            fechaFinal (date, optional): Fecha final de la incidencia. Default: None.
            diasSolicitados (int, optional): Número de días solicitados. Default: 0.
            comentarios (str, optional): Comentarios adicionales sobre la incidencia. Default: None.
            fechaRegistro (datetime, optional): Fecha en la que se registró la incidencia. Default: None.
            esIncidencia (bool, optional): Indica si el registro es una incidencia o no. Default: False.
        """
        self.idIncidencia = idIncidencia
        self.idEmpleado = idEmpleado
        self.tipoIncidencia = tipoIncidencia
        self.fechaInicial = fechaInicial
        self.fechaFinal = fechaFinal
        self.diasSolicitados = diasSolicitados
        self.comentarios = comentarios
        self.fechaRegistro = fechaRegistro
        self.esIncidencia = esIncidencia  # Nuevo campo booleano
