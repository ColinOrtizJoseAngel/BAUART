from .entities.RegistroPatronal import RegistroPatronal

class ModelRegistroPatronal:

    @classmethod
    def newRegistroPatronal(cls, db, registro_patronal):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO REGISTRO_PATRONALES (
                        ID_EMPRESA, NUMERO_REGISTRO_PATRONAL, ESTADO, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED
                    ) VALUES (?, ?, ?, ?, ?, ?);
                """
                cursor.execute(query, (
                    registro_patronal.id_empresa,
                    registro_patronal.numero_registro_patronal,
                    registro_patronal.estado,
                    registro_patronal.fecha_registro,
                    registro_patronal.usuario,
                    registro_patronal.is_blocked
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_registroPatronal(cls, db):
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT RP.ID, RP.NUMERO_REGISTRO_PATRONAL, RP.ID_EMPRESA, E.RAZON_SOCIAL, RP.ESTADO, RP.FECHA_REGISTRO, RP.USUARIO_ID, RP.IS_BLOCKED
                    FROM REGISTRO_PATRONALES RP
                    INNER JOIN EMPRESAS E ON RP.ID_EMPRESA = E.ID
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                registrospatronales = []
                for row in rows:
                    registrospatronales.append(RegistroPatronal(
                        id=row[0],
                        id_empresa=row[2],
                        numero_registro_patronal=row[1],
                        estado=row[4],
                        fecha_registro=row[5],
                        usuario=row[6],
                        is_blocked=row[7]
                    ))
                return registrospatronales
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_RegistroPatronal_empresa(cls, db, id_empresa):
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT RP.ID, RP.NUMERO_REGISTRO_PATRONAL, RP.ID_EMPRESA, E.RAZON_SOCIAL, RP.ESTADO, RP.FECHA_REGISTRO, RP.USUARIO_ID, RP.IS_BLOCKED
                    FROM REGISTRO_PATRONALES RP
                    INNER JOIN EMPRESAS E ON RP.ID_EMPRESA = E.ID
                    WHERE RP.ID_EMPRESA = ?;
                """
                cursor.execute(query, (id_empresa,))
                rows = cursor.fetchall()
                registrospatronales = []
                for row in rows:
                    registrospatronales.append(RegistroPatronal(
                        id_registro=row[0],
                        id_empresa=row[2],
                        numero_registro_patronal=row[1],
                        estado=row[4],
                        fecha_registro=row[5],
                        usuario=row[6],
                        is_blocked=row[7]
                    ))
                return registrospatronales
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_registro_patronal(cls, db, registro_patronal):
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE REGISTRO_PATRONALES
                    SET NUMERO_REGISTRO_PATRONAL = ?, ESTADO = ?, USUARIO_ID = ?, IS_BLOCKED = ?
                    WHERE ID = ?;
                """
                cursor.execute(query, (
                    registro_patronal.numero_registro_patronal,
                    registro_patronal.estado,
                    registro_patronal.usuario,
                    registro_patronal.is_blocked,
                    registro_patronal.id_registro,
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    
    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            with db.cursor() as cursor:
                query = "UPDATE REGISTRO_PATRONALES SET IS_BLOCKED = ? WHERE ID = ?"
                cursor.execute(query, (is_blocked, id))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    @classmethod
    def get_all_registros_patronales(cls, db):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM REGISTRO_PATRONALES"
                cursor.execute(query)
                rows = cursor.fetchall()
                registrospatronales = []
                for row in rows:
                    registrospatronales.append(RegistroPatronal(
                        id_registro=row[0],
                        id_empresa=row[1],
                        numero_registro_patronal=row[2],
                        estado=row[3],
                        fecha_registro=row[4],
                        usuario=row[5],
                        is_blocked=row[6]
                    ))
                return registrospatronales
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_registro_patronales(cls, db,id):
        try:
            with db.cursor() as cursor:
                query = "DELETE FROM REGISTRO_PATRONALES WHERE ID_EMPRESA = ?;"
                cursor.execute(query, (id))
                db.commit()
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_registro_patronal_by_empresa(cls, db, id_empresa):
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT ID, ID_EMPRESA, NUMERO_REGISTRO_PATRONAL, ESTADO, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED
                    FROM REGISTRO_PATRONALES 
                    WHERE ID_EMPRESA = ?;
                """
                cursor.execute(query, (id_empresa,))  # <-- Corregí la sintaxis del parámetro
                rows = cursor.fetchall()

                if not rows:
                    return []

                registrospatronales = []
                for row in rows:
                    registrospatronales.append({
                        "id_registro": row[0],
                        "id_empresa": row[1],
                        "numero_registro_patronal": row[2],
                        "estado": row[3],
                        "fecha_registro": row[4],
                        "usuario": row[5],
                        "is_blocked": row[6]
                    })
                return registrospatronales

        except Exception as ex:
            raise Exception(f"Error en la consulta: {str(ex)}")