from .entities.Presupuestos import Presupuesto,DetallePresupuesto,PresupuestoBauart,DetalleBauart
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
                    id_presupuesto, id_cliente, id_director, id_empresa, id_proyecto, usuario, estatus_proyecto, 
                    presupuesto_cliente, sub_proveedor, subtotal_cliente_iva, total_cliente_iva, indirecto_cliente_iva, 
                    sub_diferencia, pagado_cliente, porcentaje_pagado, falta_por_cobrar, falta_por_gastar, 
                    gastado_real, porcentaje_gastado, porcentaje_por_gastar, is_blocked
                FROM Presupuestos;
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                
                # Mapear resultados a objetos Presupuesto
                presupuestos = [
                    Presupuesto(
                        id=row[0],
                        id_cliente=row[1],
                        id_director=row[2],
                        id_empresa=row[3],
                        id_proyecto=row[4],
                        usuario_id=row[5],
                        estatus_proyecto=row[6],
                        presupuesto_cliente=row[7],
                        sub_proveedor=row[8],
                        sub_client_iva=row[9],
                        total_cliente_iva=row[10],
                        indirecto_client_iva=row[11],
                        sub_diferencia=row[12],
                        pagado_cliente=row[13],
                        porcentaje_pagado=row[14],
                        falta_por_cobrar=row[15],
                        falta_por_gastar=row[16],
                        gastado_real=row[17],
                        porcentaje_gastado=row[18],
                        porcentaje_por_gastar=row[19],
                        is_blocked=row[20]
                    )                    
                    for row in rows
                ]
                
                return presupuestos
        except Exception as ex:
            raise Exception(f"Error al actualizar el presupuesto: {ex}")