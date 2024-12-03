class Presupuesto:
    def __init__(self, id=0, proyecto="", id_proyecto=None, id_cliente=None, id_empresa=None, 
                 id_director=None, presupuesto_cliente=0.0, estatus_proyecto="", pagado_cliente=0.0, 
                 porcentaje_pagado=0.0, gastado_real=0.0, porcentaje_gastado=0.0, falta_por_cobrar=0.0, 
                 falta_por_gastar=0.0, porcentaje_por_gastar=0.0, sub_client_iva=0.0, 
                 indirecto_client_iva=0.0, total_cliente_iva=0.0, sub_proveedor=0.0, 
                 sub_diferencia=0.0, usuario_id=None, estatus=1):
        """
        Clase para representar un Presupuesto.

        Args:
            id (int): Identificador del presupuesto.
            proyecto (str): Nombre del proyecto asociado al presupuesto.
            id_proyecto (int): Identificador del proyecto.
            id_cliente (int): Identificador del cliente.
            id_empresa (int): Identificador de la empresa.
            id_director (int): Identificador del director del proyecto.
            presupuesto_cliente (float): Presupuesto asignado por el cliente.
            estatus_proyecto (str): Estatus del proyecto.
            pagado_cliente (float): Cantidad pagada por el cliente.
            porcentaje_pagado (float): Porcentaje del presupuesto pagado por el cliente.
            gastado_real (float): Cantidad realmente gastada.
            porcentaje_gastado (float): Porcentaje del presupuesto gastado.
            falta_por_cobrar (float): Cantidad pendiente de cobro.
            falta_por_gastar (float): Cantidad pendiente de gasto.
            porcentaje_por_gastar (float): Porcentaje pendiente de gasto.
            sub_client_iva (float): Subtotal del cliente con IVA.
            indirecto_client_iva (float): Total indirecto del cliente con IVA.
            total_cliente_iva (float): Total del cliente con IVA.
            sub_proveedor (float): Subtotal del proveedor.
            sub_diferencia (float): Subtotal de diferencia.
            usuario_id (int): Identificador del usuario que crea el presupuesto.
            estatus (int): Estatus del presupuesto.
        """
        self.id = id
        self.proyecto = proyecto
        self.id_proyecto = id_proyecto
        self.id_cliente = id_cliente
        self.id_empresa = id_empresa
        self.id_director = id_director
        self.presupuesto_cliente = presupuesto_cliente
        self.estatus_proyecto = estatus_proyecto
        self.pagado_cliente = pagado_cliente
        self.porcentaje_pagado = porcentaje_pagado
        self.gastado_real = gastado_real
        self.porcentaje_gastado = porcentaje_gastado
        self.falta_por_cobrar = falta_por_cobrar
        self.falta_por_gastar = falta_por_gastar
        self.porcentaje_por_gastar = porcentaje_por_gastar
        self.sub_client_iva = sub_client_iva
        self.indirecto_client_iva = indirecto_client_iva
        self.total_cliente_iva = total_cliente_iva
        self.sub_proveedor = sub_proveedor
        self.sub_diferencia = sub_diferencia
        self.usuario_id = usuario_id
        self.estatus = estatus


class DetallePresupuesto:
    def __init__(self, id=0, id_presupuesto=None, id_concepto=None, concepto="", 
                 id_proveedor=None, presupuesto_cliente=0.0, presupuesto_contratista=0.0, 
                 diferencia=0.0, contrato_firmado=False,is_blocked=False):
        """
        Clase para representar un Detalle de Presupuesto.

        Args:
            id (int): Identificador del detalle de presupuesto.
            id_presupuesto (int): Identificador del presupuesto al que pertenece el detalle.
            id_concepto (int): Identificador del concepto asociado.
            concepto (str): Descripción del concepto.
            id_proveedor (int): Identificador del proveedor asociado al concepto.
            presupuesto_cliente (float): Presupuesto asignado por el cliente para este concepto.
            presupuesto_contratista (float): Presupuesto asignado al contratista para este concepto.
            diferencia (float): Diferencia entre el presupuesto del cliente y del contratista.
            contrato_firmado (bool): Indica si el contrato para este detalle está firmado.
        """
        self.id = id
        self.id_presupuesto = id_presupuesto
        self.id_concepto = id_concepto
        self.concepto = concepto
        self.id_proveedor = id_proveedor
        self.presupuesto_cliente = presupuesto_cliente
        self.presupuesto_contratista = presupuesto_contratista
        self.diferencia = diferencia
        self.contrato_firmado = contrato_firmado
        self.is_blocked = is_blocked



class PresupuestoBauart:
    def __init__(self, id=0, concepto="", id_detalle=None, nombre_presupuesto="", 
                 total_presupuesto_cliente=0.0, total_presupuesto_proveedor=0.0, 
                 diferencia_presupuesto=0.0,is_blocked = False):
        """
        Clase para representar un Presupuesto Bauart.

        Args:
            id (int): Identificador del presupuesto Bauart.
            concepto (str): Concepto asociado al presupuesto Bauart.
            id_detalle (int): Identificador del detalle de presupuesto al que pertenece.
            nombre_presupuesto (str): Nombre del presupuesto Bauart.
            total_presupuesto_cliente (float): Total del presupuesto del cliente.
            total_presupuesto_proveedor (float): Total del presupuesto del proveedor.
            diferencia_presupuesto (float): Diferencia entre el presupuesto del cliente y del proveedor.
        """
        self.id = id
        self.concepto = concepto
        self.id_detalle = id_detalle
        self.nombre_presupuesto = nombre_presupuesto
        self.total_presupuesto_cliente = total_presupuesto_cliente
        self.total_presupuesto_proveedor = total_presupuesto_proveedor
        self.diferencia_presupuesto = diferencia_presupuesto
        self.is_blocked = is_blocked

class DetalleBauart:
    def __init__(self, id=0, id_presupuesto_bauart=None, id_concepto=None, concepto="", 
                 id_proveedor=None, presupuesto_cliente=0.0, presupuesto_contratista=0.0, 
                 diferencia=0.0, is_nomina=False,is_blocked =False):
        """
        Clase para representar un Detalle de Presupuesto Bauart.

        Args:
            id (int): Identificador del detalle Bauart.
            id_presupuesto_bauart (int): Identificador del presupuesto Bauart al que pertenece este detalle.
            id_concepto (int): Identificador del concepto asociado al detalle Bauart.
            concepto (str): Descripción del concepto.
            id_proveedor (int): Identificador del proveedor asociado al concepto.
            presupuesto_cliente (float): Presupuesto asignado por el cliente para este detalle.
            presupuesto_contratista (float): Presupuesto asignado al contratista para este detalle.
            diferencia (float): Diferencia entre el presupuesto del cliente y del contratista.
            is_nomina (bool): Indica si el concepto es parte de una nómina.
        """
        self.id = id
        self.id_presupuesto_bauart = id_presupuesto_bauart
        self.id_concepto = id_concepto
        self.concepto = concepto
        self.id_proveedor = id_proveedor
        self.presupuesto_cliente = presupuesto_cliente
        self.presupuesto_contratista = presupuesto_contratista
        self.diferencia = diferencia
        self.is_nomina = is_nomina
        self.is_blocked = is_blocked
        
        
