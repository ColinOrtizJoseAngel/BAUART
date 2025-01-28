from .entities.CuentasClientes import CuentasClientes

class ModelCuentasClientes:

    @classmethod
    def new_cuenta_cliente(cls, db, cuenta_cliente):
        try:
            with db.cursor() as cursor:
                query = """
                    INSERT INTO CUENTAS_CLIENTES (
                        ID_CLIENTE, ID_BANCO, NUMERO_CUENTA, CLABE, FECHA_REGISTRO, IS_BLOCKED
                    ) VALUES (?, ?, ?, ?, ?, ?);
                """
                cursor.execute(query, (
                    cuenta_cliente.id_cliente,
                    cuenta_cliente.id_banco,
                    cuenta_cliente.numero_cuenta,
                    cuenta_cliente.clabe,
                    cuenta_cliente.fecha_registro,
                    
                    cuenta_cliente.is_blocked
                ))
                db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_cuentas_cliente(cls, db,id):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM CUENTAS_CLIENTES WHERE ID_CLIENTE = ?"
                cursor.execute(query,(id))
                rows = cursor.fetchall()
                cuentas_cliente = []
                for row in rows:
                    cuentas_cliente.append(CuentasClientes(
                        id=row[0],
                        id_cliente=row[1],
                        id_banco=row[2],
                        numero_cuenta=row[3],
                        clabe=row[4],
                        fecha_registro=row[5],
                        usuario=row[6],
                        is_blocked=row[7]
                    ))
                return cuentas_cliente
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_cuentas_by_empresa(cls, db, id_cliente):
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT CC.ID, CC.ID_CLIENTE, C.RAZON_SOCIAL, CC.ID_BANCO, CC.NUMERO_CUENTA, CC.CLABE, CC.FECHA_REGISTRO, CC.USUARIO, CC.IS_BLOCKED
                    FROM CUENTAS_CLIENTES CC
                    INNER JOIN CLIENTES C ON CC.ID_CLIENTE = C.ID
                    WHERE CC.ID_CLIENTE = ?;
                """
                cursor.execute(query, (id_cliente,))
                rows = cursor.fetchall()
                cuentas_cliente = []
                for row in rows:
                    cuentas_cliente.append(CuentasClientes(
                        id=row[0],
                        id_cliente=row[1],
                        id_banco=row[3],
                        numero_cuenta=row[4],
                        clabe=row[5],
                        fecha_registro=row[6],
                        usuario=row[7],
                        is_blocked=row[8]
                    ))
                return cuentas_cliente
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_cuenta_empresa(cls, db, cuenta_cliente):
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE CUENTAS_CLIENTES
                    SET ID_CLIENTE = ?, ID_BANCO = ?, NUMERO_CUENTA = ?, CLABE = ?, FECHA_REGISTRO = GETDATE(), USUARIO = ?, IS_BLOCKED = ?
                    WHERE ID = ?;
                """
                cursor.execute(query, (
                    cuenta_cliente.id_cliente,
                    cuenta_cliente.id_banco,
                    cuenta_cliente.numero_cuenta,
                    cuenta_cliente.clabe,
                    cuenta_cliente.fecha_registro,
                    cuenta_cliente.usuario,
                    cuenta_cliente.is_blocked,
                    cuenta_cliente.id_dato_banco
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    
    @classmethod
    def change_status(cls, db, id_cuenta, is_blocked):
        try:
            with db.cursor() as cursor:
                query = "UPDATE CUENTAS_CLIENTES SET IS_BLOCKED = ? WHERE ID = ?"
                cursor.execute(query, (is_blocked, id_cuenta))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_cuentas(cls, db):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM CUENTAS_CLIENTES"
                cursor.execute(query)
                rows = cursor.fetchall()
                cuentas_empresas = []
                for row in rows:
                    cuentas_empresas.append(CuentasClientes(
                        id=row[0],
                        id_cliente=row[1],
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
    def delete_cuentas(cls, db,id):
        try:
            with db.cursor() as cursor:
                query = "DELETE FROM CUENTAS_CLIENTES WHERE ID_CLIENTE = ?;"
                cursor.execute(query, (id))
                db.commit()
        except Exception as ex:
            raise Exception(ex)
