
class Puesto():

    def __init__(self,id,puesto,sueldo_base,sueldo_tarjeta,
                 horas_extras,categoria,is_blocked = False ) -> None:

        self.id = id
        self.puesto = puesto
        self.sueldo_base = sueldo_base
        self.sueldo_tarjeta = sueldo_tarjeta
        self.horas_extras = horas_extras
        self.categoria = categoria
        self.is_blocked = is_blocked
                
            
            