from .entities.Presupuestos import Presupuesto,DetallePresupuesto,PresupuestoBauart,DetalleBauart
from models.ModelProyectoObra import ModelProyectoObra

class ModelPresupuesto:

    @classmethod
    def crear_presupuesto(cls, db, presupuesto):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO Presupuestos (
                        id_cliente, id_director, id_empresa,proyecto, id_proyecto, usuario, estatus_proyecto, presupuesto_cliente, 
                        sub_proveedor, subtotal_cliente_iva, total_cliente_iva, indirecto_cliente_iva, sub_diferencia, 
                        pagado_cliente, porcentaje_pagado, falta_por_cobrar, falta_por_gastar, 
                        gastado_real, porcentaje_gastado, porcentaje_por_gastar
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
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
                    presupuesto.sub_proveedor,
                    presupuesto.sub_client_iva,
                    presupuesto.total_cliente_iva,
                    presupuesto.indirecto_client_iva,
                    presupuesto.sub_diferencia,
                    presupuesto.pagado_cliente,
                    presupuesto.porcentaje_pagado,
                    presupuesto.falta_por_cobrar,
                    presupuesto.falta_por_gastar,
                    presupuesto.gastado_real,
                    presupuesto.porcentaje_gastado,
                    presupuesto.porcentaje_por_gastar
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
                        diferencia_presupuesto, is_blocked
                    ) VALUES (?, ?, ?, ?, ?, ?);
                """
                cursor.execute(query, (
                    presupuesto_bauart.id_detalle, presupuesto_bauart.nombre_presupuesto,
                    presupuesto_bauart.total_presupuesto_cliente, presupuesto_bauart.total_presupuesto_proveedor,
                    presupuesto_bauart.diferencia_presupuesto, presupuesto_bauart.is_blocked
                ))
                 # Recuperar el último ID insertado
                cursor.execute("SELECT TOP (1) [id_presupuesto_bauart] FROM PresupuestosBauart ORDER BY [id_presupuesto_bauart] DESC;")
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
                        id_proveedor, is_blocked,is_nomina
                    ) VALUES (?, ?, ?,?, ?, ?, ?, ?,?);
                """
                cursor.execute(query, (
                    detalle_bauart.id_presupuesto_bauart,detalle_bauart.id_concepto ,detalle_bauart.concepto, detalle_bauart.presupuesto_cliente,
                    detalle_bauart.presupuesto_contratista, detalle_bauart.diferencia, detalle_bauart.id_proveedor,
                    detalle_bauart.is_blocked,detalle_bauart.is_nomina
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
    def obtener_presupuesto_por_id(cls, db, id_presupuesto):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM Presupuestos WHERE id_presupuesto = ?;"
                cursor.execute(query, (id_presupuesto,))
                row = cursor.fetchone()
                if row:
                    return Presupuesto(*row)
                return None
        except Exception as ex:
            raise Exception(f"Error al obtener el presupuesto: {ex}")

    @classmethod
    def actualizar_presupuesto(cls, db, presupuesto):
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE Presupuestos
                    SET id_cliente = ?, id_director = ?, id_empresa = ?, id_proyecto = ?, usuario = ?, 
                        estatus_proyecto = ?, presupuesto_cliente = ?, sub_proveedor = ?, subtotal_cliente_iva = ?, 
                        total_cliente_iva = ?, indirecto_cliente_iva = ?, sub_diferencia = ?, pagado_cliente = ?, 
                        porcentaje_pagado = ?, falta_por_cobrar = ?, falta_por_gastar = ?
                    WHERE id_presupuesto = ?;
                """
                cursor.execute(query, (
                    presupuesto.id_cliente, presupuesto.id_director, presupuesto.id_empresa, presupuesto.id_proyecto,
                    presupuesto.usuario, presupuesto.estatus_proyecto, presupuesto.presupuesto_cliente,
                    presupuesto.sub_proveedor, presupuesto.subtotal_cliente_iva, presupuesto.total_cliente_iva,
                    presupuesto.indirecto_cliente_iva, presupuesto.sub_diferencia, presupuesto.pagado_cliente,
                    presupuesto.porcentaje_pagado, presupuesto.falta_por_cobrar, presupuesto.falta_por_gastar,
                    presupuesto.id_presupuesto
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al actualizar el presupuesto: {ex}")

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
                        p.estatus
                    FROM Presupuestos AS p
                    INNER JOIN CLIENTES AS c ON c.ID = p.id_cliente
                    INNER JOIN EMPRESAS AS e ON e.ID = p.id_empresa
                    INNER JOIN USUARIOS AS u ON u.ID = p.usuario;
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                # Mapear resultados a objetos o diccionarios
                presupuestos = [
                    {
                        "id_presupuesto": row[0],
                        "proyecto": row[1],
                        "id_proyecto": row[2],
                        "id_cliente": row[3],
                        "cliente": row[4],
                        "id_empresa": row[5],
                        "empresa": row[6],
                        "id_director": row[7],
                        "presupuesto_cliente": row[8],
                        "estatus_proyecto": row[9],
                        "pagado_cliente": row[10],
                        "porcentaje_pagado": row[11],
                        "gastado_real": row[12],
                        "porcentaje_gastado": row[13],
                        "falta_por_cobrar": row[14],
                        "falta_por_gastar": row[15],
                        "subtotal_cliente_iva": row[16],
                        "indirecto_cliente_iva": row[17],
                        "total_cliente_iva": row[18],
                        "sub_proveedor": row[19],
                        "sub_diferencia": row[20],
                        "usuario": row[21],
                        "nombre_usuario": row[22],
                        "estatus": row[23]
                    }
                    for row in rows
                ]

                return presupuestos
        except Exception as ex:
            raise Exception(f"Error al obtener los presupuestos: {ex}")

    # Métodos para la tabla Presupuestos
    @classmethod
    def get_presupuesto_by_id(cls, db, id_presupuesto):
        """
        Obtener un presupuesto por su ID.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT id_presupuesto, id_cliente, id_director, id_empresa, id_proyecto, usuario, estatus_proyecto,
                           presupuesto_cliente, sub_proveedor, subtotal_cliente_iva, total_cliente_iva, indirecto_cliente_iva,
                           sub_diferencia, pagado_cliente, porcentaje_pagado, falta_por_cobrar, falta_por_gastar, is_blocked,
                           porcentaje_gastado, porcentaje_por_gastar
                    FROM Presupuestos
                    WHERE id_presupuesto = ?
                """
                cursor.execute(query, (id_presupuesto,))
                row = cursor.fetchone()
                return Presupuesto(*row) if row else None
        except Exception as ex:
            raise Exception(f"Error al obtener el presupuesto: {ex}")

    @classmethod
    def get_all_presupuestos(cls, db):
        """
        Obtener todos los presupuestos.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT id_presupuesto, id_cliente, id_director, id_empresa, id_proyecto, usuario, estatus_proyecto,
                           presupuesto_cliente, sub_proveedor, subtotal_cliente_iva, total_cliente_iva, indirecto_cliente_iva,
                           sub_diferencia, pagado_cliente, porcentaje_pagado, falta_por_cobrar, falta_por_gastar, is_blocked,
                           porcentaje_gastado, porcentaje_por_gastar
                    FROM Presupuestos
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Presupuesto(*row) for row in rows] if rows else []
        except Exception as ex:
            raise Exception(f"Error al obtener todos los presupuestos: {ex}")

    @classmethod
    def get_detalles_by_presupuesto(cls, db, id_presupuesto):
        """
        Obtener los detalles de un presupuesto específico.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT id_detalle, id_presupuesto, id_concepto, id_proveedor, concepto, contrato_firmado,
                           presupuesto_cliente, presupuesto_contratista, diferencia, is_blocked
                    FROM DetallesPresupuesto
                    WHERE id_presupuesto = ?
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
        