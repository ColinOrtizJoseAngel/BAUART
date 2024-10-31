from .entities.EspecialidadesProveedor import EspecialidadesProveedor

class ModelEspecialidadesProveedor():
     
    @classmethod
    def crear_especialidad_proveedor(self, db, especialidades):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO ESPECIALIDADES_PROVEEDORES (
                    ID_ESPECIALIDAD, ID_PROVEEDOR, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED
                ) VALUES (?, ?, ?, ?, ?);
            """
            cursor.execute(query, (
                especialidades.id_especialidad, 
                especialidades.id_proveedor, 
                especialidades.fecha_registro, 
                especialidades.usuario, 
                especialidades.is_blocked    
            ))

            db.commit()

        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    
    @classmethod
    def get_especialidades_by_proveedor(cls, db, id):
        try:
            cursor = db.cursor()
            query = """
                SELECT EP.ID, EP.ID_PROVEEDOR,EP.ID_ESPECIALIDAD, CE.NOMBRE FROM ESPECIALIDADES_PROVEEDORES EP
                    INNER JOIN CATALOGO_ESPECIALIDADES CE ON EP.ID_ESPECIALIDAD = CE.ID
                WHERE ID_PROVEEDOR = ?
            """
            cursor.execute(query, (id,))
            rows = cursor.fetchall()
            especialidades_proveedor = []
            for row in rows:
                especialidades_proveedor.append(EspecialidadesProveedor(
                   id=row[0],
                   id_proveedor=row[1],
                   id_especialidad=row[2],
                   descripcion=row[3]

                ))
            return especialidades_proveedor
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_especialidades(cls, db,id):
        try:
            cursor = db.cursor()
            query = "DELETE FROM ESPECIALIDADES_PROVEEDORES WHERE ID_PROVEEDOR = ?;"
            cursor.execute(query, (id))
            db.commit()
        except Exception as ex:
            raise Exception(ex)