from .entities.Empresas import Empresas

class ModelEmpresas:
     
    @classmethod
    def crearEmpresa(cls, db, empresa):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO EMPRESAS (
                        RAZON_SOCIAL, RFC, REPSE, REGIMEN_FISCAL_ID, NOMBRE_REPRESENTANTE1, APELLIDO_REPRESENTANTE1, TELEFONO_REPRESENTANTE1, CORREO_REPRESENTANTE1, CP, 
                        NOMBRE_REPRESENTANTE2, APELLIDO_REPRESENTANTE2, TELEFONO_REPRESENTANTE2, CORREO_REPRESENTANTE2,
                        NOMBRE_APODERADO, APELLIDO_APODERADO, TELEFONO_APODERADO, CORREO_APODERADO,
                        ESTADO, CIUDAD, DIRECCION, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED,CALLE,NO_EXTERIOR,
                        NO_INTERIOR,MUNICIPIO,PAIS
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?);
                """
                cursor.execute(query, (
                    empresa.razon_social, empresa.rfc, empresa.repse, empresa.regimen_fiscal_id, empresa.nombre_representante1, empresa.apellido_representante1, empresa.telefono_representante1,
                    empresa.correo_representante1, empresa.cp, empresa.nombre_representante2, empresa.apellido_representante2, 
                    empresa.telefono_representante2, empresa.correo_representante2, empresa.nombre_apoderado, empresa.apellido_apoderado, 
                    empresa.telefono_apoderado, empresa.correo_apoderado, empresa.estado, empresa.ciudad, empresa.direccion, 
                    empresa.fecha_registro, empresa.usuario, empresa.is_blocked,empresa.calle, empresa.no_exterior,
                    empresa.no_interior,empresa.municipio,empresa.pais
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_empresas(cls, db):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM EMPRESAS"
                cursor.execute(query)
                rows = cursor.fetchall()
                empresas = []
                for row in rows:
                    empresas.append(Empresas(
                        id=row[0], razon_social=row[1], rfc=row[2],  repse=row[3], regimen_fiscal_id=row[4],
                        nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8],
                        nombre_representante2=row[9], apellido_representante2=row[10], telefono_representante2=row[11], correo_representante2=row[12], nombre_apoderado=row[13],
                        apellido_apoderado=row[14], telefono_apoderado=row[15], correo_apoderado=row[16], cp=row[17],
                        estado=row[18], ciudad=row[19], direccion=row[20], fecha_registro=row[21], usuario=row[22], is_blocked=row[23],calle=row[24],no_exterior=row[25],no_interior=row[26],
                        municipio=row[27],pais=row[28]
                    ))
                return empresas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_empresas_not_block(cls, db):
        try:
            with db.cursor() as cursor:
                
                cursor = db.cursor()
                query = "SELECT * FROM EMPRESAS WHERE is_blocked = 0"
                cursor.execute(query)
                rows = cursor.fetchall()
                empresas = []
                for row in rows:
                    empresas.append(Empresas(
                        id=row[0], razon_social=row[1], rfc=row[2],  repse=row[3], regimen_fiscal_id=row[4],
                        nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8],
                        nombre_representante2=row[9], apellido_representante2=row[10], telefono_representante2=row[11], correo_representante2=row[12], nombre_apoderado=row[13],
                        apellido_apoderado=row[14], telefono_apoderado=row[15], correo_apoderado=row[16], cp=row[17],
                        estado=row[18], ciudad=row[19], direccion=row[20], fecha_registro=row[21], usuario=row[22], is_blocked=row[23],calle=row[24],no_exterior=row[25],no_interior=row[26],
                        municipio=row[27],pais=row[28]
                    ))
                return empresas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_empresa_by_id(cls, db, id):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM EMPRESAS WHERE ID = ?"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    return Empresas(
                        id=row[0], razon_social=row[1], rfc=row[2],  repse=row[3], regimen_fiscal_id=row[4],
                        nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8],
                        nombre_representante2=row[9], apellido_representante2=row[10], telefono_representante2=row[11], correo_representante2=row[12], nombre_apoderado=row[13],
                        apellido_apoderado=row[14], telefono_apoderado=row[15], correo_apoderado=row[16], cp=row[17],
                        estado=row[18], ciudad=row[19], direccion=row[20], fecha_registro=row[21], usuario=row[22], is_blocked=row[23],calle=row[24],no_exterior=row[25],no_interior=row[26],
                        municipio=row[27],pais=row[28]
                    )
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_empresa_last_by_id(cls, db):
        try:
            with db.cursor() as cursor:
                cursor = db.cursor()
                query = "SELECT TOP 1 ID FROM EMPRESAS ORDER BY ID DESC;"
                cursor.execute(query)
                row = cursor.fetchone()
                if row:
                    return row[0]
                return None
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def update_empresa(cls, db, empresa):
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE EMPRESAS
                    SET REPSE = ?, RAZON_SOCIAL = ?, RFC = ?, NOMBRE_REPRESENTANTE1 = ?, APELLIDO_REPRESENTANTE1 = ?, TELEFONO_REPRESENTANTE1 = ?, CORREO_REPRESENTANTE1 = ?, 
                        CP = ?, REGIMEN_FISCAL_ID = ?, NOMBRE_REPRESENTANTE2 = ?, APELLIDO_REPRESENTANTE2 = ?, TELEFONO_REPRESENTANTE2 = ?, CORREO_REPRESENTANTE2 = ?, 
                        NOMBRE_APODERADO = ?, APELLIDO_APODERADO = ?, TELEFONO_APODERADO = ?, CORREO_APODERADO = ?, 
                        ESTADO = ?, CIUDAD = ?, DIRECCION = ?, FECHA_REGISTRO = ?, USUARIO_ID = ?, IS_BLOCKED = ?, CALLE = ?, NO_EXTERIOR = ?,
                        NO_INTERIOR = ?, MUNICIPIO = ?, PAIS = ?
                    WHERE ID = ?;
                """
                cursor.execute(query, (
                    empresa.repse, empresa.razon_social, empresa.rfc, empresa.nombre_representante1, empresa.apellido_representante1, 
                    empresa.telefono_representante1, empresa.correo_representante1, empresa.cp, empresa.regimen_fiscal_id, 
                    empresa.nombre_representante2, empresa.apellido_representante2, empresa.telefono_representante2, empresa.correo_representante2, 
                    empresa.nombre_apoderado, empresa.apellido_apoderado, empresa.telefono_apoderado, empresa.correo_apoderado, 
                    empresa.estado, empresa.ciudad, empresa.direccion, empresa.fecha_registro, empresa.usuario, empresa.is_blocked,empresa.calle,empresa.no_exterior,
                    empresa.no_interior,empresa.municipio,empresa.pais,empresa.id,

    
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error actualizando la empresa: {ex}")
      

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            with db.cursor() as cursor:
                cursor = db.cursor()
                query = "UPDATE EMPRESAS SET is_blocked = ? WHERE ID = ?"
                cursor.execute(query, (is_blocked, id))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def filter_empresas(cls, db, repse, razon_social, rfc, cp, estado):
        try:
            with db.cursor() as cursor:
                cursor = db.cursor()
                query = "SELECT * FROM EMPRESAS WHERE 1=1"
                params = []
                
                if repse:
                    query += " AND REPSE LIKE ?"
                    params.append(f'%{repse}%')
                if razon_social:
                    query += " AND RAZON_SOCIAL LIKE ?"
                    params.append(f'%{razon_social}%')
                if rfc:
                    query += " AND RFC LIKE ?"
                    params.append(f'%{rfc}%')
                if cp:
                    query += " AND CP LIKE ?"
                    params.append(f'%{cp}%')
                
                if estado:
                    if estado == 'activo':
                        query += " AND is_blocked = 0"
                    elif estado == 'bloqueado':
                        query += " AND is_blocked = 1"

                cursor.execute(query, params)
                rows = cursor.fetchall()
                empresas = []
                for row in rows:
                    empresas.append(Empresas(
                        id=row[0], razon_social=row[1], rfc=row[2],  repse=row[3], regimen_fiscal_id=row[4],
                        nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8],
                        nombre_representante2=row[9], apellido_representante2=row[10], telefono_representante2=row[11], correo_representante2=row[12], nombre_apoderado=row[13],
                        apellido_apoderado=row[14], telefono_apoderado=row[15], correo_apoderado=row[16], cp=row[17],
                        estado=row[18], ciudad=row[19], direccion=row[20], fecha_registro=row[21], usuario=row[22], is_blocked=row[23],calle=row[24],no_exterior=row[25],no_interior=row[26],
                        municipio=row[27],pais=row[28]
                    ))
            
                return empresas
        except Exception as ex:
            raise Exception(ex)
