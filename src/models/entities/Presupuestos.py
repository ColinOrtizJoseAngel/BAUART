class Presupuesto:
    def __init__(self, id:int, proyecto:str, id_proyecto=None,id_director=0, id_cliente=None, id_empresa=None, 
                 director_obra=None, presupuesto_cliente=0.0, estatus_proyecto="", pagado_cliente=0.0, 
                 porcentaje_pagado_cliente=0.0, gastado_real=0.0, falta_por_cobrar=0.0, 
                 falta_por_gastar=0.0, porcentaje_por_gastar=0.0, subtotal_cliente=0.0, 
                 porcentaje_indirecto=0.0, total_cliente=0.0, subtotal_proveedor=0.0, 
                 subtotal_diferencia=0.0, usuario_id=None, estatus=0, porcentaje_por_cobra=0.0,
                 fecha_inicio=None, fecha_fin=None, direccion_obra=None, porcetaje_gastado_real=0.0, 
                 total_semanas=0, total_porcentaje_indirecto=0.0, total_proveedor=0.0, total_diferencia=0.0):
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
            subtotal_cliente (float): Subtotal del cliente con IVA.
            porcentaje_indirecto (float): Total indirecto del cliente con IVA.
            total_cliente_iva (float): Total del cliente con IVA.
            subtotal_proveedor (float): Subtotal del proveedor.
            subtotal_diferencia (float): Subtotal de diferencia.
            usuario_id (int): Identificador del usuario que crea el presupuesto.
            estatus (int): Estatus del presupuesto.
        """
        self.id = id
        self.proyecto = proyecto
        self.id_proyecto = id_proyecto
        self.id_director = id_director
        self.id_cliente = id_cliente
        self.id_empresa = id_empresa
        self.presupuesto_cliente = presupuesto_cliente
        self.falta_por_cobrar = falta_por_cobrar
        self.porcentaje_por_cobra = porcentaje_por_cobra
        self.fecha_inicio = fecha_inicio
        self.direccion_obra = direccion_obra
        self.pagado_cliente = pagado_cliente
        self.porcentaje_pagado_cliente = porcentaje_pagado_cliente
        self.falta_por_gastar = falta_por_gastar
        self.porcentaje_por_gastar = porcentaje_por_gastar
        self.fecha_fin = fecha_fin
        self.director_obra = director_obra
        self.gastado_real = gastado_real
        self.porcetaje_gastado_real = porcetaje_gastado_real
        self.estatus_proyecto = estatus_proyecto
        self.total_semanas = total_semanas
        self.subtotal_cliente = subtotal_cliente
        self.subtotal_proveedor = subtotal_proveedor
        self.subtotal_diferencia = subtotal_diferencia
        self.porcentaje_indirecto = porcentaje_indirecto
        self.total_porcentaje_indirecto = total_porcentaje_indirecto
        self.total_cliente = total_cliente
        self.total_proveedor = total_proveedor
        self.total_diferencia = total_diferencia
        self.usuario_id = usuario_id
        self.estatus = estatus

    def to_dict(self):
        """
        Serializa los atributos de la instancia en un diccionario.

        Returns:
            dict: Diccionario con los atributos de la instancia.
        """
        return {
            "id": self.id,
            "proyecto": self.proyecto,
            "id_proyecto": self.id_proyecto,
            "id_cliente": self.id_cliente,
            "id_empresa": self.id_empresa,
            "id_director": self.director_obra,
            "presupuesto_cliente": self.presupuesto_cliente,
            "estatus_proyecto": self.estatus_proyecto,
            "pagado_cliente": self.pagado_cliente,
            "porcentaje_pagado_cliente": self.porcentaje_pagado_cliente,
            "gastado_real": self.gastado_real,
            "porcentaje_gastado_real": self.porcetaje_gastado_real,
            "falta_por_cobrar": self.falta_por_cobrar,
            "falta_por_gastar": self.falta_por_gastar,
            "porcentaje_por_gastar": self.porcentaje_por_gastar,
            "subtotal_cliente": self.subtotal_cliente,
            "porcentaje_indirecto": self.porcentaje_indirecto,
            "total_cliente": self.total_cliente,
            "subtotal_proveedor": self.subtotal_proveedor,
            "subtotal_diferencia": self.subtotal_diferencia,
            "usuario_id": self.usuario_id,
            "estatus": self.estatus,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "direccion_obra": self.direccion_obra,
            "total_semanas": self.total_semanas,
            "total_porcentaje_indirecto": self.total_porcentaje_indirecto,
            "total_proveedor": self.total_proveedor,
            "total_diferencia": self.total_diferencia
        }

class DetallePresupuesto:
    def __init__(self, id=0, id_presupuesto=None, id_concepto=None, concepto="", 
                 id_proveedor=None, presupuesto_cliente=0.0, presupuesto_contratista=0.0, 
                 diferencia=0.0, contrato_firmado=False,estatus=0,is_blocked=False,presupuesto_bauart=None):
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
        self.estatus = estatus
        self.presupuesto_bauart = presupuesto_bauart 

    def to_dict(self):
        """
        Serializa los atributos de la instancia en un diccionario.

        Returns:
            dict: Diccionario con los atributos de la instancia.
        """
        return {
            "id": self.id,
            "id_presupuesto": self.id_presupuesto,
            "id_concepto": self.id_concepto,
            "concepto": self.concepto,
            "id_proveedor": self.id_proveedor,
            "presupuesto_cliente": self.presupuesto_cliente,
            "presupuesto_contratista": self.presupuesto_contratista,
            "diferencia": self.diferencia,
            "contrato_firmado": self.contrato_firmado,
            "is_blocked": self.is_blocked,
            "estatus": self.estatus,
            "presupuesto_bauart": self.presupuesto_bauart.to_dict() if self.presupuesto_bauart else []
        }


class PresupuestoBauart:
    def __init__(self, id=0, concepto="", id_detalle=None, nombre_presupuesto="", 
                 total_presupuesto_cliente=0.0, total_presupuesto_proveedor=0.0, 
                 diferencia_presupuesto=0.0,is_blocked = False, estatus=0):
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
        self.estatus = estatus
        self.detalles = [] 

    def agregar_detalle(self, detalle):
        """
        Agrega un detalle al presupuesto.

        Args:
            detalle (DetalleBauart): Instancia de la clase DetalleBauart a añadir.
        """
        if isinstance(detalle, DetalleBauart):
            self.detalles.append(detalle)
            detalle.id_presupuesto_bauart = self.id  # Actualizar la referencia en el detalle
        else:
            raise TypeError("El detalle debe ser una instancia de DetalleBauart.")
    
    def to_dict(self):
        """
        Serializa los atributos de la instancia en un diccionario.

        Returns:
            dict: Diccionario con los atributos de la instancia.
        """
        return {
            "id": self.id,
            "concepto": self.concepto,
            "id_detalle": self.id_detalle,
            "nombre_presupuesto": self.nombre_presupuesto,
            "total_presupuesto_cliente": self.total_presupuesto_cliente,
            "total_presupuesto_proveedor": self.total_presupuesto_proveedor,
            "diferencia_presupuesto": self.diferencia_presupuesto,
            "is_blocked": self.is_blocked,
            "estatus": self.estatus,
            "detalles": [detalle.to_dict() for detalle in self.detalles]
        }

class DetalleBauart:
    def __init__(self, id=0, id_presupuesto_bauart=None, id_concepto=None, concepto="", 
                 id_proveedor=None, presupuesto_cliente=0.0, presupuesto_contratista=0.0, 
                 diferencia=0.0, is_nomina=False,is_blocked =False,estatus=0):
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
        self.estatus = estatus
    
    def to_dict(self):
        """
        Serializa los atributos de la instancia en un diccionario.

        Returns:
            dict: Diccionario con los atributos de la instancia.
        """
        return {
            "id": self.id,
            "id_presupuesto_bauart": self.id_presupuesto_bauart,
            "id_concepto": self.id_concepto,
            "concepto": self.concepto,
            "id_proveedor": self.id_proveedor,
            "presupuesto_cliente": self.presupuesto_cliente,
            "presupuesto_contratista": self.presupuesto_contratista,
            "diferencia": self.diferencia,
            "is_nomina": self.is_nomina,
            "is_blocked": self.is_blocked,
            "estatus": self.estatus
        }
