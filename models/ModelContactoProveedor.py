from .entities.ContactoProveedores import ContactosProveedores

class ModelContactosProveedor:

    @classmethod
    def new_contacto_proveedor(cls, db, contacto_proveedor):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CONTACTOS_PROVEEDORES (
                    ID_PROVEEDOR, NOMBRE, APELLIDO, PUESTO, TELEFONO, CORREO, FECHA_REGISTRO, USUARIO_ID, IS_BLOCKED
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
            cursor.execute(query, (
                contacto_proveedor.id_proveedor,
                contacto_proveedor.nombre,
                contacto_proveedor.apellido,
                contacto_proveedor.puesto,
                contacto_proveedor.telefono,
                contacto_proveedor.correo,
                contacto_proveedor.fecha_registro,
                3,
                contacto_proveedor.is_blocked
            ))
            db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_contacto_proveedor(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM contacto_proveedor"
            cursor.execute(query)
            rows = cursor.fetchall()
            contacto_proveedor = []
            for row in rows:
                contacto_proveedor.append(ContactosProveedores(
                    id=row[0],
                    id_proveedor=row[1],
                    nombre=row[2],
                    apellido=row[3],
                    puesto=row[4],
                    telefono=row[5],
                    correo=row[6],
                    fecha_registro=row[7],
                    usuario=row[8],
                    is_blocked=row[9]
                ))
            return contacto_proveedor
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_contactos_by_proveedor(cls, db, id_proveedor):
        try:
            cursor = db.cursor()
            query = """
                 SELECT  * FROM CONTACTOS_PROVEEDORES WHERE ID_PROVEEDOR = ?;
            """
            cursor.execute(query, (id_proveedor,))
            rows = cursor.fetchall()
            contacto_proveedor = []
            for row in rows:
                contacto_proveedor.append(ContactosProveedores(
                    id=row[0],
                    id_proveedor=row[1],
                    nombre=row[2],
                    apellido=row[3],
                    puesto=row[4],
                    telefono=row[5],
                    correo=row[6],
                    fecha_registro=row[7],
                    usuario=row[8],
                    is_blocked=row[9]
                ))
            return contacto_proveedor
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_contacto_proveedor(cls, db, contacto_proveedor):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CUENTAS_CLIENTES
                SET ID_CLIENTE=?, NOMBRE=?, APELLIDO=?, PUESTO=?, TELEFONO=?, CORREO=?, FECHA_REGISTRO=?, USUARIO=?, IS_BLOCKED=?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                contacto_proveedor.id_cliente,
                contacto_proveedor.nombre,
                contacto_proveedor.apellido,
                contacto_proveedor.puesto,
                contacto_proveedor.telefono,
                contacto_proveedor.correo,
                contacto_proveedor.fecha_registro,
                contacto_proveedor.usuario,
                contacto_proveedor.is_blocked
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    
    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE contacto_proveedor SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_contactos(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM contacto_proveedor"
            cursor.execute(query)
            rows = cursor.fetchall()
            contacto_proveedor = []
            for row in rows:
                contacto_proveedor.append(ContactosProveedores(
                    id=row[0],
                    id_proveedor=row[1],
                    nombre=row[2],
                    apellido=row[3],
                    puesto=row[4],
                    telefono=row[5],
                    correo=row[6],
                    fecha_registro=row[7],
                    usuario=row[8],
                    is_blocked=row[9]
                ))
            return contacto_proveedor
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_contactos_proveedor(cls, db,id):
            try:
                cursor = db.cursor()
                query = "DELETE FROM CONTACTOS_PROVEEDORES WHERE ID_PROVEEDOR = ?;"
                cursor.execute(query, (id))
                db.commit()
            except Exception as ex:
                raise Exception(ex)