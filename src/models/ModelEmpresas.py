from .entities.Empresas import Empresas

class ModelEmpresas():
     
    @classmethod
    def crearEmpresa(self,db,empresa):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO EMPRESAS (
                    REPSE, RAZON_SOCIAL, RFC,NOREGIS1, NOMBRE_REPRESENTANTE1, APELLIDO_REPRESENTANTE1, TELEFONO_REPRESENTANTE1, CORREO_REPRESENTANTE1, CP,REG_FISCAL,
                    NOMBRE_REPRESENTANTE2, APELLIDO_REPRESENTANTE2, TELEFONO_REPRESENTANTE2, CORREO_REPRESENTANTE2,
                    NOMBRE_APODERADO, APELLIDO_APODERADO, TELEFONO_APODERADO, CORREO_APODERADO, NOREGIS2, NOREGIS3, NOREGIS4,
                    ESTADO, CIUDAD, DIRECCION
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
            cursor.execute(query, (
                empresa.repse, empresa.razon_social,empresa.rfc, empresa.noregis1, empresa.nombre_representante1, empresa.apellido_representante1, empresa.telefono_representante1, empresa.correo_representante1, empresa.cp,
                empresa.reg_fiscal,empresa.nombre_representante2, empresa.apellido_representante2, empresa.telefono_representante2, empresa.correo_representante2,
                empresa.nombre_apoderado, empresa.apellido_apoderado, empresa.telefono_apoderado, empresa.correo_apoderado, empresa.noregis2, empresa.noregis3, empresa.noregis4,
                empresa.estado, empresa.ciudad, empresa.direccion
            ))
            db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_empresas(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM empresas"
            cursor.execute(query)
            rows = cursor.fetchall()
            empresas = []
            for row in rows:
                empresas.append(Empresas(
                    id=row[0], repse=row[1], razon_social=row[2], rfc=row[3], noregis1=row[4], 
                    nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8], cp=row[9],reg_fiscal=row[25],
                    nombre_representante2=row[10], apellido_representante2=row[11], telefono_representante2=row[12], correo_representante2=row[13],
                    nombre_apoderado=row[14], apellido_apoderado=row[15], telefono_apoderado=row[16], correo_apoderado=row[17],
                    noregis2=row[18], noregis3=row[19], noregis4=row[20], estado=row[21], ciudad=row[22], direccion=row[23],is_blocked=row[24] 
                ))
            return empresas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_empresas_not_block(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM empresas WHERE is_blocked = 'False'"
            cursor.execute(query)
            rows = cursor.fetchall()
            empresas = []
            for row in rows:
                empresas.append(Empresas(
                    id=row[0], repse=row[1], razon_social=row[2], rfc=row[3], noregis1=row[4], 
                    nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8], cp=row[9],reg_fiscal=row[25],
                    nombre_representante2=row[10], apellido_representante2=row[11], telefono_representante2=row[12], correo_representante2=row[13],
                    nombre_apoderado=row[14], apellido_apoderado=row[15], telefono_apoderado=row[16], correo_apoderado=row[17],
                    noregis2=row[18], noregis3=row[19], noregis4=row[20], estado=row[21], ciudad=row[22], direccion=row[23],is_blocked=row[24] 
                ))
            return empresas
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def get_empresa_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM empresas WHERE ID_EMPRESA = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Empresas(
                    id=row[0], repse=row[1], razon_social=row[2], rfc=row[3], noregis1=row[4],
                    nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8], cp=row[9],reg_fiscal=row[25],
                    nombre_representante2=row[10], apellido_representante2=row[11], telefono_representante2=row[12], correo_representante2=row[13],
                    nombre_apoderado=row[14], apellido_apoderado=row[15], telefono_apoderado=row[16], correo_apoderado=row[17],
                    noregis2=row[18], noregis3=row[19], noregis4=row[20], estado=row[21], ciudad=row[22], direccion=row[23],is_blocked=row[24] 
                )
            return None
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def get_empresa_last_by_id(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT TOP 1 ID_EMPRESA FROM EMPRESAS ORDER BY ID_EMPRESA DESC;"
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
            cursor = db.cursor()
            query = """
                UPDATE empresas
                SET REPSE = ?, RAZON_SOCIAL = ?, RFC = ?, NOREGIS1 = ?, NOMBRE_REPRESENTANTE1 = ?, APELLIDO_REPRESENTANTE1 = ?, TELEFONO_REPRESENTANTE1 = ?, CORREO_REPRESENTANTE1 = ?, CP = ?, REG_FISCAL = ?,
                    NOMBRE_REPRESENTANTE2 = ?, APELLIDO_REPRESENTANTE2 = ?, TELEFONO_REPRESENTANTE2 = ?, CORREO_REPRESENTANTE2 = ?,
                    NOMBRE_APODERADO = ?, APELLIDO_APODERADO = ?, TELEFONO_APODERADO = ?, CORREO_APODERADO = ?, NOREGIS2 = ?, NOREGIS3 = ?, NOREGIS4 = ?, ESTADO = ?, CIUDAD = ?, DIRECCION = ?
                WHERE ID_EMPRESA = ?;
            """
            cursor.execute(query, (
                empresa.repse, empresa.razon_social, empresa.rfc, empresa.noregis1, empresa.nombre_representante1, empresa.apellido_representante1, empresa.telefono_representante1, empresa.correo_representante1, empresa.cp,
                empresa.reg_fiscal,empresa.nombre_representante2, empresa.apellido_representante2, empresa.telefono_representante2, empresa.correo_representante2,
                empresa.nombre_apoderado, empresa.apellido_apoderado, empresa.telefono_apoderado, empresa.correo_apoderado, empresa.noregis2, empresa.noregis3, empresa.noregis4,
                empresa.estado, empresa.ciudad, empresa.direccion, empresa.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            print(f"ESTE ES EL ESTATUS{is_blocked}")
            cursor = db.cursor()
            query = "UPDATE empresas SET is_blocked = ? WHERE ID_EMPRESA = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    


    # Añadir el método de filtrado en la clase ModelEmpresas
    @classmethod
    def filter_empresas(cls, db, repse, razon_social, rfc, noregis1, cp, estado):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM empresas WHERE 1=1"
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
            if noregis1:
                query += " AND NOREGIS1 LIKE ?"
                params.append(f'%{noregis1}%')
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
                    id=row[0], repse=row[1], razon_social=row[2], rfc=row[3], noregis1=row[4], 
                    nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7],
                    correo_representante1=row[8], cp=row[9],reg_fiscal=[25], nombre_representante2=row[10], apellido_representante2=row[11],
                    telefono_representante2=row[12], correo_representante2=row[13], nombre_apoderado=row[14],
                    apellido_apoderado=row[15], telefono_apoderado=row[16], correo_apoderado=row[17], noregis2=row[18],
                    noregis3=row[19], noregis4=row[20], estado=row[21], ciudad=row[22], direccion=row[23], is_blocked=row[24]
                ))
            cursor.close()
            return empresas
        except Exception as ex:
            raise Exception(ex)