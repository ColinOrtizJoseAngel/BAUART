class ProyectoObra:
    def __init__(self, id, id_empresa, id_cliente, fecha_inicio, fecha_contrato, fecha_fin, nombre_proyecto, centro_comercial, 
                 pais, estado, municipio, colonia, calle, numero_exterior, numero_interior,
                 director_proyecto, lider_proyecto, gerente_proyecto, lider1, lider2, tipo_id,
                 cp, fecha_registro=None, usuario_id=None, is_blocked=False, hora_entrada=None, hora_salida=None,
                 direccion_obra=None, latitud=None, longitud=None) -> None:

        self.id = id
        self.id_empresa = id_empresa
        self.id_cliente = id_cliente
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
        self.cp = cp
        self.fecha_registro = fecha_registro
        self.usuario_id = usuario_id
        self.is_blocked = is_blocked
        self.tipo_id = tipo_id
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.direccion_obra = direccion_obra
        self.latitud = latitud
        self.longitud = longitud
