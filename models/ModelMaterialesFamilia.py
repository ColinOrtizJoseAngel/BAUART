from .entities.MaterialesFamilia import MaterialesFamilia

class ModelMaterialesFamilia:

    @classmethod
    def crear_material_familia(cls, db, material_familia):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CATALOGO_MATERIALES_FAMILIAS (
                    ID_FAMILIA,MATERIAL,UNIDAD_MEDIDA, IS_BLOCKED
                ) VALUES (?, ?, ?,?)
            """
            cursor.execute(query, (
                material_familia.id_familia,
                material_familia.material,
                material_familia.unidad_medida,
                material_familia.is_blocked
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_materiales_familia(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT MATERIALES.ID, MATERIALES.ID_FAMILIA, MATERIALES.MATERIAL, MATERIALES.UNIDAD_MEDIDA, MATERIALES.FECHA_REGISTRO, MATERIALES.USUARIO_ID, MATERIALES.IS_BLOCKED, FAMILIAS.FAMILIA FROM CATALOGO_MATERIALES_FAMILIAS AS MATERIALES INNER JOIN CATALOGO_FAMILIAS AS FAMILIAS ON MATERIALES.ID_FAMILIA = FAMILIAS.ID"
            cursor.execute(query)
            rows = cursor.fetchall()
            materiales_familia = []
            for row in rows:
                materiales_familia.append(MaterialesFamilia(
                    id=row[0], id_familia=row[1], material=row[2],unidad_medida=row[3],
                    fecha_registro=row[4], usuario=row[5], is_blocked=row[6],familia=row[7]
                ))
            return materiales_familia
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_materiales_by_familia(cls, db, id_familia):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_MATERIALES_FAMILIAS WHERE ID_FAMILIA = ?"
            cursor.execute(query, (id_familia,))
            rows = cursor.fetchall()
            materiales_familia = []
            for row in rows:
                materiales_familia.append(MaterialesFamilia(
                    id=row[0], id_familia=row[1], material=row[2],unidad_medida=row[3],
                    fecha_registro=row[4], usuario=row[5], is_blocked=row[6]
                ))
            return materiales_familia
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_familias_by_material(cls, db, id_material):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_MATERIALES_FAMILIAS WHERE MATERIAL = ?"
            cursor.execute(query, (id_material,))
            rows = cursor.fetchall()
            familias_material = []
            for row in rows:
                familias_material.append(MaterialesFamilia(
                   id=row[0], id_familia=row[1], material=row[2],unidad_medida=row[3],
                    fecha_registro=row[4], usuario=row[5], is_blocked=row[6]
                ))
            return familias_material
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_material_familia(cls, db, material_familia):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CATALOGO_MATERIALES_FAMILIAS
                SET ID_FAMILIA = ?, MATERIAL = ?, FECHA_REGISTRO = ?, USUARIO_ID = ?, IS_BLOCKED = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                material_familia.id_familia,
                material_familia.material,
                material_familia.fecha_registro,
                material_familia.usuario,
                material_familia.is_blocked,
                material_familia.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE CATALOGO_MATERIALES_FAMILIAS SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def filter_material_familia(cls, db, id_familia=None, id_material=None, estado=None):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_MATERIALES_FAMILIAS WHERE 1=1"
            params = []

            if id_familia:
                query += " AND ID_FAMILIA = ?"
                params.append(id_familia)

            if id_material:
                query += " AND ID_MATERIAL = ?"
                params.append(id_material)

            if estado:
                if estado == 'activo':
                    query += " AND IS_BLOCKED = 0"
                elif estado == 'bloqueado':
                    query += " AND IS_BLOCKED = 1"

            cursor.execute(query, params)
            rows = cursor.fetchall()
            list_materiales_familia = []
            for row in rows:
                list_materiales_familia.append(MaterialesFamilia(
                  id=row[0], id_familia=row[1], material=row[2],unidad_medida=row[3],
                    fecha_registro=row[4], usuario=row[5], is_blocked=row[6]
                ))
            cursor.close()
            return list_materiales_familia
        except Exception as ex:
            raise Exception(ex)
