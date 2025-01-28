from datetime import datetime
from .entities.Requisicion import Requisicion

class ModelRequisiciones:
    @classmethod
    def create_requisicion(cls, db, data):
        """
        Crea una nueva requisición en la base de datos y retorna el id de la requisición creada.
        """
        try:
            cursor = db.cursor()
            nombre_proyecto = data.get('nombre_proyecto')
            concepto = data.get('concepto')
            fecha_requerida = data.get('fecha_requerida', None)  # Permitir valor nulo
            status = data.get('status', None)  # Permitir valor nulo

            if not nombre_proyecto or not concepto:
                print("Error: 'nombre_proyecto' y 'concepto' son obligatorios.")
                return None

            # Fecha de solicitud asignada automáticamente
            fecha_solicitud = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cursor.execute("""
                INSERT INTO REQUISICIONES (NOMBRE_PROYECTO, CONCEPTO, FECHA_SOLICITUD, FECHA_REQUERIDA, STATUS)
                OUTPUT INSERTED.ID_REQUISICION
                VALUES (?, ?, ?, ?, ?)
            """, nombre_proyecto, concepto, fecha_solicitud, fecha_requerida, status)

            id_requisicion = cursor.fetchone()[0]
            db.commit()
            return id_requisicion
        except Exception as ex:
            print("Error al crear requisición:", ex)
            return None

    @classmethod
    def add_partida(cls, db, partida):
        """
        Agrega una partida a la requisición especificada en la base de datos.
        """
        try:
            cursor = db.cursor()
            id_requisicion = partida.get('id_requisicion')
            descripcion = partida.get('descripcion')
            unidad = partida.get('unidad')
            cantidad = partida.get('cantidad')
            moneda = partida.get('moneda', None)
            tipo_cambio = partida.get('tipo_cambio', None)
            fecha_creacion = partida.get('fecha_creacion', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            detalles = partida.get('detalles', None)

            if not id_requisicion or not descripcion or not unidad or not cantidad:
                print("Error: 'id_requisicion', 'descripcion', 'unidad', y 'cantidad' son obligatorios.")
                return False

            cursor.execute("""
                INSERT INTO PARTIDAS_REQUISICION (ID_REQUISICION, DESCRIPCION, UNIDAD, CANTIDAD, MONEDA, TIPO_CAMBIO, FECHA_CREACION, DETALLES)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, id_requisicion, descripcion, unidad, cantidad, moneda, tipo_cambio, fecha_creacion, detalles)
            
            db.commit()
            print(f"Partida agregada a requisición {id_requisicion}")
            return True
        except Exception as ex:
            print("Error al agregar partida:", ex)
            return False

    @classmethod
    def filter_requisiciones(cls, db, nombre_proyecto=None, concepto=None, status=None):
        """
        Filtra requisiciones según criterios opcionales.
        """
        try:
            cursor = db.cursor()
            query = "SELECT ID_REQUISICION, NOMBRE_PROYECTO, CONCEPTO, FECHA_SOLICITUD, FECHA_LLEGADA, STATUS FROM REQUISICIONES WHERE 1=1"
            params = []
            
            if nombre_proyecto:
                query += " AND NOMBRE_PROYECTO LIKE ?"
                params.append(f'%{nombre_proyecto}%')
            if concepto:
                query += " AND CONCEPTO LIKE ?"
                params.append(f'%{concepto}%')
            if status is not None:
                query += " AND STATUS = ?"
                params.append(int(status))

            cursor.execute(query, params)
            rows = cursor.fetchall()
            requisiciones = []
            for row in rows:
                requisiciones.append(Requisicion(
                    id=row[0], nombre_proyecto=row[1], concepto=row[2], 
                    fecha_solicitud=row[3], fecha_recibido=row[4], status=row[5]
                ))
        
            return requisiciones
        except Exception as ex:
            print(f"Error al filtrar requisiciones: {ex}")
            return []

    @classmethod
    def update_status(cls, db, requisicion_id, new_status):
        """
        Actualiza el estado de una requisición y establece la fecha de llegada si se ha recibido.
        """
        try:
            cursor = db.cursor()
            if new_status == 1:  # Set FECHA_LLEGADA if status is "received"
                fecha_llegada = datetime.now()
                query = "UPDATE REQUISICIONES SET STATUS = ?, FECHA_LLEGADA = ? WHERE ID_REQUISICION = ?"
                cursor.execute(query, (new_status, fecha_llegada, requisicion_id))
            else:
                query = "UPDATE REQUISICIONES SET STATUS = ? WHERE ID_REQUISICION = ?"
                cursor.execute(query, (new_status, requisicion_id))
            db.commit()
        except Exception as ex:
            print(f"Error al actualizar el estado de la requisición: {ex}")

    @staticmethod
    def obtener_requisicion(db, requisicion_id):
        """
        Obtiene los detalles de una requisición por su ID.
        """
        try:
            cursor = db.cursor()
            query = """
                SELECT ID_REQUISICION, NOMBRE_PROYECTO, CONCEPTO, FECHA_SOLICITUD, STATUS
                FROM REQUISICIONES
                WHERE ID_REQUISICION = ?
            """
            cursor.execute(query, (requisicion_id,))
            row = cursor.fetchone()
            
            if row:
                fecha_solicitud = row[3]
                if isinstance(fecha_solicitud, str):
                    try:
                        fecha_solicitud = datetime.strptime(fecha_solicitud, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        fecha_solicitud = "N/A"

                requisicion = {
                    "id": row[0],
                    "nombre_proyecto": row[1],
                    "concepto": row[2],
                    "fecha_solicitud": fecha_solicitud.strftime("%d-%m-%Y %H:%M") if isinstance(fecha_solicitud, datetime) else fecha_solicitud,
                    "status": row[4]
                }
                return requisicion
            else:
                return None
        except Exception as e:
            print(f"Error al obtener requisición: {e}")
            return None

    @staticmethod
    def obtener_partidas(db, requisicion_id):
        """
        Obtiene las partidas asociadas a una requisición.
        """
        try:
            cursor = db.cursor()
            query = """
                SELECT ID, DESCRIPCION, UNIDAD, CANTIDAD, MONEDA, TIPO_CAMBIO, FECHA_CREACION, DETALLES
                FROM PARTIDAS_REQUISICION
                WHERE ID_REQUISICION = ?
            """
            cursor.execute(query, (requisicion_id,))
            rows = cursor.fetchall()
            
            partidas = []
            for row in rows:
                partida = {
                    "id": row[0],
                    "descripcion": row[1],
                    "unidad": row[2],
                    "cantidad": row[3],
                    "moneda": row[4],
                    "tipo_cambio": row[5],
                    "fecha_creacion": row[6].strftime("%d-%m-%Y %H:%M") if isinstance(row[6], datetime) else "N/A",
                    "detalles": row[7]
                }
                partidas.append(partida)
            
            return partidas
        except Exception as e:
            print(f"Error al obtener partidas de la requisición: {e}")
            return []

    @classmethod
    def update_status(cls, db, requisicion_id, new_status):
        """
        Actualiza el estado de una requisición y establece la fecha de llegada si se ha recibido.
        """
        try:
            cursor = db.cursor()
            if new_status == 1:  # Set FECHA_LLEGADA if status is "received"
                fecha_llegada = datetime.now()
                query = "UPDATE REQUISICIONES SET STATUS = ?, FECHA_LLEGADA = ? WHERE ID_REQUISICION = ?"
                cursor.execute(query, (new_status, fecha_llegada, requisicion_id))
            else:
                query = "UPDATE REQUISICIONES SET STATUS = ? WHERE ID_REQUISICION = ?"
                cursor.execute(query, (new_status, requisicion_id))
            db.commit()
        except Exception as ex:
            print(f"Error al actualizar el estado de la requisición: {ex}")