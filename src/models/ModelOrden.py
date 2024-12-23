from .entities.Partida import Partida
from .entities.Proveedores import Proveedores


class MyOrdendeCompra:

    @classmethod
    def get_proveedor_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = """
                SELECT 
                    p.*, 
                    c.NUMERO_CUENTA, 
                    c.CLABE,
                    b.NOMBRE AS BANCO
                FROM PROVEEDORES p
                LEFT JOIN CUENTAS_PROVEEDORES c ON p.ID = c.ID_PROVEEDOR
                LEFT JOIN BANCOS b ON c.ID_BANCO = b.ID
                WHERE p.ID = ?
            """
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                proveedor = Proveedores(
                    id=row[0], id_empresa=row[1], razon_social=row[2], regimen_fiscal_id=row[3], tipo_id=row[4], rfc=row[5],
                    pais=row[6], estado=row[7], cp=row[8], municipio=row[9], colonia=row[10],
                    calle=row[11], numero_exterior=row[12], numero_interior=row[13],
                    fecha_registro=row[14], usuario=row[15], is_blocked=row[16]
                )
                proveedor.cuenta_pesos = row[17] if len(row) > 17 else None
                proveedor.clabe = row[18] if len(row) > 18 else None
                proveedor.banco = row[19] if len(row) > 19 else "No disponible"
                return proveedor
            return None
        except Exception as ex:
            raise Exception(f"Error al obtener el proveedor: {ex}")

    @staticmethod
    def get_contactos_by_proveedor_id(db, proveedor_id):
        query = """
            SELECT NOMBRE, APELLIDO, PUESTO, TELEFONO, CORREO
            FROM CONTACTOS_PROVEEDORES
            WHERE ID_PROVEEDOR = ?
        """
        try:
            cursor = db.cursor()
            cursor.execute(query, (proveedor_id,))
            contactos = cursor.fetchall()
            contactos_list = [
                {
                    "NOMBRE": contacto[0],
                    "APELLIDO": contacto[1],
                    "PUESTO": contacto[2],
                    "TELEFONO": contacto[3],
                    "CORREO": contacto[4],
                }
                for contacto in contactos
            ]
            return contactos_list
        except Exception as e:
            print(f"Error al obtener contactos: {e}")
            return []

    @staticmethod
    def get_partidas_by_orden_id(conn, orden_id):
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM PARTIDAS_REQUISICION WHERE ID_ORDEN = ?"
            cursor.execute(query, (orden_id,))
            results = cursor.fetchall()
            partidas = [
                {
                    "id": row[0],
                    "descripcion": row[2],
                    "unidad": row[3],
                    "cantidad": row[4],
                    "precio_unitario": row[9],
                    "total": row[10],
                }
                for row in results
            ]
            return partidas
        except Exception as e:
            print(f"Error al obtener partidas por orden: {e}")
            return []

    @staticmethod
    def get_requisicion_by_id(db, id_requisicion):
        query = """
            SELECT ID_REQUISICION, NOMBRE_PROYECTO, CONCEPTO, FECHA_LLEGADA, STATUS, FECHA_SOLICITUD, FECHA_REQUERIDA
            FROM REQUISICIONES
            WHERE ID_REQUISICION = ?
        """
        cursor = db.cursor()
        cursor.execute(query, (id_requisicion,))
        row = cursor.fetchone()

        if row:
            return {
                "id": row[0],
                "nombre_proyecto": row[1],
                "concepto": row[2],
                "fecha_llegada": row[3].strftime('%Y-%m-%d') if row[3] else None,
                "status": row[4],
                "fecha_solicitud": row[5].strftime('%Y-%m-%d') if row[5] else None,
                "fecha_requerida": row[6].strftime('%Y-%m-%d') if row[6] else None,
            }
        else:
            return None

    @staticmethod
    def create_orden(db, id_requisicion, id_proveedor, fecha_hora_entrega=None, direccion_entrega=None, contacto=None, telefono=None):
        query_insert = """
            INSERT INTO ORDENES (ID_REQUISICION, ID_PROVEEDOR, FechaHoraEntrega, DireccionEntrega, Contacto, Telefono)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        query_identity = "SELECT SCOPE_IDENTITY()"
        cursor = db.cursor()

        try:
            cursor.execute(query_insert, (id_requisicion, id_proveedor, fecha_hora_entrega, direccion_entrega, contacto, telefono))
            cursor.execute(query_identity)
            last_id = cursor.fetchone()[0]
            db.commit()
            return last_id
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def get_partidas_by_requisicion_id(db, id_requisicion):
        query = """
            SELECT ID, ID_REQUISICION, DESCRIPCION, UNIDAD, CANTIDAD, FECHA_CREACION, DETALLES, STATUS
            FROM PARTIDAS_REQUISICION
            WHERE ID_REQUISICION = ?
        """
        cursor = db.cursor()
        cursor.execute(query, (id_requisicion,))
        rows = cursor.fetchall()

        partidas = []
        for row in rows:
            partidas.append({
                "id": row[0],
                "id_requisicion": row[1],
                "descripcion": row[2],
                "unidad": row[3],
                "cantidad": row[4],
                "fecha_creacion": row[5].strftime('%Y-%m-%d') if row[5] else None,
                "detalles": row[6],
                "status": row[7]
            })

        return partidas

    @staticmethod
    def guardar_orden(conn, id_requisicion, id_proveedor, fecha_hora_entrega, direccion_entrega, contacto, telefono, porcentaje_descuento, numero_cotizacion):
        """
        Inserta una nueva orden en la tabla ORDENES con el nuevo campo Número de Cotización.

        :param conn: Conexión a la base de datos.
        :param id_requisicion: ID de la requisición asociada.
        :param id_proveedor: ID del proveedor.
        :param fecha_hora_entrega: Fecha y hora de entrega.
        :param direccion_entrega: Dirección de entrega.
        :param contacto: Nombre del contacto.
        :param telefono: Teléfono del contacto.
        :param porcentaje_descuento: Porcentaje de descuento aplicado a la orden.
        :param numero_cotizacion: Número de cotización.
        :return: ID de la nueva orden creada.
        """
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO ORDENES 
                (id_requisicion, id_proveedor, FechaHoraEntrega, DireccionEntrega, Contacto, Telefono, PorcentajeDescuento, NumeroCotizacion) 
                OUTPUT INSERTED.id 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (id_requisicion, id_proveedor, fecha_hora_entrega, direccion_entrega, contacto, telefono, porcentaje_descuento, numero_cotizacion)
            )
            id_orden = cursor.fetchone()[0]
            conn.commit()
            return id_orden
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()


    @staticmethod
    def actualizar_partidas(conn, id_orden, partidas):
        """
        Actualiza las partidas en la base de datos con el ID de orden y el precio unitario.
        Calcula automáticamente el total basado en la cantidad y el precio unitario.

        :param conn: Conexión a la base de datos
        :param id_orden: ID de la orden asociada
        :param partidas: Lista de partidas con ID y precio_unitario
        """
        try:
            cursor = conn.cursor()
            for partida in partidas:
                partida_id = partida.get('id')
                precio_unitario = partida.get('precio_unitario')

                if not partida_id or not precio_unitario:
                    raise ValueError("Datos incompletos en partidas")

                # Actualizar el precio unitario y el id_orden
                cursor.execute(
                    """
                    UPDATE PARTIDAS_REQUISICION 
                    SET id_orden = ?, precio_unitario = ? 
                    WHERE id = ?
                    """,
                    (id_orden, precio_unitario, partida_id)
                )

                # Calcular el total basado en cantidad * precio_unitario
                cursor.execute(
                    """
                    UPDATE PARTIDAS_REQUISICION 
                    SET total = (cantidad * precio_unitario)
                    WHERE id = ?
                    """,
                    (partida_id,)
                )

            conn.commit()
            return True

        except Exception as e:
            raise Exception(f"Error al actualizar partidas: {str(e)}")