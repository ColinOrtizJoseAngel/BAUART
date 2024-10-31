from .entities.Banco import Banco

class ModelBanco:

    @classmethod
    def newBanco(cls, db, banco):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO BANCOS (
                    NOMBRE, FECHA_REGISTRO, IS_BLOCKED
                ) VALUES (?, ?, ?);
            """
            cursor.execute(query, (
                banco.nombre,
                banco.fecha_registro,
                banco.is_blocked
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_bancos(cls, db):
        try:
            with db.cursor() as cursor:  # Usar el contexto 'with' asegura que el cursor se cierre adecuadamente
                query = "SELECT * FROM BANCOS"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                bancos = []
                for row in rows:
                    bancos.append(Banco(
                        id=row[0],
                        nombre=row[1],
                        fecha_registro=row[2],
                        usuario=row[3],
                        is_blocked=row[4]
                    ))
                print(f"Lista de bancos obtenida: {bancos}")
                return bancos
        except Exception as ex:
            raise  #

    @classmethod
    def get_banco_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM BANCOS WHERE ID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Banco(
                    id=row[0],
                    nombre=row[1],
                    fecha_registro=row[2],
                    usuario=row[3],
                    is_blocked=row[4]
                )
            return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_banco(cls, db, banco):
        try:
            cursor = db.cursor()
            query = """
                UPDATE BANCOS
                SET NOMBRE = ?, FECHA_REGISTRO = ?, USUARIO_ID = ?, IS_BLOCKED = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                banco.nombre,
                banco.fecha_registro,
                3,
                banco.is_blocked,
                banco.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    
    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE BANCOS SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_bancos_no_block(cls, db):
        try:
            with db.cursor() as cursor:  # Usar el contexto 'with' asegura que el cursor se cierre adecuadamente
                query = "SELECT * FROM BANCOS WHERE IS_BLOCKED = 0"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                bancos = []
                for row in rows:
                    bancos.append(Banco(
                        id=row[0],
                        nombre=row[1],
                        fecha_registro=row[2],
                        usuario=row[3],
                        is_blocked=row[4]
                    ))
                print(f"Lista de bancos obtenida: {bancos}")
                return bancos
        except Exception as ex:
            raise  #
