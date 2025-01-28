
class Requisicion:
    
    def __init__(self, id, nombre_proyecto, concepto, fecha_solicitud, fecha_recibido, status):
        self.id = id
        self.nombre_proyecto = nombre_proyecto
        self.concepto = concepto
        self.fecha_solicitud = fecha_solicitud
        self.fecha_recibido = fecha_recibido  # Updated field
        self.status = status