from .entities.Presupuestos import Presupuesto
from .entities.Presupuestos import DetallePresupuesto
from .entities.Presupuestos import PresupuestoBauart
from .entities.Presupuestos import DetalleBauart
from models.ModelProyectoObra import ModelProyectoObra

class ModelPresupuesto:
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
        
        
        