from .entities.CuentasProveedor import CuentasProveedor

class ModelCuentasProveedor:

    @classmethod
    def new_cuenta_proveedor(cls, db, cuenta_proveedor):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CUENTAS_PROVEEDORES (
                    ID_PROVEEDOR, ID_BANCO, NUMERO_CUENTA, CLABE, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED
                ) VALUES (?, ?, ?, ?, ?, ?, ?);
            """
            cursor.execute(query, (
                cuenta_proveedor.id_proveedor,
                cuenta_proveedor.id_banco,
                cuenta_proveedor.numero_cuenta,
                cuenta_proveedor.clabe,
                cuenta_proveedor.fecha_registro,
                3,
                cuenta_proveedor.is_blocked
            ))
            db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_cuentas_empresas(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CUENTAS_PROVEEDORES"
            cursor.execute(query)
            rows = cursor.fetchall()
            cuentas_empresas = []
            for row in rows:
                cuentas_empresas.append(CuentasProveedor(
                    id=row[0],
                    id_proveedor=row[1],
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
    def get_cuentas_by_proeveedor(cls, db, id_proveedor):
        try:
            cursor = db.cursor()
            query = """
                 SELECT * FROM CUENTAS_PROVEEDORES WHERE ID_PROVEEDOR = ?;
            """
            cursor.execute(query, (id_proveedor,))
            rows = cursor.fetchall()
            cuentas_empresas = []
            for row in rows:
                cuentas_empresas.append(CuentasProveedor(
                    id=row[0],
                    id_proveedor=row[1],
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
    def update_cuenta_proveedor(cls, db, cuenta_proveedor):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CUENTAS_PROVEEDORES
                SET ID_PROVEEDOR  = ?, ID_BANCO = ?, NUMERO_CUENTA = ?, CLABE = ?, FECHA_REGISTRO = ?, USUARIO = ?, IS_BLOCKED = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                cuenta_proveedor.id_empresa,
                cuenta_proveedor.id_banco,
                cuenta_proveedor.numero_cuenta,
                cuenta_proveedor.clabe,
                cuenta_proveedor.fecha_registro,
                cuenta_proveedor.usuario,
                cuenta_proveedor.is_blocked,
                cuenta_proveedor.id_dato_banco
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
                cuentas_empresas.append(CuentasProveedor(
                    id=row[0],
                    id_proveedor=row[1],
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
    def delete_cuentas_proveedor(cls, db,id):
                try:
                    cursor = db.cursor()
                    query = "DELETE FROM CUENTAS_PROVEEDORES WHERE ID_PROVEEDOR = ?;"
                    cursor.execute(query, (id))
                    db.commit()
                except Exception as ex:
                    raise Exception(ex)   