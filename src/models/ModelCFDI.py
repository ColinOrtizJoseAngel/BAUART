from .entities.UsoCFDI import UsoCFDI

class ModelCFDI:

    @classmethod
    def get_all_usoCFDI(cls,db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM USOCFDI"
            cursor.execute(query)
            rows = cursor.fetchall()
            uso_CFDI = []
            for row in rows:
                uso_CFDI.append(UsoCFDI(
                        id=row[0],
                        clave=row[1],
                        descripcion=row[2].upper(),
                        aplicacion=row[3]
                    ))
            return uso_CFDI
        except Exception as ex:
            raise Exception(ex)

    
    @classmethod
    def get_cfdi_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM USOCFDI WHERE ID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return UsoCFDI(
                        id=row[0],
                        clave=row[1],
                        descripcion=row[2],
                        aplicacion=row[3]
                    )
            return None
        except Exception as ex:
            raise Exception(ex)