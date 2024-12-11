from .entities.Materiales import Materiales

class ModelMateriales:

    @classmethod
    def crear_material(cls, db, material):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CATALOGO_MATERIALES (
                    CLAVE_ID, UNIDAD_MEDIDA, DESCRIPCION, IS_BLOCKED
                ) VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (
                material.clave_id,
                material.unidad_medida,
                material.descripcion,
                material.is_blocked
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_materiales(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_MATERIALES_FAMILIAS ORDER BY MATERIAL ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            materiales = []
            for row in rows:
                materiales.append(Materiales(
                    id=row[0], clave_id=row[1], descripcion=row[2], unidad_medida=row[3],
                    fecha_registro=row[4], usuario=row[5], is_blocked=row[6]
                ))
            return materiales
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_all_materiales_not_blocked(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_MATERIALES WHERE IS_BLOCKED = 0"
            cursor.execute(query)
            rows = cursor.fetchall()
            materiales = []
            for row in rows:
                materiales.append(Materiales(
                    id=row[0], clave_id=row[1], unidad_medida=row[2], descripcion=row[3],
                    fecha_registro=row[4], usuario=row[5], is_blocked=row[6]
                ))
            return materiales
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_material_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_MATERIALES WHERE ID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Materiales(
                    id=row[0], clave_id=row[1], unidad_medida=row[2], descripcion=row[3],
                    fecha_registro=row[4], usuario=row[5], is_blocked=row[6]
                )
            return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_material(cls, db, material):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CATALOGO_MATERIALES
                SET CLAVE_ID = ?, UNIDAD_MEDIDA = ?, DESCRIPCION = ?, FECHA_REGISTRO = ?, USUARIO_ID = ?, IS_BLOCKED = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                material.clave_id,
                material.unidad_medida,
                material.descripcion,
                material.fecha_registro,
                material.usuario,
                material.is_blocked,
                material.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE CATALOGO_MATERIALES SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def filter_material(cls, db, descripcion=None, estado=None):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_MATERIALES WHERE 1=1"
            params = []

            if descripcion:
                query += " AND DESCRIPCION LIKE ?"
                params.append(f'%{descripcion}%')

            if estado:
                if estado == 'activo':
                    query += " AND IS_BLOCKED = 0"
                elif estado == 'bloqueado':
                    query += " AND IS_BLOCKED = 1"

            cursor.execute(query, params)
            rows = cursor.fetchall()
            list_materiales = []
            for row in rows:
                list_materiales.append(Materiales(
                    id=row[0], clave_id=row[1], unidad_medida=row[2], descripcion=row[3],
                    fecha_registro=row[4], usuario=row[5], is_blocked=row[6]
                ))
            cursor.close()
            return list_materiales
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_material_by_name(cls, db, material_name):
            try:
                cursor = db.cursor()
                # Consulta para buscar el material por su nombre
                query = "SELECT MATERIAL, UNIDAD_MEDIDA FROM CATALOGO_MATERIALES_FAMILIAS WHERE MATERIAL = ? AND IS_BLOCKED = 0"
                cursor.execute(query, (material_name,))
                row = cursor.fetchone()
                # Si se encuentra el material, retornamos un diccionario con los datos
                if row:
                    return {
                        "material": row[0],
                        "unidad_medida": row[1]
                    }
                return None  # Si no se encuentra, retornamos None
            except Exception as ex:
                raise Exception(f"Error al obtener material por nombre: {ex}")