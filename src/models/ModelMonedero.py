from .entities.Monedero import Monedero

class ModelMonedero:

    @classmethod
    def alta_monedero(cls, db, monedero):
        """
        Inserta un nuevo monedero en la base de datos.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO MONEDERO (
                        BANCO, NUMERO_TARJETA, ID_BANCO, ESTATUS
                    ) 
                    VALUES (
                        ?, ?, ?, ?
                    )
                """
                cursor.execute(query, (
                    monedero.banco, 
                    monedero.numero_tarjeta, 
                    monedero.id_banco, 
                    monedero.estatus
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al insertar el monedero: {str(ex)}")

    @classmethod
    def update_monedero(cls, db, monedero):
        """
        Actualiza los datos de un monedero en la base de datos.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE MONEDERO
                    SET 
                        BANCO = ?, 
                        NUMERO_TARJETA = ?, 
                        ID_BANCO = ?, 
                        ESTATUS = ?
                    WHERE ID = ?
                """
                cursor.execute(query, (
                    monedero.banco, 
                    monedero.numero_tarjeta, 
                    monedero.id_banco, 
                    monedero.estatus, 
                    monedero.id
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al actualizar el monedero: {str(ex)}")

    @classmethod
    def get_all_monedero(cls, db):
        """
        Obtiene todos los monederos de la base de datos.
        """
        try:
            with db.cursor() as cursor:
                query = """ SELECT * FROM MONEDERO """
                cursor.execute(query)
                rows = cursor.fetchall()
                monederos = [
                    Monedero(
                        id=row[0],
                        banco=row[1],
                        id_banco=row[2],
                        estatus=row[3],
                        id_empleado=row[4],
                        numero_tarjeta=row[5],
                    ) for row in rows
                ]
                return monederos
        except Exception as ex:
            raise Exception(f"Error al obtener todos los monederos: {str(ex)}")

    @classmethod
    def get_monedero_by_id(cls, db, id):
        """
        Obtiene un monedero por su ID.
        """
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM MONEDERO WHERE ID = ?"""
                cursor.execute(query, (id,))
                row = cursor.fetchone()       
                if row:
                    return Monedero(
                        id=row[0],
                        banco=row[1],
                        id_banco=row[2],
                        estatus=row[3],
                        id_empleado=row[4],
                        numero_tarjeta=row[5],
                    )
        except Exception as ex:
            raise Exception(f"Error al obtener el monedero: {str(ex)}")

    @classmethod
    def get_monedero_disponibles(cls, db):
        """
        Obtiene todos los monederos disponibles (estatus = 0).
        """
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM MONEDERO WHERE ESTATUS = 0"""
                cursor.execute(query)
                rows = cursor.fetchall()
                monederos = []
                for row in rows:
                    monederos.append(Monedero(
                        id=row[0],
                        banco=row[1],
                        id_banco=row[2],
                        estatus=row[3],
                        id_empleado=row[4],
                        numero_tarjeta=row[5],
                    ))
                return monederos
        except Exception as ex:
            raise Exception(f"Error al obtener los monederos disponibles: {str(ex)}")

    @classmethod
    def filter_monedero(cls, db, banco=None, estatus=None, numero_tarjeta=None):
        """
        Filtra monederos según los criterios proporcionados.
        """
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM MONEDERO WHERE 1=1"
                params = []
                
                if banco:
                    query += " AND BANCO LIKE ?"
                    params.append(f'%{banco}%')

                if estatus:
                    query += " AND ESTATUS = ?"
                    params.append(estatus)

                if numero_tarjeta:
                    query += " AND NUMERO_TARJETA LIKE ?"
                    params.append(f'%{numero_tarjeta}%')

                cursor.execute(query, params)
                rows = cursor.fetchall()
                monederos = [
                    Monedero(
                        id=row[0],
                        banco=row[1],
                        id_banco=row[2],
                        estatus=row[3],
                        id_empleado=row[4],
                        numero_tarjeta=row[5],
                    ) for row in rows
                ]
                return monederos
        except Exception as ex:
            raise Exception(f"Error al filtrar los monederos: {str(ex)}")
        
    @classmethod
    def filter_monedero_disponible(cls, db, banco=None, estatus=None, numero_tarjeta=None):
        """
        Filtra monederos según los criterios proporcionados.
        """
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM MONEDERO WHERE 1=1 AND ESTATUS = 0"
                params = []
                
                if banco:
                    query += " AND BANCO LIKE ?"
                    params.append(f'%{banco}%')

                if estatus:
                    query += " AND ESTATUS = ?"
                    params.append(estatus)

                if numero_tarjeta:
                    query += " AND NUMERO_TARJETA LIKE ?"
                    params.append(f'%{numero_tarjeta}%')

                cursor.execute(query, params)
                rows = cursor.fetchall()
                monederos = [
                    Monedero(
                        id=row[0],
                        banco=row[1],
                        id_banco=row[2],
                        estatus=row[3],
                        id_empleado=row[4],
                        numero_tarjeta=row[5],
                    ) for row in rows
                ]
                return monederos
        except Exception as ex:
            raise Exception(f"Error al filtrar los monederos: {str(ex)}")

    @classmethod
    def change_status(cls, db, id, estatus):
        """
        Cambia el estatus de un monedero.
        """
        try:
            with db.cursor() as cursor:
                query = "UPDATE MONEDERO SET ESTATUS = ? WHERE ID = ?"
                cursor.execute(query, (estatus, id))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al cambiar el estatus del monedero: {str(ex)}")

    @classmethod
    def get_monedero_with_conditions(cls, db):
        """
        Obtiene monederos con estatus 0 y ID_EMPLEADO NULL.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT * 
                    FROM MONEDERO 
                    WHERE ESTATUS = 0 AND ID_EMPLEADO IS NULL
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                monederos = [
                    Monedero(
                        id=row[0],
                        banco=row[1],
                        numero_tarjeta=row[2],
                        id_banco=row[3],
                        estatus=row[4],
                        id_empleado=row[5]
                    ) for row in rows
                ]
                return monederos
        except Exception as ex:
            raise Exception(f"Error al obtener monederos con las condiciones: {str(ex)}")

    @classmethod
    def get_monedero_complete_data(cls, db, id):
        """
        Obtiene todos los datos de un monedero por su ID.
        """
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM MONEDERO WHERE ID = ?"""
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    return {
                        "id": row[0],
                        "banco": row[1],
                        "numero_tarjeta": row[2],
                        "id_banco": row[3],
                        "estatus": row[4],
                        "id_empleado": row[5]
                    }
                else:
                    return None
        except Exception as ex:
            raise Exception(f"Error al obtener los datos completos del monedero: {str(ex)}")

    @classmethod
    def update_id_empleado(cls, db, monedero_id, empleado_id):
        """
        Actualiza el campo id_empleado de un monedero.

        Args:
            db: conexión a la base de datos.
            monedero_id: ID del monedero a actualizar.
            empleado_id: Nuevo ID del empleado asociado al monedero.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE MONEDERO
                    SET ID_EMPLEADO = ?
                    WHERE ID = ?
                """
                cursor.execute(query, (empleado_id, monedero_id))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al actualizar el id_empleado del monedero: {str(ex)}")