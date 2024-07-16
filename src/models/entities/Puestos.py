
class Puesto():

    def __init__(self,ent_IdPuesto,ent_IdCategoria,ent_Puesto,ent_SueldoDiario,ent_TipoEmpleado,
                ent_TipoSueldo,ent_SueldoMensual,ent_SueldoIMSS,ent_SueldoMonedero,ent_HoraExtra,
                ent_Sueldo,ent_is_blocked = False ) -> None:
        
            self.ent_IdPuesto = ent_IdPuesto
            self.ent_IdCategoria = ent_IdCategoria
            self.ent_Puesto = ent_Puesto
            self.ent_TipoEmpleado = ent_TipoEmpleado
            self.ent_TipoSueldo = ent_TipoSueldo
            self.ent_Sueldo = ent_Sueldo
            self.ent_SueldoDiario = ent_SueldoDiario
            self.ent_SueldoMensual = ent_SueldoMensual
            self.ent_SueldoIMSS = ent_SueldoIMSS
            self.ent_SueldoMonedero = ent_SueldoMonedero
            self.ent_HoraExtra = ent_HoraExtra
            self.ent_is_blocked = ent_is_blocked
            