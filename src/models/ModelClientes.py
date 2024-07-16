from .entities.Clientes import Clientes

class Modelclientes():
     
    @classmethod
    def crearCliente(self, db, cliente):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO Clientes (
                    RazonSocial, RFC, EmpresaID, CP, Estado, Municipio, Pais, Calle, NoExterior, NoInterior, Nombre,
                    Apellido, Telefono, Correo, ResponsableProyecto, TelefonoDirectorio, CorreoDirectorio,
                    TelefonoEmergencia, Puesto, RegimenFiscal, UsoCFDI, FormaPago, DiasCredito, Banco,
                    CuentaBancaria, Clabe 
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
            cursor.execute(query, (
                cliente.razon_social, cliente.rfc, cliente.empresa, cliente.cp, cliente.estado, cliente.municipio, cliente.pais,
                cliente.calle,  cliente.no_Exterior, cliente.no_Interior, cliente.nombre_contacto, cliente.apellido_contacto, 
                cliente.telefono_contacto, cliente.correo_contacto, cliente.responsable_proyecto, cliente.telfono_responsable_proyecto, 
                cliente.correo_responsable_proyecto,cliente.contacto_emergencia, cliente.puesto_empresa, cliente.regimen_fiscal, cliente.uso_cfdi, 
                cliente.forma_pago, cliente.dias_credito, cliente.banco,cliente.cuenta_banco, cliente.clabe
            ))

            db.commit()
    
        except Exception as ex:
            db.rollback()
            raise Exception(ex)


    @classmethod
    def get_all_clientes(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM Clientes"
            cursor.execute(query)
            rows = cursor.fetchall()
            clientes = []
            for row in rows:
                clientes.append(Clientes(
                    id=row[0], razon_social=row[1], rfc=row[2], empresa=row[3], cp=row[4], 
                    estado=row[5], municipio=row[6], pais=row[7], calle=row[8], nombre_contacto=row[11],
                    apellido_contacto=row[12], telefono_contacto=row[13], correo_contacto=row[14], responsable_proyecto=row[15],
                    telfono_responsable_proyecto=row[16], correo_responsable_proyecto=row[17], contacto_emergencia=row[18], puesto_empresa=row[19],
                    regimen_fiscal=row[20], uso_cfdi=row[21], forma_pago=row[23], dias_credito=row[22], banco=row[24], cuenta_banco=row[25],clabe=row[26],
                    no_Exterior = row[9], no_Interior=row[10], is_blocked = row[27]
                ))
            return clientes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_clientes_not_block(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM clientes WHERE is_blocked = 'False'"
            cursor.execute(query)
            rows = cursor.fetchall()
            clientes = []
            for row in rows:
                clientes.append(Clientes(
                    id=row[0], repse=row[1], razon_social=row[2], rfc=row[3], noregis1=row[4], 
                    nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8], cp=row[9],
                    nombre_representante2=row[10], apellido_representante2=row[11], telefono_representante2=row[12], correo_representante2=row[13],
                    nombre_apoderado=row[14], apellido_apoderado=row[15], telefono_apoderado=row[16], correo_apoderado=row[17],
                    noregis2=row[18], noregis3=row[19], noregis4=row[20], estado=row[21], ciudad=row[22], direccion=row[23],is_blocked=row[24] 
                ))
            return clientes
        except Exception as ex:
            raise Exception(ex)
        pass

    @classmethod
    def get_cliente_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM clientes WHERE ClienteID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Clientes(
                    id=row[0], razon_social=row[1], rfc=row[2], empresa=row[3], cp=row[4], 
                    estado=row[5], municipio=row[6], pais=row[7], calle=row[8], nombre_contacto=row[11],
                    apellido_contacto=row[12], telefono_contacto=row[13], correo_contacto=row[14], responsable_proyecto=row[15],
                    telfono_responsable_proyecto=row[16], correo_responsable_proyecto=row[17], contacto_emergencia=row[18], puesto_empresa=row[19],
                    regimen_fiscal=row[20], uso_cfdi=row[21], forma_pago=row[23], dias_credito=row[22], banco=row[24], cuenta_banco=row[25],clabe=row[26],
                    no_Exterior = row[9], no_Interior=row[10], is_blocked = row[27]
                )
            return None
        except Exception as ex:
            raise Exception(ex)
        
    

    @classmethod
    def update_cliente(cls, db, cliente):
        try:
            cursor = db.cursor()
            query = """
                UPDATE clientes
                SET REPSE = ?, RAZON_SOCIAL = ?, RFC = ?, NOREGIS1 = ?, NOMBRE_REPRESENTANTE1 = ?, APELLIDO_REPRESENTANTE1 = ?, TELEFONO_REPRESENTANTE1 = ?, CORREO_REPRESENTANTE1 = ?, CP = ?,
                    NOMBRE_REPRESENTANTE2 = ?, APELLIDO_REPRESENTANTE2 = ?, TELEFONO_REPRESENTANTE2 = ?, CORREO_REPRESENTANTE2 = ?,
                    NOMBRE_APODERADO = ?, APELLIDO_APODERADO = ?, TELEFONO_APODERADO = ?, CORREO_APODERADO = ?, NOREGIS2 = ?, NOREGIS3 = ?, NOREGIS4 = ?, ESTADO = ?, CIUDAD = ?, DIRECCION = ?
                WHERE ID_cliente = ?;
            """
            cursor.execute(query, (
                cliente.repse, cliente.razon_social, cliente.rfc, cliente.noregis1, cliente.nombre_representante1, cliente.apellido_representante1, cliente.telefono_representante1, cliente.correo_representante1, cliente.cp,
                cliente.nombre_representante2, cliente.apellido_representante2, cliente.telefono_representante2, cliente.correo_representante2,
                cliente.nombre_apoderado, cliente.apellido_apoderado, cliente.telefono_apoderado, cliente.correo_apoderado, cliente.noregis2, cliente.noregis3, cliente.noregis4,
                cliente.estado, cliente.ciudad, cliente.direccion, cliente.id
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            print(f"Soy el valor de is blocked {is_blocked}")
            cursor = db.cursor()
            query = "UPDATE Clientes SET is_blocked = ? WHERE ClienteID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    


    # Añadir el método de filtrado en la clase Modelclientes
    @classmethod
    def filter_clientes(cls, db, repse, razon_social, rfc, noregis1, cp, estado):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM clientes WHERE 1=1"
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
            clientes = []
            for row in rows:
                clientes.append(clientes(
                    id=row[0], repse=row[1], razon_social=row[2], rfc=row[3], noregis1=row[4], 
                    nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7],
                    correo_representante1=row[8], cp=row[9], nombre_representante2=row[10], apellido_representante2=row[11],
                    telefono_representante2=row[12], correo_representante2=row[13], nombre_apoderado=row[14],
                    apellido_apoderado=row[15], telefono_apoderado=row[16], correo_apoderado=row[17], noregis2=row[18],
                    noregis3=row[19], noregis4=row[20], estado=row[21], ciudad=row[22], direccion=row[23], is_blocked=row[24]
                ))
            cursor.close()
            return clientes
        except Exception as ex:
            raise Exception(ex)