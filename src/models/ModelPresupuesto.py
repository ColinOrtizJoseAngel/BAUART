from .entities.Presupuestos import Presupuesto,DetallePresupuesto,PresupuestoBauart,DetalleBauart
from models.ModelProyectoObra import ModelProyectoObra

      


class ModelPresupuesto:
    
    @staticmethod
    def formatear_a_pesos(valor):
        """
        Da formato de pesos mexicanos a un número.

        :param valor: float o int, Valor numérico a formatear
        :return: str, Valor formateado como moneda en pesos (e.g., "$1,234.56")
        """
        try:
            return f"${valor:,.2f}"
        except (ValueError, TypeError):
            return "$0.00"
    
    @staticmethod
    def vierificar_diferecnia(valor):
        """
        Verifica si la diferencia del presupuesto es positiva o negativa

        :param valor: valor float
        :return: True o Flase
        """
        try:
            if valor < 0:
                return True
            else:
                False
        except (ValueError, TypeError):
            return None
    
    
    @classmethod
    def crear_presupuesto(cls, db, presupuesto):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO Presupuestos (
                        id_cliente, 
                        id_director, 
                        id_empresa, 
                        proyecto, 
                        id_proyecto, 
                        usuario, 
                        estatus_proyecto, 
                        presupuesto_cliente, 
                        sub_proveedor, 
                        subtotal_cliente_iva, 
                        total_cliente_iva, 
                        indirecto_cliente_iva, 
                        sub_diferencia, 
                        pagado_cliente, 
                        porcentaje_pagado, 
                        falta_por_cobrar, 
                        falta_por_gastar, 
                        gastado_real, 
                        porcentaje_gastado, 
                        porcentaje_por_gastar, 
                        fecha_inicio, 
                        direccion_obra, 
                        fecha_fin, 
                        total_semanas, 
                        total_contratista, 
                        total_diferencia, 
                        is_blocked, 
                        estatus,
                        director
                    ) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);
                """
                cursor.execute(query, (
                    presupuesto.id_cliente,
                    presupuesto.id_director,
                    presupuesto.id_empresa,
                    presupuesto.proyecto,
                    presupuesto.id_proyecto,
                    presupuesto.usuario_id,
                    presupuesto.estatus_proyecto,
                    presupuesto.presupuesto_cliente,
                    presupuesto.subtotal_proveedor,
                    presupuesto.subtotal_cliente,
                    presupuesto.total_cliente,
                    presupuesto.porcentaje_indirecto,
                    presupuesto.subtotal_diferencia,
                    presupuesto.pagado_cliente,
                    presupuesto.porcentaje_pagado_cliente,
                    presupuesto.falta_por_cobrar,
                    presupuesto.falta_por_gastar,
                    presupuesto.gastado_real,
                    presupuesto.porcetaje_gastado_real,
                    presupuesto.porcentaje_por_gastar,
                    presupuesto.fecha_inicio,
                    presupuesto.direccion_obra,
                    presupuesto.fecha_fin,
                    presupuesto.total_semanas,
                    presupuesto.total_proveedor,
                    presupuesto.total_diferencia,
                    0,  # is_blocked, se establece como 0 por defecto
                    presupuesto.estatus,
                    presupuesto.director_obra
                ))

                # Recuperar el último ID insertado
                cursor.execute("SELECT TOP (1) [id_presupuesto] FROM [Presupuestos] ORDER BY [id_presupuesto] DESC;")
                last_id = cursor.fetchone()[0]

                db.commit()
                return int(last_id)  # Asegurarse de devolver el ID como entero
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al crear el presupuesto: {ex}\nQuery: {query}\nDatos: {presupuesto}")

    
    @classmethod
    def agregar_detalle_presupuesto(cls, db, detalle):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO DetallesPresupuesto (
                        id_presupuesto, id_concepto, id_proveedor, concepto, contrato_firmado, presupuesto_cliente, 
                        presupuesto_contratista, diferencia, is_blocked
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                """
                cursor.execute(query, (
                    detalle.id_presupuesto, detalle.id_concepto, detalle.id_proveedor, detalle.concepto,
                    detalle.contrato_firmado, detalle.presupuesto_cliente, detalle.presupuesto_contratista,
                    detalle.diferencia, detalle.is_blocked
                ))
                
                 # Recuperar el último ID insertado
                cursor.execute("SELECT TOP (1) [id_detalle] FROM DetallesPresupuesto ORDER BY [id_detalle] DESC;")
                last_id = cursor.fetchone()[0]
                
                db.commit()
                return int(last_id)
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al agregar el detalle del presupuesto: {ex}")

    @classmethod
    def agregar_presupuesto_bauart(cls, db, presupuesto_bauart):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO PresupuestosBauart (
                        id_detalle, nombre_presupuesto, total_presupuesto_cliente, total_presupuesto_proveedor, 
                        diferencia_presupuesto, is_blocked, estatus, id_presupuesto
                    ) OUTPUT INSERTED.id_presupuesto_bauart
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                """
                cursor.execute(query, (
                    presupuesto_bauart.id_detalle, presupuesto_bauart.nombre_presupuesto,
                    presupuesto_bauart.total_presupuesto_cliente, presupuesto_bauart.total_presupuesto_proveedor,
                    presupuesto_bauart.diferencia_presupuesto, presupuesto_bauart.is_blocked,
                    presupuesto_bauart.estatus, presupuesto_bauart.id_presupuesto
                ))
                
                # Obtener el último ID insertado
                last_id = cursor.fetchone()[0]
                
                db.commit()
                return int(last_id)
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al agregar el presupuesto Bauart: {ex}")

    @classmethod
    def agregar_detalle_bauart(cls, db, detalle_bauart):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO DetallesBauart (
                        id_presupuesto_bauart, id_concepto,concepto, presupuesto_cliente, presupuesto_contratista, diferencia, 
                        id_proveedor, is_blocked,is_nomina,estatus
                    ) VALUES (?, ?, ?,?, ?, ?, ?, ?,?,?);
                """
                cursor.execute(query, (
                    detalle_bauart.id_presupuesto_bauart,detalle_bauart.id_concepto ,detalle_bauart.concepto, detalle_bauart.presupuesto_cliente,
                    detalle_bauart.presupuesto_contratista, detalle_bauart.diferencia, detalle_bauart.id_proveedor,
                    detalle_bauart.is_blocked,detalle_bauart.is_nomina,detalle_bauart.estatus
                ))
                 # Recuperar el último ID insertado
                cursor.execute("SELECT TOP (1) [id_detalle_bauart] FROM DetallesBauart ORDER BY [id_detalle_bauart] DESC;")
                last_id = cursor.fetchone()[0]
                
                db.commit()
                return int(last_id)
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al agregar el detalle Bauart: {ex}")



    @classmethod
    def obtener_presupuesto_completo(cls, db, id_presupuesto):
        """
        Obtener un presupuesto completo por su ID, incluyendo detalles y presupuestos Bauart.
        """
        try:
            # Obtener la información general del presupuesto
            presupuesto_general = cls.obtener_presupuesto_por_id(db, id_presupuesto)
            # Obtener los detalles del presupuesto
            detalles_presupuesto = cls.obtener_detalle_presupuesto_por_id(db, id_presupuesto)
            
            presupuesto_general['total_partidas'] = len(detalles_presupuesto)

            # Obtener presupuestos Bauart asociados a los detalles del presupuesto
            #presupuestos_bauart = cls.obtener_presupuesto_bauart_por_detalle(db, detalles_presupuesto)

            # Obtener los detalles de los presupuestos Bauart
            #detalles_bauart = cls.obtener_detalle_de_presupuesto_bauart(db, presupuestos_bauart)

         
            for i in  detalles_presupuesto:
                
                presupuesto_bauart = cls.obtener_presupuesto_bauart_por_detalle(db, i.id)
                
                if presupuesto_bauart:
                
                    detalles_bauart = cls.obtener_detalle_de_presupuesto_bauart(db, presupuesto_bauart.id)
                    presupuesto_bauart.detalles = detalles_bauart
                
                i.presupuesto_bauart = presupuesto_bauart
                                
                # Si es proveedor es 0 se trata de un proveedor Bauart
                
                """
                  if i.id_proveedor == 0:
                    for j in presupuestos_bauart:
                        if j.id_detalle == i.id:
                            for e in detalles_bauart:
                                if e.id_presupuesto_bauart == j.id:
                                    j.agregar_detalle(e)
                    i.presupuesto_bauart = j
                    print(i.presupuesto_bauart)     
                """
               
                  
                presupuesto_general["detalle_presupuesto"].append(i.to_dict())
                                
            return presupuesto_general
        except Exception as ex:
            raise Exception(f"Error al obtener el presupuesto completo: {ex}")



    @classmethod
    def obtener_presupuesto_por_id(cls, db, id_presupuesto):
        """
            Obtener un presupuesto por su ID.
        """
        try:
            with db.cursor() as cursor:
                query = """
                     
                    SELECT 
                        p.id_presupuesto,
                        p.proyecto,
                        p.id_proyecto,
                        p.id_cliente, 
                        c.RAZON_SOCIAL AS cliente,
                        p.id_empresa,
                        e.RAZON_SOCIAL AS empresa,
                        p.id_director,
                        p.presupuesto_cliente,
                        p.estatus_proyecto,
                        p.pagado_cliente,
                        p.porcentaje_pagado,
                        p.gastado_real,
                        p.porcentaje_gastado,
                        p.falta_por_cobrar,
                        p.falta_por_gastar,
                        p.subtotal_cliente_iva,
                        p.indirecto_cliente_iva,
                        p.total_cliente_iva,
                        p.sub_proveedor,
                        p.sub_diferencia,
                        p.usuario,
                        u.NOMBRE_USUARIO AS nombre_usuario,
                        p.estatus,
						p.direccion_obra,
						p.fecha_inicio,
						p.fecha_fin,
						p.total_semanas,
                        p.porcentaje_por_cobra,
                        p.porcentaje_por_gastar,
                        p.total_contratista,
                        p.total_diferencia,
                        p.porcentaje_indirecto,
                        p.estatus_contratos,
						p.estatus_presupuesto
                    FROM Presupuestos AS p
                    INNER JOIN CLIENTES AS c ON c.ID = p.id_cliente
                    INNER JOIN EMPRESAS AS e ON e.ID = p.id_empresa
                    INNER JOIN USUARIOS AS u ON u.ID = p.usuario
                    WHERE  p.id_presupuesto = ?
                    ;
                """

                cursor.execute(query, (id_presupuesto,))
                row = cursor.fetchone()
                
                presupuesto = {
                        "id_presupuesto": row[0],
                        "proyecto": row[1],
                        "id_proyecto": row[2],
                        "id_cliente": row[3],
                        "cliente": row[4],
                        "id_empresa": row[5],
                        "empresa": row[6],
                        "id_director": row[7],
                        "presupuesto_cliente": cls.formatear_a_pesos(row[8]),
                        "estatus_proyecto":cls.formatear_a_pesos(row[9]),
                        "pagado_cliente":cls.formatear_a_pesos(row[10]),
                        "porcentaje_pagado":row[11],
                        "gastado_real": cls.formatear_a_pesos(row[12]),
                        "porcentaje_gastado": row[13],
                        "falta_por_cobrar": cls.formatear_a_pesos(row[14]),
                        "falta_por_gastar": cls.formatear_a_pesos(row[15]),
                        "subtotal_cliente_iva": cls.formatear_a_pesos(row[16]),
                        "indirecto_cliente_iva": cls.formatear_a_pesos(row[17]),
                        "total_cliente_iva": cls.formatear_a_pesos(row[18]),
                        "sub_proveedor": cls.formatear_a_pesos(row[19]),
                        "sub_diferencia": cls.formatear_a_pesos(row[20]),
                        "diferencia_es_negativa" : cls.vierificar_diferecnia(row[20]),
                        "usuario": row[21],
                        "nombre_usuario": row[22],
                        "estatus": row[23],
                        "direcion_obra" : row[24],
                        "fecha_inicio": row[25],
                        "fecha_fin": row[26],
                        "total_semanas": row[27],
                        "porcentaje_por_cobrar":row[28],
                        "porcentaje_por_gastar":row[29],
                        "total_proveedor":cls.formatear_a_pesos(row[30]),
                        "total_diferencia":cls.formatear_a_pesos(row[31]),
                        "porcentaje_indirecto":row[32],
                        "estatus_contratos":row[33],
                        "estatus_presupuesto":row[34],
                        "detalle_presupuesto" : []
                    }
                return presupuesto
        except Exception as ex:
            raise Exception(f"Error al obtener el presupuesto: {ex}")

    @classmethod
    def obtener_detalle_presupuesto_por_id(cls,db, id):
        """
            Obtener el detalle de presupuesto por id
        """
        try:
            with db.cursor() as cursor:
                query = """
                     
                     SELECT * FROM DetallesPresupuesto WHERE id_presupuesto = ?
                    ;
                """

                cursor.execute(query, (id,))
                rows = cursor.fetchall()
                
                presupuesto = [DetallePresupuesto(id=row[0],
                                                  id_presupuesto=row[1],
                                                  id_concepto=row[2],
                                                  id_proveedor=row[3],
                                                  concepto=row[4],
                                                  contrato_firmado=row[5],
                                                  presupuesto_cliente=cls.formatear_a_pesos(row[6]),
                                                  presupuesto_contratista=cls.formatear_a_pesos(row[7]),
                                                  diferencia=cls.formatear_a_pesos(row[8]),
                                                  is_blocked=row[9],
                                                  estatus=row[10]
                )
                               for row in rows
                ]
                return presupuesto
        except Exception as ex:
            raise Exception(f"Error al obtener el presupuesto: {ex}")


    @classmethod
    def obtener_presupuesto_bauart_por_detalle(cls, db, id_detalle):
        """
        Obtener los presupuestos Bauart asociados a un conjunto de detalles.
        """
        try:
            # Lista para almacenar todos los presupuestos encontrado
            with db.cursor() as cursor:
                
                query = """
                    SELECT * FROM PresupuestosBauart WHERE id_detalle = ?;
                    """
                cursor.execute(query, (id_detalle,))
                row = cursor.fetchone()

                if row:  # Verificar si hay resultados
                    presupuesto_bauart = PresupuestoBauart(
                        id=row[0],
                        id_detalle=row[1],
                        nombre_presupuesto=row[2],
                        total_presupuesto_cliente=cls.formatear_a_pesos(row[3]),
                        total_presupuesto_proveedor=cls.formatear_a_pesos(row[4]),
                        diferencia_presupuesto=cls.formatear_a_pesos(row[5]),
                        is_blocked=row[6],
                        estatus=row[7]
                    )
                
                else:
                    presupuesto_bauart = None   
                    
            return presupuesto_bauart  # Devolver la lista completa de presupuestos
        except Exception as ex:
            raise Exception(f"Error al obtener el presupuesto: {ex}")

    @classmethod
    def obtener_detalle_de_presupuesto_bauart(cls, db, id):
        """
        Obtener los presupuestos Bauart asociados a un conjunto de detalles.
        """
        try:
            presupuestos = []  # Lista para almacenar todos los presupuestos encontrados
            with db.cursor() as cursor:
                query = """
                    SELECT * FROM DetallesBauart WHERE id_presupuesto_bauart = ?;
                """
                cursor.execute(query, (id,))
                rows = cursor.fetchall()
                if rows:  # Verificar si hay resultados
                    presupuestos.extend([
                        DetalleBauart(
                            id=row[0],
                            id_presupuesto_bauart=row[1],
                            concepto=row[2],
                            presupuesto_cliente=cls.formatear_a_pesos(row[3]),
                            presupuesto_contratista=cls.formatear_a_pesos(row[4]),
                            diferencia=cls.formatear_a_pesos(row[5]), 
                            id_proveedor=row[6],   
                            is_blocked=row[7],
                            is_nomina=row[8],
                            id_concepto=row[9],
                            estatus=row[10]
                            )
                        for row in rows
                        ])
            return presupuestos  # Devolver la lista completa de presupuestos
        except Exception as ex:
            raise Exception(f"Error al obtener el presupuesto: {ex}")

 
    
    @classmethod
    def obtener_presupuestos(cls, db):
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT 
                        p.id_presupuesto,
                        p.proyecto,
                        p.id_proyecto,
                        p.id_cliente, 
                        c.RAZON_SOCIAL AS cliente,
                        p.id_empresa,
                        e.RAZON_SOCIAL AS empresa,
                        p.id_director,
                        p.presupuesto_cliente,
                        p.estatus_proyecto,
                        p.pagado_cliente,
                        p.porcentaje_pagado,
                        p.gastado_real,
                        p.porcentaje_gastado,
                        p.falta_por_cobrar,
                        p.falta_por_gastar,
                        p.subtotal_cliente_iva,
                        p.indirecto_cliente_iva,
                        p.total_cliente_iva,
                        p.sub_proveedor,
                        p.sub_diferencia,
                        p.usuario,
                        u.NOMBRE_USUARIO AS nombre_usuario,
                        p.estatus,
                        p.total_contratista,
                        p.total_diferencia,
                        p.porcentaje_indirecto
                    FROM Presupuestos AS p
                    INNER JOIN CLIENTES AS c ON c.ID = p.id_cliente
                    INNER JOIN EMPRESAS AS e ON e.ID = p.id_empresa
                    INNER JOIN USUARIOS AS u ON u.ID = p.usuario;
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                presupuestos = []
                for row in rows:
                    # Mapear resultados a objetos o diccionarios
                    presupuesto ={
                            "id_presupuesto": row[0],
                            "proyecto": row[1],
                            "id_proyecto": row[2],
                            "id_cliente": row[3],
                            "cliente": row[4],
                            "id_empresa": row[5],
                            "empresa": row[6],
                            "id_director": row[7],
                            "presupuesto_cliente": cls.formatear_a_pesos(row[8]),
                            "estatus_proyecto":cls.formatear_a_pesos(row[9]),
                            "pagado_cliente":cls.formatear_a_pesos(row[10]),
                            "porcentaje_pagado":cls.formatear_a_pesos(row[11]),
                            "gastado_real": cls.formatear_a_pesos(row[12]),
                            "porcentaje_gastado": cls.formatear_a_pesos(row[13]),
                            "falta_por_cobrar": cls.formatear_a_pesos(row[14]),
                            "falta_por_gastar": cls.formatear_a_pesos(row[15]),
                            "subtotal_cliente_iva": cls.formatear_a_pesos(row[16]),
                            "indirecto_cliente_iva": cls.formatear_a_pesos(row[17]),
                            "total_cliente_iva": cls.formatear_a_pesos(row[18]),
                            "sub_proveedor": cls.formatear_a_pesos(row[19]),
                            "sub_diferencia": cls.formatear_a_pesos(row[20]),
                            "diferencia_es_negativa" : cls.vierificar_diferecnia(row[20]),
                            "usuario": row[21],
                            "nombre_usuario": row[22],
                            "estatus": row[23],
                            "total_proveedor":row[24],
                            "total_diferencia": row[25],
                            "porcentaje_indirecto": row[26]
                    }
                    detalle_presupuesto = cls.obtener_detalle_presupuesto_por_id(db, presupuesto["id_presupuesto"])
                    contras_firmados = 0
                    partidas_aprobadas = 0
                    
                    
                    for i in  detalle_presupuesto:
                        if i.contrato_firmado == 1:
                            contras_firmados += 1
                        if i.estatus == 1:
                            partidas_aprobadas += 1
                    
                    partidas_totales = len(detalle_presupuesto)
                    presupuesto["contratos_firmados"] = contras_firmados
                    presupuesto["partidas_aprobadas"] = partidas_aprobadas
                    presupuesto["partidas_sin_contrato"] = partidas_totales - contras_firmados
                    presupuesto["partidas_por_aprobar"] = partidas_totales - partidas_aprobadas
                    presupuesto["partidas_totales"] = partidas_totales  
                        
                    presupuestos.append(presupuesto)
                    
                return presupuestos
        except Exception as ex:
            raise Exception(f"Error al obtener los presupuestos: {ex}")



    @classmethod
    def get_detalles_by_presupuesto(cls, db, id_presupuesto):
        """
        Obtener los detalles de un presupuesto específico.
        """
        try:
            with db.cursor() as cursor:
                query = """
                      SELECT * FROM DetallesPresupuesto WHERE id_presupuesto = ?
                """
                cursor.execute(query, (id_presupuesto,))
                rows = cursor.fetchall()
                
                
                return [DetallePresupuesto(*row) for row in rows] if rows else []
        except Exception as ex:
            raise Exception(f"Error al obtener detalles del presupuesto: {ex}")

    @classmethod
    def get_bauart_by_detalle(cls, db, id_detalle):
        """
        Obtener un presupuesto Bauart asociado a un detalle.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT id_presupuesto_bauart, id_detalle, nombre_presupuesto, total_presupuesto_cliente,
                           total_presupuesto_proveedor, diferencia_presupuesto, is_blocked
                    FROM PresupuestosBauart
                    WHERE id_detalle = ?
                """
                cursor.execute(query, (id_detalle,))
                row = cursor.fetchone()
                return PresupuestoBauart(*row) if row else None
        except Exception as ex:
            raise Exception(f"Error al obtener el presupuesto Bauart: {ex}")

    @classmethod
    def get_all_bauart(cls, db):
        """
        Obtener todos los presupuestos Bauart.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT id_presupuesto_bauart, id_detalle, nombre_presupuesto, total_presupuesto_cliente,
                           total_presupuesto_proveedor, diferencia_presupuesto, is_blocked
                    FROM PresupuestosBauart
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                return [PresupuestoBauart(*row) for row in rows] if rows else []
        except Exception as ex:
            raise Exception(f"Error al obtener todos los presupuestos Bauart: {ex}")

    @classmethod
    def get_detalles_bauart_by_presupuesto(cls, db, id_presupuesto_bauart):
        """
        Obtener las partidas asociadas a un presupuesto Bauart.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT id_detalle_bauart, id_presupuesto_bauart, concepto, presupuesto_cliente, presupuesto_contratista,
                           diferencia, id_proveedor, is_blocked
                    FROM DetallesBauart
                    WHERE id_presupuesto_bauart = ?
                """
                cursor.execute(query, (id_presupuesto_bauart,))
                rows = cursor.fetchall()
                return [DetalleBauart(*row) for row in rows] if rows else []
        except Exception as ex:
            raise Exception(f"Error al obtener detalles Bauart: {ex}")

    @classmethod
    def get_all_detalles_bauart(cls, db):
        """
        Obtener todos los detalles Bauart.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT id_detalle_bauart, id_presupuesto_bauart, concepto, presupuesto_cliente, presupuesto_contratista,
                           diferencia, id_proveedor, is_blocked
                    FROM DetallesBauart
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                return [DetalleBauart(*row) for row in rows] if rows else []
        except Exception as ex:
            raise Exception(f"Error al obtener todos los detalles Bauart: {ex}")

    @classmethod
    def get_presupuesto_por_proyecto(cls, db, proyecto_id):
        """
        Obtener un presupuesto asociado a un proyecto específico.
        """
        try:
            with db.cursor() as cursor:
                # Cambiar LIMIT por TOP 1 para SQL Server
                query = """
                    SELECT TOP 1
                        id_presupuesto, id_cliente, id_director, id_empresa, id_proyecto, usuario, estatus_proyecto,
                        presupuesto_cliente, sub_proveedor, subtotal_cliente_iva, total_cliente_iva, indirecto_cliente_iva,
                        sub_diferencia, pagado_cliente, porcentaje_pagado, falta_por_cobrar, falta_por_gastar, is_blocked,
                        porcentaje_gastado, porcentaje_por_gastar
                    FROM Presupuestos
                    WHERE id_proyecto = ?
                    ORDER BY id_presupuesto DESC
                """
                cursor.execute(query, (proyecto_id,))
                row = cursor.fetchone()
                return Presupuesto(*row) if row else None
        except Exception as ex:
            raise Exception(f"Error al obtener presupuesto por proyecto: {ex}")

        
    @classmethod
    def get_proyecto_last_by_id(cls, db):
        """
        Obtiene el último proyecto registrado.
        """
        try:
            with db.cursor() as cursor:
                # Cambiar LIMIT por TOP para SQL Server
                query = "SELECT TOP 1 * FROM PROYECTOS ORDER BY ID DESC"
                cursor.execute(query)
                row = cursor.fetchone()
                if row:
                    return ModelProyectoObra(
                        id=row[0],
                        id_cliente=row[1],
                        id_empresa=row[2],
                        nombre_proyecto=row[3],
                        tipo_id=row[4],
                        fecha_inicio=row[5],
                        fecha_fin=row[6],
                        pais=row[7],
                        estado=row[8],
                        municipio=row[9],
                        colonia=row[10],
                        calle=row[11],
                        numero_exterior=row[12],
                        numero_interior=row[13],
                        cp=row[14],
                        centro_comercial=row[15],
                        director_proyecto=row[16],
                        lider_proyecto=row[17],
                        gerente_proyecto=row[18],
                        lider1=row[19],
                        lider2=row[20],
                        fecha_registro=row[21],
                        usuario_id=row[22],
                        is_blocked=row[23]
                    )
                return None
        except Exception as ex:
            raise Exception(f"Error al obtener el último proyecto: {ex}")
    
    @classmethod
    def verificar_proveedor_en_detalles(cls, db, id_presupuesto):
        """
        Verifica si algún detalle del presupuesto tiene un proveedor con ID 0.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT COUNT(*)
                    FROM DetallesPresupuesto
                    WHERE id_presupuesto = ? AND id_proveedor = 0
                """
                cursor.execute(query, (id_presupuesto,))
                count = cursor.fetchone()[0]
                return count > 0  # Devuelve True si hay algún proveedor con ID 0
        except Exception as ex:
            raise Exception(f"Error al verificar proveedores en detalles del presupuesto: {ex}")
        
    @classmethod
    def get_detalles_bauart_by_presupuesto(cls, db, id_presupuesto_bauart):
        """
        Obtiene los detalles de DetallesBauart asociados a un PresupuestoBauart.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT 
                        id_detalle_bauart, 
                        id_presupuesto_bauart, 
                        concepto, 
                        presupuesto_cliente, 
                        presupuesto_contratista, 
                        diferencia, 
                        id_proveedor, 
                        is_blocked
                    FROM 
                        DetallesBauart
                    WHERE 
                        id_presupuesto_bauart = ?
                """
                cursor.execute(query, (id_presupuesto_bauart,))
                rows = cursor.fetchall()

                # Mapeo de los resultados a una lista de diccionarios
                detalles = [
                    {
                        "id_detalle_bauart": row[0],
                        "id_presupuesto_bauart": row[1],
                        "concepto": row[2],
                        "presupuesto_cliente": row[3],
                        "presupuesto_contratista": row[4],
                        "diferencia": row[5],
                        "id_proveedor": row[6],
                        "is_blocked": row[7]
                    }
                    for row in rows
                ]

                return detalles
        except Exception as ex:
            raise Exception(f"Error al obtener los detalles Bauart: {ex}")

    class PresupuestoService:
        @staticmethod
        def obtener_detalles_bauart_por_proyecto(db, proyecto_id):
            try:
                # Paso 1: Obtener el presupuesto asociado al proyecto
                presupuesto = ModelPresupuesto.get_presupuesto_por_proyecto(db, proyecto_id)
                if not presupuesto:
                    return {"error": "No se encontró un presupuesto asociado a este proyecto."}

                # Paso 2: Verificar si algún detalle del presupuesto tiene un proveedor con ID 0
                tiene_proveedor_cero = ModelPresupuesto.verificar_proveedor_en_detalles(db, presupuesto.id_presupuesto)
                if not tiene_proveedor_cero:
                    return {"mensaje": "Todos los detalles del presupuesto tienen un proveedor asignado."}

                # Paso 3: Obtener los presupuestos Bauart asociados a los detalles
                detalles_presupuesto = ModelPresupuesto.get_detalles_by_presupuesto(db, presupuesto.id_presupuesto)
                resultados = []

                for detalle in detalles_presupuesto:
                    if detalle.id_proveedor == 0:
                        # Obtener el presupuesto Bauart del detalle
                        bauart = ModelPresupuesto.get_bauart_by_detalle(db, detalle.id_detalle)
                        if bauart:
                            # Paso 4: Obtener los detalles Bauart asociados al presupuesto Bauart
                            detalles_bauart = ModelPresupuesto.get_detalles_bauart_by_presupuesto(db, bauart.id_presupuesto_bauart)
                            resultados.append({
                                "detalle": detalle.__dict__,
                                "bauart": bauart.__dict__,
                                "detalles_bauart": detalles_bauart
                            })

                return resultados if resultados else {"mensaje": "No se encontraron presupuestos Bauart asociados a detalles con proveedor 0."}

            except Exception as ex:
                raise Exception(f"Error al procesar los detalles Bauart por proyecto: {ex}")


    @classmethod
    def obtener_presupuestos_bauart(cls, db, proyecto_id):
        """
        Obtiene todos los presupuestos Bauart asociados a un proyecto específico.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT 
                        pb.id_presupuesto_bauart, pb.id_detalle, pb.nombre_presupuesto, 
                        pb.total_presupuesto_cliente, pb.total_presupuesto_proveedor, 
                        pb.diferencia_presupuesto, pb.is_blocked
                    FROM 
                        PresupuestosBauart pb
                    INNER JOIN 
                        DetallesPresupuesto dp ON pb.id_detalle = dp.id_detalle
                    INNER JOIN 
                        Presupuestos p ON dp.id_presupuesto = p.id_presupuesto
                    WHERE 
                        p.id_proyecto = ?
                """
                cursor.execute(query, (proyecto_id,))
                rows = cursor.fetchall()

                # Convertir resultados en un formato estructurado
                return [
                    {
                        "id_presupuesto_bauart": row[0],
                        "id_detalle": row[1],
                        "nombre_presupuesto": row[2],
                        "total_presupuesto_cliente": row[3],
                        "total_presupuesto_proveedor": row[4],
                        "diferencia_presupuesto": row[5],
                        "is_blocked": row[6],
                    }
                    for row in rows
                ]
        except Exception as ex:
            raise Exception(f"Error al obtener presupuestos Bauart: {ex}")
        
    
    def convertir_a_float(valor, valor_default=0.0):
        """
        Convierte un valor a float. Si no es posible, devuelve un valor predeterminado.
        
        :param valor: Valor a convertir
        :param valor_default: Valor por defecto si la conversión falla
        :return: Valor convertido a float o el valor por defecto
        """
        try:
            # Elimina el símbolo '$' y las comas, luego convierte a float
            return float(valor.replace("$", "").replace(",", ""))
        except (ValueError, AttributeError):
            return valor_default


    
    @classmethod
    def actualizar_presupuesto(cls, db, presupuesto):
        try:
            with db.cursor() as cursor:
                presupuesto_actual = cls.obtener_presupuesto_por_id(db,presupuesto.id)
                
                query = "UPDATE Presupuestos SET "
                params = []
                updates = []

                if presupuesto_actual['presupuesto_cliente'] != presupuesto.presupuesto_cliente:
                    updates.append("presupuesto_cliente = ?")
                    params.append(cls.convertir_a_float(presupuesto.presupuesto_cliente))
                
                if presupuesto_actual['pagado_cliente'] != presupuesto.pagado_cliente:
                    updates.append("pagado_cliente = ?")
                    params.append(cls.convertir_a_float(presupuesto.pagado_cliente))
                
                if presupuesto_actual['porcentaje_gastado'] != presupuesto.porcetaje_gastado_real:
                    updates.append("porcentaje_gastado = ?")
                    params.append(float(presupuesto.porcetaje_gastado_real))
                
                if presupuesto_actual['subtotal_cliente_iva'] != presupuesto.subtotal_cliente:
                    updates.append("subtotal_cliente_iva = ?")
                    params.append(cls.convertir_a_float(presupuesto.subtotal_cliente))
                
                if presupuesto_actual['sub_proveedor'] != presupuesto.subtotal_proveedor:
                    updates.append("sub_proveedor = ?")
                    params.append(cls.convertir_a_float(presupuesto.subtotal_proveedor))
                
                if presupuesto_actual['sub_diferencia'] != presupuesto.subtotal_diferencia:
                    updates.append("sub_diferencia = ?")
                    params.append(cls.convertir_a_float(presupuesto.subtotal_diferencia))
                
                if presupuesto_actual['indirecto_cliente_iva'] != presupuesto.total_porcentaje_indirecto:
                    updates.append("indirecto_cliente_iva = ?")
                    params.append(cls.convertir_a_float(presupuesto.total_porcentaje_indirecto))
                
                if presupuesto_actual['total_cliente_iva'] != presupuesto.total_cliente:
                    updates.append("total_cliente_iva = ?")
                    params.append(cls.convertir_a_float(presupuesto.total_cliente))
                
                if presupuesto_actual['total_proveedor'] != presupuesto.total_proveedor:
                    updates.append("total_contratista = ?")
                    params.append(cls.convertir_a_float(presupuesto.total_proveedor))
                
                if presupuesto_actual['total_diferencia'] != presupuesto.total_diferencia:
                    updates.append("total_diferencia = ?")
                    params.append(cls.convertir_a_float(presupuesto.total_diferencia))
                
                if presupuesto_actual['usuario'] != presupuesto.usuario_id:
                    updates.append("usuario = ?")
                    params.append(presupuesto.usuario_id)
                    
                if presupuesto_actual['estatus'] != presupuesto.estatus:
                    updates.append("estatus = ?")
                    params.append(presupuesto.estatus)
                    
                if presupuesto_actual['estatus_contratos'] != presupuesto.estatus_contratos:  
                    updates.append("estatus_contratos = ?")
                    params.append(presupuesto.estatus_contratos)
                
                if presupuesto_actual['estatus_presupuesto'] != presupuesto.estatus_presupuesto:
                    updates.append("estatus_presupuesto = ?")
                    params.append(presupuesto.estatus_presupuesto)
                
                updates.append("porcentaje_indirecto = ?")
                params.append(float(presupuesto.porcentaje_indirecto))
                    
                if updates:
                    query += ", ".join(updates) + " WHERE id_presupuesto = ?"
                    params.append(int(presupuesto.id))
                    cursor.execute(query, params)
                    db.commit()
                
                return True
                
        except Exception as ex:
            print(f"Error al actualizar el presupuesto: {ex}")
            raise ex
    
  
        
    @classmethod
    def actualizar_detalle_presupuesto(cls, db, fila):
        try:
            with db.cursor() as cursor:
                # Recuperar el detalle actual
                cursor.execute("SELECT * FROM DetallesPresupuesto WHERE id_detalle = ?", (fila['id_detalle'],))
                detalle_actual = cursor.fetchone()
                
                query = "UPDATE DetallesPresupuesto SET "
                params = []
                updates = []
                
                if detalle_actual[2] != fila['id_proveedor']:
                    updates.append("id_proveedor = ?")
                    params.append(int(fila['id_proveedor']))
                
                if detalle_actual[5] != fila['contrato_firmado']:   
                    updates.append("contrato_firmado = ?")
                    params.append(fila['contrato_firmado'])
                   
                 
                if detalle_actual[6] != fila['presupuesto_cliente']:
                    updates.append("presupuesto_cliente = ?")
                    params.append(fila['presupuesto_cliente'])
                    
                if detalle_actual[7] != fila['presupuesto_contratista']:
                    updates.append("presupuesto_contratista = ?")
                    params.append(fila['presupuesto_contratista'])
                
                if detalle_actual[8] != fila['diferencia']:
                    updates.append("diferencia = ?")
                    params.append(fila['diferencia'])
                
                if detalle_actual[10] != fila['estatus']:
                    updates.append("estatus = ?")
                    params.append(int(fila['estatus']))
                    
                if updates:
                    query += ", ".join(updates) + " WHERE id_detalle = ?"
                    params.append(fila['id_detalle'])
                    
                    # Imprime la consulta SQL para depuración
                    print("Executing query:", query)
                    print("With parameters:", params)
                    
                    cursor.execute(query, params)
                    db.commit()
            
            return True
        except Exception as ex:
            db.rollback()
            print(f"Error al actualizar el detalle del presupuesto: {ex}")
            raise ex    
        
    @classmethod
    def actualizar_presupuesto_bauart(cls, db, fila):
        try:
            with db.cursor() as cursor:
                # Recuperar el detalle actual
                cursor.execute("SELECT * FROM PresupuestosBauart WHERE id_presupuesto_bauart = ?", (fila['id_detalle'],))
                detalle_actual = cursor.fetchone()
                
                query = "UPDATE PresupuestosBauart SET "
                params = []
                updates = []
                
                if detalle_actual[3] != fila['presupuesto_cliente']:
                    updates.append("total_presupuesto_cliente = ?")
                    params.append(fila['presupuesto_cliente'])
                    
                if detalle_actual[4] != fila['presupuesto_contratista']:
                    updates.append("total_presupuesto_proveedor = ?")
                    params.append(fila['presupuesto_contratista'])
                    
                if detalle_actual[5] != fila['diferencia']:
                    updates.append("diferencia_presupuesto = ?")
                    params.append(fila['diferencia'])
                
                    
                if updates:
                    query += ", ".join(updates) + " WHERE id_presupuesto_bauart = ?"
                    params.append(fila['id_detalle'])
                    
                    # Imprime la consulta SQL para depuración
                    print("Executing query:", query)
                    print("With parameters:", params)
                    
                    cursor.execute(query, params)
                    db.commit()
            
            return True
        except Exception as ex:
            db.rollback()
            print(f"Error al actualizar el detalle del presupuesto: {ex}")
            raise ex
        
    @classmethod
    def actualizar_presupuesto_bauart_detalle(cls,db,fila):
            try:
                with db.cursor() as cursor:
                    # Recuperar el detalle actual
                    cursor.execute("SELECT * FROM DetallesBauart WHERE id_detalle_bauart = ?", (fila['id_detalle'],))
                    detalle_actual = cursor.fetchone()
                    
                    query = "UPDATE DetallesBauart SET "
                    params = []
                    updates = []
                    
                    if detalle_actual[2] != fila['especialidad']:
                        updates.append("[concepto] = ?")
                        params.append(fila['especialidad'])
                    
                    if detalle_actual[3] != fila['presupuesto_cliente']:
                        updates.append("presupuesto_cliente = ?")
                        params.append(fila['presupuesto_cliente'])
                        
                    if detalle_actual[4] != fila['presupuesto_proveedor']:
                        updates.append("presupuesto_contratista = ?")
                        params.append(fila['presupuesto_proveedor'])
                        
                    if detalle_actual[5] != fila['diferencia']:
                        updates.append("diferencia = ?")
                        params.append(fila['diferencia'])
                    
                
                    if detalle_actual[9] != fila['id_concepto']:
                        updates.append("id_concepto = ?")
                        params.append(fila['id_concepto'])
                    
                    if detalle_actual[10] != fila['estatus']:
                        updates.append("estatus = ?")
                        params.append(fila['estatus'])
                    
                    if updates:
                        query += ", ".join(updates) + " WHERE id_detalle_bauart = ?"
                        params.append(fila['id_detalle'])
                        
                        # Imprime la consulta SQL para depuración
                        print("Executing query:", query)
                        print("With parameters:", params)
                        
                        cursor.execute(query, params)
                        db.commit()
                
                return True
            except Exception as ex:
                db.rollback()
                print(f"Error al actualizar el detalle del presupuesto: {ex}")
                raise ex
            
            