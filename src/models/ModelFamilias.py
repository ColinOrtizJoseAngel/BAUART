from .entities.Familias import Familias

class ModelFamilias:

    @classmethod
    def crearFamilia(cls, db, familia):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CATALOGO_FAMILIAS (
                    FAMILIA, IS_BLOCKED
                ) VALUES (?, ?)
            """
            cursor.execute(query, (
                familia.familia,
                familia.is_blocked
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_familias(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_FAMILIAS ORDER BY FAMILIA ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            familias = []
            for row in rows:
                familias.append(Familias(
                    id=row[0], familia=row[1], fecha_registro=row[2], 
                    usuario=row[3], is_blocked=row[4]
                ))
            return familias
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_all_familias_not_block(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_FAMILIAS WHERE IS_BLOCKED = 0"
            cursor.execute(query)
            rows = cursor.fetchall()
            familias = []
            for row in rows:
                familias.append(Familias(
                    id=row[0], familia=row[1], fecha_registro=row[2], 
                    usuario=row[3], is_blocked=row[4]
                ))
            return familias
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_familia_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_FAMILIAS WHERE ID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Familias(
                    id=row[0], familia=row[1], fecha_registro=row[2], 
                    usuario=row[3], is_blocked=row[4]
                )
            return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_familia(cls, db, familia):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CATALOGO_FAMILIAS
                SET FAMILIA = ?, FECHA_REGISTRO = ?, USUARIO = ?, IS_BLOCKED = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                familia.familia,
                familia.fecha_registro,
                familia.usuario,
                familia.is_blocked,
                familia.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE CATALOGO_FAMILIAS SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def filter_familia(cls, db, familia=None, estado=None):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_FAMILIAS WHERE 1=1"
            params = []

            if familia:
                query += " AND FAMILIA LIKE ?"
                params.append(f'%{familia}%')

            if estado:
                if estado == 'activo':
                    query += " AND IS_BLOCKED = 0"
                elif estado == 'bloqueado':
                    query += " AND IS_BLOCKED = 1"

            cursor.execute(query, params)
            rows = cursor.fetchall()
            list_familias = []
            for row in rows:
                list_familias.append(Familias(
                    id=row[0], familia=row[1], fecha_registro=row[2], 
                    usuario=row[3], is_blocked=row[4]
                ))
            cursor.close()
            return list_familias
        except Exception as ex:
            raise Exception(ex)
