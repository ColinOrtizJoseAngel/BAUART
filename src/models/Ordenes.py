class Ordenes:

    def __init__(self, id, id_requisicion=None, fecha_hora_entrega=None, direccion_entrega=None, contacto=None, telefono=None, porcentaje_descuento=None):
        """
        Clase para representar una orden de compra.

        :param id: ID único de la orden.
        :param id_requisicion: ID de la requisición asociada (opcional).
        :param fecha_hora_entrega: Fecha y hora programada para la entrega (opcional).
        :param direccion_entrega: Dirección donde se realizará la entrega (opcional).
        :param contacto: Nombre del contacto para la entrega (opcional).
        :param telefono: Teléfono del contacto (opcional).
        :param porcentaje_descuento: Porcentaje de descuento aplicado a la orden (opcional).
        """
        self.id = id
        self.id_requisicion = id_requisicion
        self.fecha_hora_entrega = fecha_hora_entrega
        self.direccion_entrega = direccion_entrega
        self.contacto = contacto
        self.telefono = telefono
        self.porcentaje_descuento = porcentaje_descuento

    def __repr__(self):
        return (f"Ordenes(id={self.id}, id_requisicion={self.id_requisicion}, "
                f"fecha_hora_entrega={self.fecha_hora_entrega}, direccion_entrega={self.direccion_entrega}, "
                f"contacto={self.contacto}, telefono={self.telefono}, "
                f"porcentaje_descuento={self.porcentaje_descuento})")
