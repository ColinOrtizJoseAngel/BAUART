from .entities.Categoria import Categoria

class ModelCategoria():

    @classmethod
    def alta_categoria(self,db,categoria):
        try:
            cursor = db.cursor()
            query = """
                    INSERT INTO CATEGORIAS (
                    CATEGORIA) VALUES (?);
                    """
            cursor.execute(query, (
                categoria.categoria  
                
            ))
            db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_categorias(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATEGORIAS"
            cursor.execute(query)
            rows = cursor.fetchall()
            categorias = []
            for row in rows:
                categorias.append(Categoria(
                    idCategoria=row[0], categoria=row[1], _is_blocked=row[3]
                    ))
            return categorias
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            print(f"ESTE ES EL ESTATUS{is_blocked}")
            cursor = db.cursor()
            query = "UPDATE CATEGORIAS SET is_blocked = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    
    #ACTUALIAZA CATEGORIA
    @classmethod
    def update_categoria(cls, db, categoria):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CATEGORIAS
                SET CATEGORIA = ?
                WHERE ID = ?;
            """
            print(categoria.idCategoria)
            cursor.execute(query, (
                categoria.categoria,
                categoria.idCategoria
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    #OBTENER CATEGORIA POR ID
    @classmethod
    def get_categoria_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATEGORIAS WHERE ID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Categoria(
                        idCategoria=row[0],
                        categoria=row[1]

                )
            return None
        except Exception as ex:
            raise Exception(ex)
