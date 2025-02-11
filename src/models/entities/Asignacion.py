class Asignacion:
    def __init__(self, id_empleado=None, id_proyecto=None, sueldo_base=None, sueldo_imss=None, monedero=None, 
                 fecha_asignacion=None, fecha_fin=None, id_detalle=None, hora_entrada_p=None, hora_salida_p=None):
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto
        self.sueldo_base = sueldo_base
        self.sueldo_imss = sueldo_imss
        self.monedero = monedero
        self.fecha_asignacion = fecha_asignacion
        self.fecha_fin = fecha_fin
        self.id_detalle = id_detalle
        self.hora_entrada_p = hora_entrada_p
        self.hora_salida_p = hora_salida_p