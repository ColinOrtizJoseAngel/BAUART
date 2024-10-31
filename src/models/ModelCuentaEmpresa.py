from .entities.CuentasEmpresas import CuentasEmpresas

class ModelCuentasEmpresas:

    @classmethod
    def new_cuenta_empresa(cls, db, cuenta_empresa):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CUENTAS_EMPRESAS (
                    ID_EMPRESA, ID_BANCO, NUMERO_CUENTA, CLABE, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED
                ) VALUES (?, ?, ?, ?, ?, ?, ?);
            """
            cursor.execute(query, (
                cuenta_empresa.id_empresa,
                cuenta_empresa.id_banco,
                cuenta_empresa.numero_cuenta,
                cuenta_empresa.clabe,
                cuenta_empresa.fecha_registro,
                cuenta_empresa.usuario,
                cuenta_empresa.is_blocked
            ))
            db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_cuentas_empresas(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CUENTA_EMPRESAS"
            cursor.execute(query)
            rows = cursor.fetchall()
            cuentas_empresas = []
            for row in rows:
                cuentas_empresas.append(CuentasEmpresas(
                    id=row[0],
                    id_empresa=row[1],
                    id_banco=row[3],
                    numero_cuenta=row[4],
                    clabe=row[5],
                    fecha_registro=row[6],
                    usuario=row[7],
                    is_blocked=row[8]
                ))
            return cuentas_empresas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_cuentas_by_empresa(cls, db, id_empresa):
        try:
            cursor = db.cursor()
            query = """
                SELECT CE.ID, CE.ID_EMPRESA, E.RAZON_SOCIAL, CE.ID_BANCO, CE.NUMERO_CUENTA, CE.CLABE, CE.FECHA_REGISTRO, CE.USUARIO, CE.IS_BLOCKED
                FROM CUENTAS_EMPRESAS CE
                INNER JOIN EMPRESAS E ON CE.ID_EMPRESA = E.ID
                WHERE CE.ID_EMPRESA = ?;
            """
            cursor.execute(query, (id_empresa,))
            rows = cursor.fetchall()
            cuentas_empresas = []
            for row in rows:
                cuentas_empresas.append(CuentasEmpresas(
                    id=row[0],
                    id_empresa=row[1],
                    id_banco=row[3],
                    numero_cuenta=row[4],
                    clabe=row[5],
                    fecha_registro=row[6],
                    usuario=row[7],
                    is_blocked=row[8]
                ))
            return cuentas_empresas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_cuenta_empresa(cls, db, cuenta_empresa):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CUENTAS_EMPRESAS
                SET ID_EMPRESA = ?, ID_BANCO = ?, NUMERO_CUENTA = ?, CLABE = ?, FECHA_REGISTRO = ?, USUARIO = ?, IS_BLOCKED = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                cuenta_empresa.id_empresa,
                cuenta_empresa.id_banco,
                cuenta_empresa.numero_cuenta,
                cuenta_empresa.clabe,
                cuenta_empresa.fecha_registro,
                cuenta_empresa.usuario,
                cuenta_empresa.is_blocked,
                cuenta_empresa.id_dato_banco
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    
    @classmethod
    def change_status(cls, db, id_dato_banco, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE CUENTAS_EMPRESAS SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id_dato_banco))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_cuentas(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CUENTAS_EMPRESAS"
            cursor.execute(query)
            rows = cursor.fetchall()
            cuentas_empresas = []
            for row in rows:
                cuentas_empresas.append(CuentasEmpresas(
                    id=row[0],
                    id_empresa=row[1],
                    id_banco=row[2],
                    numero_cuenta=row[3],
                    clabe=row[4],
                    fecha_registro=row[5],
                    usuario=row[6],
                    is_blocked=row[7]
                ))
            return cuentas_empresas
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_cuenta_empresa_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CUENTAS_EMPRESAS WHERE ID_EMPRESA = ?"
            cursor.execute(query, (id,))  # Se pasa el parámetro 'id' como una tupla
            rows = cursor.fetchall()
            
            cuentas_empresas = []
            for row in rows:
                cuentas_empresas.append(CuentasEmpresas(
                    id=row[0],
                    id_empresa=row[1],
                    id_banco=row[2],
                    numero_cuenta=row[3],
                    clabe=row[4],
                    fecha_registro=row[5],
                    usuario=row[6],
                    is_blocked=row[7]
                ))
            return cuentas_empresas
        except Exception as ex:
            raise Exception(f"Error retrieving cuentas_empresas: {ex}")

        

    @classmethod
    def delete_cuentas_empresa(cls, db,id):
        try:
            cursor = db.cursor()
            query = "DELETE FROM CUENTAS_EMPRESAS WHERE ID_EMPRESA = ?;"
            cursor.execute(query, (id))
            db.commit()
        except Exception as ex:
            raise Exception(ex)
