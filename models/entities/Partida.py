from datetime import datetime

class Partida:
    def __init__(self, id, id_requisicion, descripcion, unidad, cantidad, 
                 fecha_creacion=None, detalles=None, status=None, 
                 precio_unitario=None, total=None):
        self.id = id
        self.id_requisicion = id_requisicion
        self.descripcion = descripcion
        self.unidad = unidad
        self.cantidad = cantidad
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()
        self.detalles = detalles
        self.status = status
        self.precio_unitario = precio_unitario
        self.total = total

    def calcular_total(self):
        """Calcula el total de la partida basado en el precio unitario y la cantidad."""
        if self.precio_unitario is not None and self.cantidad is not None:
            self.total = self.precio_unitario * self.cantidad
        else:
            self.total = None  # Total será None si falta algún dato

    def __repr__(self):
        return (f"<Partida {self.id} - {self.descripcion} - Unidad: {self.unidad} - "
                f"Cantidad: {self.cantidad} - Precio Unitario: {self.precio_unitario} - "
                f"Total: {self.total}>")
