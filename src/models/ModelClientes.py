from .entities.Clientes import Clientes

class Modelclientes:
     
    @classmethod
    def crearCliente(cls, db, cliente):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CLIENTES (
                    ID_EMPRESA, RAZON_SOCIAL, RFC, CP, ESTADO, CIUDAD, MUNICIPIO, PAIS, CALLE, NO_EXTERIOR,
                    REGIMEN_FISCAL_ID, USO_CFDI_ID, CONDICION_PAGO_ID, FORMA_PAGO_ID, FECHA_REGISTRO, IS_BLOCKED
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
            cursor.execute(query, (
                cliente.id_empresa, cliente.razon_social, cliente.rfc, cliente.cp, cliente.estado, cliente.ciudad, 
                cliente.municipio, cliente.pais, cliente.calle, cliente.no_exterior, cliente.regimen_fiscal_id,
                cliente.uso_cfdi_id, cliente.condicion_pago_id, cliente.forma_pago_id, cliente.fecha_registro,
                cliente.is_blocked
            ))

            db.commit()
    
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_clientes(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CLIENTES"
            cursor.execute(query)
            rows = cursor.fetchall()
            clientes = []
            for row in rows:
                clientes.append(Clientes(
                    id=row[0], id_empresa=row[1], razon_social=row[2], rfc=row[3], cp=row[4], estado=row[5], 
                    ciudad=row[6], municipio=row[7], pais=row[8], calle=row[9], no_exterior=row[10], 
                    regimen_fiscal_id=row[11], uso_cfdi_id=row[12], condicion_pago_id=row[13], forma_pago_id=row[14],
                    fecha_registro=row[15], usuario=row[16], is_blocked=row[17]
                ))
            return clientes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_clientes_not_block(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CLIENTES WHERE IS_BLOCKED = 0"
            cursor.execute(query)
            rows = cursor.fetchall()
            clientes = []
            for row in rows:
                clientes.append(Clientes(
                    id=row[0], id_empresa=row[1], razon_social=row[2], rfc=row[3], cp=row[4], estado=row[5], 
                    ciudad=row[6], municipio=row[7], pais=row[8], calle=row[9], no_exterior=row[10], 
                    regimen_fiscal_id=row[11], uso_cfdi_id=row[12], condicion_pago_id=row[13], forma_pago_id=row[14],
                    fecha_registro=row[15], usuario=row[16], is_blocked=row[17]
                ))
            return clientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_cliente_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CLIENTES WHERE ID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Clientes(
                    id=row[0], id_empresa=row[1], razon_social=row[2], rfc=row[3], cp=row[4], estado=row[5], 
                    ciudad=row[6], municipio=row[7], pais=row[8], calle=row[9], no_exterior=row[10], 
                    regimen_fiscal_id=row[11], uso_cfdi_id=row[12], condicion_pago_id=row[13], forma_pago_id=row[14],
                    fecha_registro=row[15], usuario=row[16], is_blocked=row[17]
                )
            return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_cliente_last_by_id(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT TOP 1 ID FROM CLIENTES ORDER BY ID DESC;"
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                return row[0]
            return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_cliente(cls, db, cliente):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CLIENTES
                SET ID_EMPRESA = ?, RAZON_SOCIAL = ?, RFC = ?, CP = ?, ESTADO = ?, CIUDAD = ?, MUNICIPIO = ?, PAIS = ?, CALLE = ?, 
                    NO_EXTERIOR = ?, REGIMEN_FISCAL_ID = ?, USO_CFDI_ID = ?, CONDICION_PAGO_ID = ?, FORMA_PAGO_ID = ?, FECHA_REGISTRO = ?, 
                    USUARIO_ID = ?, IS_BLOCKED = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                cliente.id_empresa, cliente.razon_social, cliente.rfc, cliente.cp, cliente.estado, cliente.ciudad, 
                cliente.municipio, cliente.pais, cliente.calle, cliente.no_exterior, cliente.regimen_fiscal_id,
                cliente.uso_cfdi_id, cliente.condicion_pago_id, cliente.forma_pago_id, cliente.fecha_registro,
                cliente.usuario, cliente.is_blocked, cliente.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE CLIENTES SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def filter_clientes(cls, db, razon_social, rfc,cp, estado):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CLIENTES WHERE 1=1"
            params = []
            
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
            clientes = []
            for row in rows:
                clientes.append(Clientes(
                    id=row[0], id_empresa=row[1], razon_social=row[2], rfc=row[3], cp=row[4], estado=row[5], 
                    ciudad=row[6], municipio=row[7], pais=row[8], calle=row[9], no_exterior=row[10], 
                    regimen_fiscal_id=row[11], uso_cfdi_id=row[12], condicion_pago_id=row[13], forma_pago_id=row[14],
                    fecha_registro=row[15], usuario=row[16], is_blocked=row[17]
                ))
            cursor.close()
            return clientes
        except Exception as ex:
            raise Exception(ex)
