from .entities.Banco import Banco

class ModelBanco():

    @classmethod
    def newBanco(self,db,banco):
        try:
            cursor = db.cursor()
            query = """
                    INSERT INTO BANCO (
                    BANCO ) VALUES (?);
                    """
            cursor.execute(query, (
                banco.banco  
                
            ))
            db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_banco(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM BANCO"
            cursor.execute(query)
            rows = cursor.fetchall()
            categorias = []
            for row in rows:
                categorias.append(Banco(
                    id_banco=row[0], banco=row[1], is_blocked=row[2]
                    ))
            return categorias
        except Exception as ex:
            raise Exception(ex)