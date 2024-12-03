class Presupuesto:
    def __init__(self, id_presupuesto, id_cliente, id_director, id_empresa, id_proyecto,
                 usuario, estatus_proyecto, presupuesto_cliente, sub_proveedor, 
                 subtotal_cliente_iva, total_cliente_iva, indirecto_cliente_iva, sub_diferencia, 
                 pagado_cliente, porcentaje_pagado, falta_por_cobrar, falta_por_gastar, 
                 is_blocked=False, porcentaje_gastado=0, porcentaje_por_gastar=0):
        self.id_presupuesto = id_presupuesto
        self.id_cliente = id_cliente
        self.id_director = id_director
        self.id_empresa = id_empresa
        self.id_proyecto = id_proyecto
        self.usuario = usuario
        self.estatus_proyecto = estatus_proyecto
        self.presupuesto_cliente = presupuesto_cliente
        self.sub_proveedor = sub_proveedor
        self.subtotal_cliente_iva = subtotal_cliente_iva
        self.total_cliente_iva = total_cliente_iva
        self.indirecto_cliente_iva = indirecto_cliente_iva
        self.sub_diferencia = sub_diferencia
        self.pagado_cliente = pagado_cliente
        self.porcentaje_pagado = porcentaje_pagado
        self.falta_por_cobrar = falta_por_cobrar
        self.falta_por_gastar = falta_por_gastar
        self.is_blocked = is_blocked
        self.porcentaje_gastado = porcentaje_gastado
        self.porcentaje_por_gastar = porcentaje_por_gastar
        
class DetallePresupuesto:
    def __init__(self, id_detalle, id_presupuesto, id_concepto, id_proveedor, 
                 concepto, contrato_firmado, presupuesto_cliente, presupuesto_contratista, 
                 diferencia, is_blocked=False):
        self.id_detalle = id_detalle
        self.id_presupuesto = id_presupuesto
        self.id_concepto = id_concepto
        self.id_proveedor = id_proveedor
        self.concepto = concepto
        self.contrato_firmado = contrato_firmado
        self.presupuesto_cliente = presupuesto_cliente
        self.presupuesto_contratista = presupuesto_contratista
        self.diferencia = diferencia
        self.is_blocked = is_blocked

class PresupuestoBauart:
    def __init__(self, id_presupuesto_bauart, id_detalle, nombre_presupuesto, 
                 total_presupuesto_cliente, total_presupuesto_proveedor, 
                 diferencia_presupuesto, is_blocked=False):
        self.id_presupuesto_bauart = id_presupuesto_bauart
        self.id_detalle = id_detalle
        self.nombre_presupuesto = nombre_presupuesto
        self.total_presupuesto_cliente = total_presupuesto_cliente
        self.total_presupuesto_proveedor = total_presupuesto_proveedor
        self.diferencia_presupuesto = diferencia_presupuesto
        self.is_blocked = is_blocked

class DetalleBauart:
    def __init__(self, id_detalle_bauart, id_presupuesto_bauart, concepto, 
                 presupuesto_cliente, presupuesto_contratista, diferencia, 
                 id_proveedor, is_blocked=False):
        self.id_detalle_bauart = id_detalle_bauart
        self.id_presupuesto_bauart = id_presupuesto_bauart
        self.concepto = concepto
        self.presupuesto_cliente = presupuesto_cliente
        self.presupuesto_contratista = presupuesto_contratista
        self.diferencia = diferencia
        self.id_proveedor = id_proveedor
        self.is_blocked = is_blocked

