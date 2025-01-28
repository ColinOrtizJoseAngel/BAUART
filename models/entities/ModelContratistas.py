from .entities.Contratistas import Contratistas

class Modelcontratistas:
    @classmethod
    def get_all_contratistas(cls, db, id_especialidad):
        try:
            query = """
            SELECT E.ID_ESPECIALIDAD, E.ID_PROVEEDOR, C.NOMBRE, P.RAZON_SOCIAL 
            FROM ESPECIALIDADES_PROVEEDORES E 
            INNER JOIN PROVEEDORES P ON E.ID_PROVEEDOR = P.ID 
            INNER JOIN CATALOGO_ESPECIALIDADES C ON E.ID_ESPECIALIDAD = C.ID 
            WHERE E.ID_ESPECIALIDAD = ?
            """
            
            with db.cursor() as cursor:
                cursor.execute(query, (id_especialidad,))
                rows = cursor.fetchall()
            
            contratistas = []
            for row in rows:
                contratistas.append(Contratistas(
                    id_especialidad=row[0], id_proveedor=row[1], nombre=row[2], razon_social=row[3]
                ))
            return contratistas
        except Exception as ex:
            raise Exception(ex)
