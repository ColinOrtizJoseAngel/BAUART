class ContactosClientes:
    
    def __init__(self, id, id_cliente, nombre, apellido, puesto, telefono, correo, fecha_registro = None, usuario = None, is_blocked=False) -> None:
        self.id = id
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.puesto = puesto
        self.telefono = telefono
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.is_blocked = is_blocked