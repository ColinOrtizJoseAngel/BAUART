from .entities.RegistroPatronal import RegistroPatronal

class ModelRegistroPatronal:

    @classmethod
    def newRegistroPatronal(cls, db, registro_patronal):
        try:
            cursor = db.cursor()
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
            cursor = db.cursor()
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
            cursor = db.cursor()
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
            cursor = db.cursor()
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
            cursor = db.cursor()
            query = "UPDATE REGISTRO_PATRONALES SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_registros_patronales(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM REGISTRO_PATRONALES"
            cursor.execute(query)
            rows = cursor.fetchall()
            registrospatronales = []
            for row in rows:
                registrospatronales.append(RegistroPatronal(
                    id_registro=row[0],
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
    def delete_registro_patronales(cls, db,id):
        try:
            cursor = db.cursor()
            query = "DELETE FROM REGISTRO_PATRONALES WHERE ID_EMPRESA = ?;"
            cursor.execute(query, (id))
            db.commit()
        except Exception as ex:
            raise Exception(ex)
