from .entities.ContactoClientes import ContactosClientes

class ModelContactosClientes:

    @classmethod
    def new_contacto_cliente(cls, db, contacto_cliente):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO CONTACTOS_CLIENTES (
                    ID_CLIENTE, NOMBRE, APELLIDO, PUESTO, TELEFONO, CORREO, FECHA_REGISTRO, IS_BLOCKED
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """
            cursor.execute(query, (
                contacto_cliente.id_cliente,
                contacto_cliente.nombre,
                contacto_cliente.apellido,
                contacto_cliente.puesto,
                contacto_cliente.telefono,
                contacto_cliente.correo,
                contacto_cliente.fecha_registro,
                contacto_cliente.is_blocked
            ))
            db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_contactos_clientes(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CONTACTOS_CLIENTES"
            cursor.execute(query)
            rows = cursor.fetchall()
            contactos_clientes = []
            for row in rows:
                contactos_clientes.append(ContactosClientes(
                    id=row[0],
                    id_cliente=row[1],
                    nombre=row[2],
                    apellido=row[3],
                    puesto=row[4],
                    telefono=row[5],
                    correo=row[6],
                    fecha_registro=row[7],
                    usuario=row[8],
                    is_blocked=row[9]
                ))
            return contactos_clientes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_contactos_by_cliente(cls, db, id_cliente):
        try:
            cursor = db.cursor()
            query = """
                 SELECT CC.ID, CC.ID_CLIENTE, C.RAZON_SOCIAL, CC.NOMBRE, CC.APELLIDO, CC.PUESTO, CC.TELEFONO, CC.CORREO, CC.FECHA_REGISTRO, CC.USUARIO_ID, CC.IS_BLOCKED
                FROM CONTACTOS_CLIENTES CC
                    INNER JOIN CLIENTES C ON CC.ID_CLIENTE = C.ID
                        WHERE CC.ID_CLIENTE = ?;
            """
            cursor.execute(query, (id_cliente,))
            rows = cursor.fetchall()
            contactos_clientes = []
            for row in rows:
                contactos_clientes.append(ContactosClientes(
                    id=row[0],
                    id_cliente=row[1],
                    nombre=row[2],
                    apellido=row[3],
                    puesto=row[4],
                    telefono=row[5],
                    correo=row[6],
                    fecha_registro=row[7],
                    usuario=row[8],
                    is_blocked=row[9]
                ))
            return contactos_clientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_contacto_cliente(cls, db, contacto_cliente):
        try:
            cursor = db.cursor()
            query = """
                UPDATE CUENTAS_CLIENTES
                SET ID_CLIENTE=?, NOMBRE=?, APELLIDO=?, PUESTO=?, TELEFONO=?, CORREO=?, FECHA_REGISTRO=?, USUARIO=?, IS_BLOCKED=?
                WHERE ID = ?;
            """
            cursor.execute(query, (
                contacto_cliente.id_cliente,
                contacto_cliente.nombre,
                contacto_cliente.apellido,
                contacto_cliente.puesto,
                contacto_cliente.telefono,
                contacto_cliente.correo,
                contacto_cliente.fecha_registro,
                contacto_cliente.usuario,
                contacto_cliente.is_blocked
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
    
    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE CONTACTOS_CLIENTES SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    

    @classmethod
    def get_all_contactos(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM CONTACTOS_CLIENTES"
            cursor.execute(query)
            rows = cursor.fetchall()
            contactos_clientes = []
            for row in rows:
                contactos_clientes.append(ContactosClientes(
                    id=row[0],
                    id_cliente=row[1],
                    nombre=row[2],
                    apellido=row[3],
                    puesto=row[4],
                    telefono=row[5],
                    correo=row[6],
                    fecha_registro=row[7],
                    usuario=row[8],
                    is_blocked=row[9]
                ))
            return contactos_clientes
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_contactos(cls, db,id):
        try:
            cursor = db.cursor()
            query = "DELETE FROM CONTACTOS_CLIENTES WHERE ID_CLIENTE = ?;"
            cursor.execute(query, (id))
            db.commit()
        except Exception as ex:
            raise Exception(ex)
