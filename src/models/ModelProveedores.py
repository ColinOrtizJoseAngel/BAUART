from .entities.Proveedores import Proveedores


class ModelProveedores():
     
    @classmethod
    def crear_proveedor(self, db, proveedores):
        try:
            with db.cursor() as cursor:
                # Consulta SQL para insertar el nuevo proveedor
                query_insert = """
                    INSERT INTO PROVEEDORES (
                        ID_EMPRESA, RAZON_SOCIAL, REGIMEN_FISCAL_ID, TIPO_ID, RFC,
                        PAIS, ESTADO, CP, MUNICIPIO, COLONIA, CALLE,
                        NUMERO_EXTERIOR, NUMERO_INTERIOR, FECHA_REGISTRO,
                        USUARIO_ID, IS_BLOCKED
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """
                # Ejecutar la consulta de inserción
                cursor.execute(query_insert, (
                    1, 
                    proveedores.razon_social, 
                    proveedores.regimen_fiscal_id, 
                    proveedores.tipo_id, 
                    proveedores.rfc,
                    proveedores.pais, 
                    proveedores.estado, 
                    proveedores.cp, 
                    proveedores.municipio, 
                    proveedores.colonia, 
                    proveedores.calle,
                    proveedores.numero_exterior, 
                    proveedores.numero_interior, 
                    proveedores.fecha_registro,
                    proveedores.usuario, 
                    proveedores.is_blocked
                ))

            
                db.commit()

                # Consulta SQL para obtener el ID generado
                cursor.execute("SELECT TOP(1) ID  FROM  PROVEEDORES ORDER BY ID DESC;")
                proveedor_id = cursor.fetchone()[0]  # Obtener el valor de SCOPE_IDENTITY()
                
                return proveedor_id  # Retornar el ID del proveedor insertado

        except Exception as ex:
            db.rollback()
            raise Exception(ex)


    
    @classmethod
    def get_proveedor_last_by_id(cls, db):
        try:
            with db.cursor() as cursor:
                query = "SELECT TOP 1 ID FROM PROVEEDORES ORDER BY ID DESC;"
                cursor.execute(query)
                row = cursor.fetchone()
                if row:
                    return row[0]
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_all_proveedores(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM PROVEEDORES ORDER BY ID DESC"
            cursor.execute(query)
            rows = cursor.fetchall()
            lista_proveedores = []
            for row in rows:
                lista_proveedores.append(Proveedores(
                    id=row[0], id_empresa=row[1], razon_social=row[2], regimen_fiscal_id=row[3], tipo_id=row[4], rfc=row[5],
                    pais=row[6], estado=row[7], cp=row[8], municipio=row[9], colonia=row[10],
                    calle=row[11], numero_exterior=row[12], numero_interior=row[13],
                    fecha_registro=row[14], usuario=row[15], is_blocked=row[16]
                ))
            return lista_proveedores
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE PROVEEDORES SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_proveedores_not_blocked(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM PROVEEDORES WHERE IS_BLOCKED = 0"
            cursor.execute(query)
            rows = cursor.fetchall()
            lista_proveedores = []
            for row in rows:
                lista_proveedores.append(Proveedores(
                    id=row[0], id_empresa=row[1], razon_social=row[2], regimen_fiscal_id=row[3], tipo_id=row[4], rfc=row[5],
                    pais=row[6], estado=row[7], cp=row[8], municipio=row[9], colonia=row[10],
                    calle=row[11], numero_exterior=row[12], numero_interior=row[13],
                    fecha_registro=row[14], usuario=row[15], is_blocked=row[16]
                ))
            return lista_proveedores
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_proveedor_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM PROVEEDORES WHERE ID = ?"            
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                proveedor = Proveedores(
                    id=row[0], id_empresa=row[1], razon_social=row[2], regimen_fiscal_id=row[3], tipo_id=row[4], rfc=row[5],
                    pais=row[6], estado=row[7], cp=row[8], municipio=row[9], colonia=row[10],
                    calle=row[11], numero_exterior=row[12], numero_interior=row[13],
                    fecha_registro=row[14], usuario=row[15], is_blocked=row[16]
                )
                return proveedor
            return None
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def update_proveedor(cls, db, proveedor):
        try:
            cursor = db.cursor()
            query = """
                UPDATE PROVEEDORES
                SET ID_EMPRESA = ?, RAZON_SOCIAL = ?, REGIMEN_FISCAL_ID = ?, TIPO_ID = ?, RFC = ?,
                PAIS = ?, ESTADO = ?, CP = ?, MUNICIPIO = ?, COLONIA = ?, CALLE = ?, 
                NUMERO_EXTERIOR = ?, NUMERO_INTERIOR = ?, FECHA_REGISTRO = ?, 
                USUARIO_ID = ?, IS_BLOCKED = ?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                proveedor.id_empresa, proveedor.razon_social, proveedor.regimen_fiscal_id, proveedor.tipo_id, proveedor.rfc,
                proveedor.pais, proveedor.estado, proveedor.cp, proveedor.municipio, proveedor.colonia, proveedor.calle,
                proveedor.numero_exterior, proveedor.numero_interior, proveedor.fecha_registro,
                3, proveedor.is_blocked, proveedor.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def filter_proveedores(cls, db, proveedor, regimen_fiscal, rfc, estado):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM PROVEEDORES WHERE 1=1"
                params = []
                
                if proveedor:
                    query += " AND RAZON_SOCIAL LIKE ?"
                    params.append(f'%{proveedor}%')
                if regimen_fiscal:
                    query += " AND REGIMEN_FISCAL_ID = ?"
                    params.append(regimen_fiscal)
                if rfc:
                    query += " AND RFC LIKE ?"
                    params.append(f'%{rfc}%')
                if estado is not None:
                    if estado == 'activo':
                        query += " AND IS_BLOCKED = 0"
                    elif estado == 'bloqueado':
                        query += " AND IS_BLOCKED = 1"

                cursor.execute(query, params)
                rows = cursor.fetchall()
                lista_proveedores = []
                for row in rows:
                    lista_proveedores.append(Proveedores(
                        id=row[0], id_empresa=row[1], razon_social=row[2], regimen_fiscal_id=row[3], tipo_id=row[4], rfc=row[5],
                        pais=row[6], estado=row[7], cp=row[8], municipio=row[9], colonia=row[10],
                        calle=row[11], numero_exterior=row[12], numero_interior=row[13],
                        fecha_registro=row[14], usuario=row[15], is_blocked=row[16]
                    ))
                
                return lista_proveedores
        except Exception as ex:
            raise Exception(ex)
