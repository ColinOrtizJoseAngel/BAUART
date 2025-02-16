class ProyectoObra:
    def __init__(self, id, id_empresa, id_cliente, tipo_id, fecha_inicio, fecha_contrato,
                 fecha_fin, nombre_proyecto, centro_comercial, pais, estado, municipio, 
                 colonia, calle, numero_exterior, numero_interior, director_proyecto, 
                 lider_proyecto, gerente_proyecto, lider1, lider2, fecha_registro, 
                 usuario_id, is_blocked, cp, hora_entrada, hora_salida, direccion_obra, 
                 latitud, longitud, lider_nombre=None, lider_apellido=None):  # 🔹 Se agregan como opcionales
        self.id = id
        self.id_empresa = id_empresa
        self.id_cliente = id_cliente
        self.tipo_id = tipo_id
        self.fecha_inicio = fecha_inicio
        self.fecha_contrato = fecha_contrato
        self.fecha_fin = fecha_fin
        self.nombre_proyecto = nombre_proyecto
        self.centro_comercial = centro_comercial
        self.pais = pais
        self.estado = estado
        self.municipio = municipio
        self.colonia = colonia
        self.calle = calle
        self.numero_exterior = numero_exterior
        self.numero_interior = numero_interior
        self.director_proyecto = director_proyecto
        self.lider_proyecto = lider_proyecto
        self.gerente_proyecto = gerente_proyecto
        self.lider1 = lider1
        self.lider2 = lider2
        self.fecha_registro = fecha_registro
        self.usuario_id = usuario_id
        self.is_blocked = is_blocked
        self.cp = cp
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.direccion_obra = direccion_obra
        self.latitud = latitud
        self.longitud = longitud
        self.lider_nombre = lider_nombre if lider_nombre else " "  # 🔹 Default "N/A"
        self.lider_apellido = lider_apellido if lider_apellido else " "  # 🔹 Default "N/A"
