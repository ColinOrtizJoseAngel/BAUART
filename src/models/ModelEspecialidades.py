from .entities.Especialidades import Especialidades

class ModelEspecialidades:

    @classmethod
    def crearEspecialidad(cls, db, especialidad):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CATALOGO_ESPECIALIDADES (
                    NOMBRE, IS_BLOCKED
                ) VALUES (?, ?)
            """
            cursor.execute(query, (
                especialidad.nombre,
                especialidad.is_blocked
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_especialidades(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_ESPECIALIDADES ORDER BY NOMBRE ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            especialidades = []
            for row in rows:
                especialidades.append(Especialidades(
                    id=row[0],nombre=row[1],fecha_registro=row[2],
                    usuario=row[3],is_blocked=row[4]
                ))
            return especialidades
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_all_especialidades_not_block(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_ESPECIALIDADES WHERE IS_BLOCKED = 0"
            cursor.execute(query)
            rows = cursor.fetchall()
            especialidades = []
            for row in rows:
                especialidades.append(Especialidades(
                    id=row[0],nombre=row[1],fecha_registro=row[2],
                    usuario=row[3],is_blocked=row[4]
                ))
            return especialidades
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_especialidad_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_ESPECIALIDADES WHERE ID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Especialidades(
                    id=row[0], id_proveedor=row[1], especialidad=row[2], fecha_registro=row[3],
                    usuario=row[4], is_blocked=row[5]
                )
            return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_especialidad(cls, db, especialidad):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CATALOGO_ESPECIALIDADES
                SET NOMBRE = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                especialidad.nombre,
                especialidad.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE CATALOGO_ESPECIALIDADES SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def filter_especialidad(cls, db, especialidad=None, estado=None):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CATALOGO_ESPECIALIDADES WHERE 1=1"
            params = []

            if especialidad:
                query += " AND ESPECILIDAD LIKE ?"
                params.append(f'%{especialidad}%')

            if estado:
                if estado == 'activo':
                    query += " AND IS_BLOCKED = 0"
                elif estado == 'bloqueado':
                    query += " AND IS_BLOCKED = 1"

            cursor.execute(query, params)
            rows = cursor.fetchall()
            list_especialidades = []
            for row in rows:
                list_especialidades.append(Especialidades(
                    id=row[0], id_proveedor=row[1], especialidad=row[2], fecha_registro=row[3],
                    usuario=row[4], is_blocked=row[5]
                ))
            cursor.close()
            return list_especialidades
        except Exception as ex:
            raise Exception(ex)
