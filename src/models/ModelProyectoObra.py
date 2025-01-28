from .entities.ProyectoObra import ProyectoObra
from datetime import datetime, timedelta,date

class ModelProyectoObra:
    
    def format_time(value):
        try:
            return datetime.strptime(value[:8], '%H:%M:%S').strftime('%H:%M')
        except ValueError:
            return None  # Manejo de errores si el formato no es válido
        
    
    @classmethod 
    def crear_ProyectoObra(cls, db, proyecto):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO PROYECTOS (
                        ID_CLIENTE, ID_EMPRESA, NOMBRE_PROYECTO, TIPO_ID, FECHA_INICIO, FECHA_CONTRATO, FECHA_FIN, 
                        PAIS, ESTADO, MUNICIPIO, COLONIA, CALLE, NUMERO_EXTERIOR, NUMERO_INTERIOR,
                        CENTRO_COMERCIAL, DIRECTOR_PROYECTO, LIDER_PROYECTO, GERENTE_PROYECTO, LIDER1, LIDER2,
                        CP, HORA_ENTRADA, HORA_SALIDA, LONGITUD, LATITUD, DIRECCION_OBRA, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED
                    ) VALUES (?, ?, ?, ?, ?, ?,GETDATE(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, GETDATE(), ?, ?);
                """
                cursor.execute(query, (
                    proyecto.id_cliente, proyecto.id_empresa, proyecto.nombre_proyecto, proyecto.tipo_id, proyecto.fecha_inicio, proyecto.fecha_fin,
                    proyecto.pais, proyecto.estado, proyecto.municipio, proyecto.colonia, proyecto.calle, proyecto.numero_exterior, proyecto.numero_interior, 
                    proyecto.centro_comercial, proyecto.director_proyecto, proyecto.lider_proyecto, proyecto.gerente_proyecto, proyecto.lider1, 
                    proyecto.lider2, proyecto.cp, proyecto.hora_entrada, proyecto.hora_salida, proyecto.longitud, proyecto.latitud, proyecto.direcion_obra, 
                    proyecto.usuario_id, proyecto.is_blocked
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_proyectos(cls, db):
        try:
            with db.cursor() as cursor:
                query = """

                SELECT 
                        P.[ID],
                        P.[ID_EMPRESA],
                        P.[ID_CLIENTE],
                        P.[TIPO_ID],
                        P.[FECHA_INICIO],
                        P.[FECHA_CONTRATO],
                        P.[FECHA_FIN],
                        P.[NOMBRE_PROYECTO],
                        P.[CENTRO_COMERCIAL],
                        P.[PAIS],
                        P.[ESTADO],
                        P.[MUNICIPIO],
                        P.[COLONIA],
                        P.[CALLE],
                        P.[NUMERO_EXTERIOR],
                        P.[NUMERO_INTERIOR],
                        P.[DIRECTOR_PROYECTO],
                        P.[LIDER_PROYECTO],
                        P.[GERENTE_PROYECTO],
                        P.[LIDER1],
                        P.[LIDER2],
                        P.[FECHA_REGISTRO],
                        P.[USUARIO_ID],
                        P.[IS_BLOCKED],
                        P.[CP],
                        C.[RAZON_SOCIAL],
                        P.[HORA_ENTRADA],
                        P.[HORA_SALIDA],
                        P.[LONGITUD],
                        P.[LATITUD],
                        P.[DIRECCION_OBRA]
                    FROM 
                        [PROYECTOS] P
                    INNER JOIN 
                        [CLIENTES] C ON C.[ID] = P.[ID_CLIENTE];

                """
                cursor.execute(query)
                rows = cursor.fetchall()
                proyectos = []
            for row in rows:
                proyectos.append(ProyectoObra(
                    id=row[0], 
                    id_empresa=row[1], 
                    id_cliente=row[25],
                    tipo_id=row[3],  
                    fecha_inicio=row[4],
                    fecha_contrato=[5], 
                    fecha_fin=row[6],
                    nombre_proyecto=row[7], 
                    centro_comercial=row[8],
                    pais=row[9], estado=row[10], municipio=row[11],
                    colonia=row[12], calle=row[13], 
                    numero_exterior=row[14], numero_interior=row[15], 
                    director_proyecto=row[16], lider_proyecto=row[17], 
                    gerente_proyecto=row[18], lider1=row[19], 
                    lider2=row[20],
                    fecha_registro=row[21], 
                    usuario_id=row[22], 
                    is_blocked=row[23],
                    cp=row[24],
                    hora_entrada=row[25],
                    hora_salida=row[26],
                    longitud=row[27],
                    latitud=row[28],
                    direcion_obra=row[29]
                    

                ))
            return proyectos
        except Exception as ex:
            raise Exception(ex)   


    
    @classmethod
    def buscar_proyectos(cls, db):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM PROYECTOS"
                cursor.execute(query)
                rows = cursor.fetchall()
                proyectos = []
            for row in rows:
                proyectos.append(ProyectoObra(
                    id=row[0],
                    id_empresa=row[1],
                    id_cliente=row[2], 
                    tipo_id=row[3],
                    fecha_inicio=[4],
                    fecha_contrato=[5], 
                    fecha_fin=row[6],
                    nombre_proyecto=row[7], 
                    centro_comercial=row[8],
                    pais=row[9],
                    estado=row[10], 
                    municipio=row[11],
                    colonia=row[12], 
                    calle=row[13], 
                    numero_exterior=row[14], 
                    numero_interior=row[15], 
                    director_proyecto=row[16], 
                    lider_proyecto=row[17], 
                    gerente_proyecto=row[18],
                    lider1=row[19], 
                    lider2=row[20],
                    fecha_registro=row[21], 
                    usuario_id=row[22],
                    is_blocked=row[23],
                    cp=row[24],
                    hora_entrada=row[25],
                    hora_salida=row[26],
                    direcion_obra=row[27],
                    longitud=row[28],
                    latitud=row[29]
                    
                    
                ))
            return proyectos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_proyectos_not_block(cls, db):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM PROYECTOS WHERE is_blocked = 0"
                cursor.execute(query)
                rows = cursor.fetchall()
                proyectos = []
            for row in rows:
                proyectos.append(ProyectoObra(
                   id=row[0], 
                    id_empresa=row[1], 
                    id_cliente=row[2],
                    tipo_id=row[3],  
                    fecha_inicio=row[4],
                    fecha_contrato=[5], 
                    fecha_fin=row[6],
                    nombre_proyecto=row[7], 
                    centro_comercial=row[8],
                    pais=row[9], estado=row[10], municipio=row[11],
                    colonia=row[12], calle=row[13], 
                    numero_exterior=row[14], numero_interior=row[15], 
                    director_proyecto=row[16], lider_proyecto=row[17], 
                    gerente_proyecto=row[18], lider1=row[19], 
                    lider2=row[20],
                    fecha_registro=row[21], 
                    usuario_id=row[22], is_blocked=row[23],
                    cp=row[24],
                    hora_entrada=row[25],
                    hora_salida=row[26],
                    direcion_obra=row[27],
                    longitud=row[28],
                    latitud=row[29]
                ))
            return proyectos
        except Exception as ex:
            raise Exception(ex)    
        

    @classmethod
    def get_proyecto_by_id(cls, db, id):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM PROYECTOS WHERE ID = ?"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    return ProyectoObra(
                    id=row[0], 
                    id_empresa=row[1], 
                    id_cliente=row[2],
                    tipo_id=row[3],  
                    fecha_inicio=row[4],
                    fecha_contrato=[5], 
                    fecha_fin=row[6],
                    nombre_proyecto=row[7], 
                    centro_comercial=row[8],
                    pais=row[9], estado=row[10], municipio=row[11],
                    colonia=row[12], calle=row[13], 
                    numero_exterior=row[14], numero_interior=row[15], 
                    director_proyecto=row[16], lider_proyecto=row[17], 
                    gerente_proyecto=row[18], lider1=row[19], 
                    lider2=row[20],
                    fecha_registro=row[21], 
                    usuario_id=row[22], is_blocked=row[23],
                    cp=row[24],
                    hora_entrada=cls.format_time(row[25]),
                    hora_salida=cls.format_time(row[26]),
                    direcion_obra=row[27],
                    longitud=row[28],
                    latitud=row[29]
                )
                return None
        except Exception as ex:
            raise Exception(ex)    


    @classmethod
    def get_proyecto_last_by_id(cls, db):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM PROYECTOS ORDER BY ID DESC LIMIT"
                cursor.execute(query)
                row = cursor.fetchone()
                if row:
                    return ProyectoObra(
                        id=row[0], id_cliente=row[1], id_empresa=row[2], nombre_proyecto=row[3], tipo_id=row[4], fecha_inicio=row[5], fecha_fin=row[6], 
                        pais=row[7], estado=row[8], municipio=row[9], colonia=row[10], calle=row[11], numero_exterior=row[12], numero_interior=row[13], 
                        cp=row[14], centro_comercial=row[15], director_proyecto=row[16], lider_proyecto=row[17], gerente_proyecto=row[18], lider1=row[19], 
                        lider2=row[20], fecha_registro=row[21], usuario_id=row[22], is_blocked=row[23]
                    )
                return None
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def update_proyecto(cls, db, proyecto):
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE PROYECTOS SET
                        ID_CLIENTE = ?, ID_EMPRESA = ?, NOMBRE_PROYECTO = ?, TIPO_ID = ?, FECHA_INICIO = ?, FECHA_FIN = ?,
                        PAIS = ?, ESTADO = ?, MUNICIPIO = ?, COLONIA = ?, CALLE = ?, NUMERO_EXTERIOR = ?, NUMERO_INTERIOR = ?, CP = ?,
                        CENTRO_COMERCIAL = ?, DIRECTOR_PROYECTO = ?, LIDER_PROYECTO = ?, GERENTE_PROYECTO = ?, LIDER1 = ?, LIDER2 = ?,
                        FECHA_REGISTRO = ?, USUARIO_ID = ?, IS_BLOCKED = ?
                    WHERE ID = ?
                """
                cursor.execute(query, (
                    proyecto.id_cliente, proyecto.id_empresa, proyecto.nombre_proyecto, proyecto.tipo_id, proyecto.fecha_inicio, proyecto.fecha_fin,
                    proyecto.pais, proyecto.estado, proyecto.municipio, proyecto.colonia, proyecto.calle, proyecto.numero_exterior, proyecto.numero_interior,
                    proyecto.cp, proyecto.centro_comercial, proyecto.director_proyecto, proyecto.lider_proyecto, proyecto.gerente_proyecto, proyecto.lider1, 
                    proyecto.lider2, proyecto.fecha_registro, proyecto.usuario_id, proyecto.is_blocked, proyecto.id
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def change_status(cls, db, id, status):
        try:
            with db.cursor() as cursor:
                query = "UPDATE PROYECTOS SET IS_BLOCKED = ? WHERE ID = ?"
                cursor.execute(query, (status, id))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def filter_proyecto(cls, db, proyecto, id_cliente, estado):
        try:
            with db.cursor() as cursor:
                query = """
                        SELECT 
                            P.[ID],
                            P.[ID_EMPRESA],
                            P.[ID_CLIENTE],
                            P.[TIPO_ID],
                            P.[FECHA_INICIO],
                            P.[FECHA_CONTRATO],
                            P.[FECHA_FIN],
                            P.[NOMBRE_PROYECTO],
                            P.[CENTRO_COMERCIAL],
                            P.[PAIS],
                            P.[ESTADO],
                            P.[MUNICIPIO],
                            P.[COLONIA],
                            P.[CALLE],
                            P.[NUMERO_EXTERIOR],
                            P.[NUMERO_INTERIOR],
                            P.[DIRECTOR_PROYECTO],
                            P.[LIDER_PROYECTO],
                            P.[GERENTE_PROYECTO],
                            P.[LIDER1],
                            P.[LIDER2],
                            P.[FECHA_REGISTRO],
                            P.[USUARIO_ID],
                            P.[IS_BLOCKED],
                            P.[CP],
                            C.[RAZON_SOCIAL]
                        FROM 
                            [PROYECTOS] P
                        INNER JOIN 
                            [CLIENTES] C ON C.[ID] = P.[ID_CLIENTE]
                        WHERE 1=1
                """
                params = []
                
                # Condiciones dinámicas
                if proyecto:
                    query += " AND P.[NOMBRE_PROYECTO] LIKE ?"
                    params.append(f'%{proyecto}%')
                
                if id_cliente:
                    query += " AND P.[ID_CLIENTE] = ?"
                    params.append(id_cliente)
                
                if estado:
                    if estado == 'activo':
                        query += " AND P.[IS_BLOCKED] = 0"
                    elif estado == 'bloqueado':
                        query += " AND P.[IS_BLOCKED] = 1"
                
                # Ejecutar consulta
                cursor.execute(query, params)
                rows = cursor.fetchall()

                # Mapeo de resultados a objetos
                proyectos = []
                    
                for row in rows:
                        proyectos.append(ProyectoObra(
                            id=row[0], 
                        id_empresa=row[1], 
                        id_cliente=row[25],
                        tipo_id=row[3],  
                        fecha_inicio=row[4],
                        fecha_contrato=[5], 
                        fecha_fin=row[6],
                        nombre_proyecto=row[7], 
                        centro_comercial=row[8],
                        pais=row[9], estado=row[10], municipio=row[11],
                        colonia=row[12], calle=row[13], 
                        numero_exterior=row[14], numero_interior=row[15], 
                        director_proyecto=row[16], lider_proyecto=row[17], 
                        gerente_proyecto=row[18], lider1=row[19], 
                        lider2=row[20],
                        fecha_registro=row[21], 
                        usuario_id=row[22], is_blocked=row[23],
                        cp=row[24]
                        ))
                    
                return proyectos
                
        except Exception as ex:
            raise Exception(f"Error al filtrar proyectos: {ex}")
