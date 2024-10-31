class ModelProyectoObra:
    @classmethod
    def crear_ProyectoObra(cls, db, proyectoObra):
        try:
            cursor = db.cursor()
            
            query = """
                INSERT INTO PROYECTOS (
                    ID_EMPRESA, ID_CLIENTE, FECHA_INICIO, FECHA_CONTRATO, FECHA_FIN,
                    NOMBRE_PROYECTO, CENTRO_COMERCIAL, PAIS, ESTADO, MUNICIPIO, COLONIA,
                    CALLE, NUMERO_EXTERIOR, NUMERO_INTERIOR, DIRECTOR_PROYECTO, LIDER_PROYECTO,
                    GERENTE_PROYECTO, LIDER1, LIDER2, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED, TIPO_ID
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);
            """
            cursor.execute(query, (
                proyectoObra.id_empresa,
                proyectoObra.id_cliente,
                proyectoObra.fecha_inicio,
                proyectoObra.fecha_contrato,
                proyectoObra.fecha_fin,
                proyectoObra.nombre_proyecto,
                proyectoObra.centro_comercial,
                proyectoObra.pais,
                proyectoObra.estado,
                proyectoObra.municipio,
                proyectoObra.colonia,
                proyectoObra.calle,
                proyectoObra.numero_exterior,
                proyectoObra.numero_interior,
                proyectoObra.director_proyecto,
                proyectoObra.lider_proyecto,
                proyectoObra.gerente_proyecto,
                proyectoObra.lider1,
                proyectoObra.lider2,
                proyectoObra.fecha_registro,
                proyectoObra.usuario_id,
                proyectoObra.is_blocked,
                proyectoObra.tipo_id
            ))
          
            db.commit()
    
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
