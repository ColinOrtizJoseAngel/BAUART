from .entities.Puestos import Puesto

class ModelPuesto():
     
    @classmethod
    def crearPuesto(self,db,puesto):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO PUEST (
                    pue_IdCategoria, pue_Puesto, pue_tipoEmpleado,
                    pue_TipoSueldo, pue_sueldo, pue_SueldoDiario,
                    pue_SueldoMensual, pue_SueldoIMSS,
                    pue_SueldoMonedero, pue_HoraExtra
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

            """
            cursor.execute(query, (
                puesto.ent_IdCategoria, puesto.ent_Puesto, puesto.ent_TipoEmpleado,
                puesto.ent_TipoSueldo, puesto.ent_Sueldo, puesto.ent_SueldoDiario,
                puesto.ent_SueldoMensual, puesto.ent_SueldoIMSS, puesto.ent_SueldoMonedero,
                puesto.ent_HoraExtra
            ))

            db.commit()
                    
        except Exception as ex:
                    db.rollback()
                    raise Exception(ex)

    @classmethod
    def get_all_puestos(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM PUEST ORDER BY pue_Puesto ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            dicc_Puestos = []
            for row in rows:
                dicc_Puestos.append(Puesto(
                    ent_IdPuesto=row[0], ent_IdCategoria=row[1], ent_Puesto=row[2], ent_TipoEmpleado=row[3],
                    ent_TipoSueldo=row[4], ent_Sueldo=row[5], ent_SueldoDiario=row[6], ent_SueldoMensual=row[7],
                    ent_SueldoIMSS=row[8], ent_SueldoMonedero=row[9], ent_HoraExtra=row[10], ent_is_blocked=row[11]
                    ))
            return dicc_Puestos
        except Exception as ex:
            raise Exception(ex)

    # Devuelve la categoria del puetso seleccionado en el altaEmpleado.html
    @classmethod
    def get_categoria_by_puesto(cls, db, id_puesto):
        try:
            print("Entro a ModelPuesto.get_categoria_by_puesto")
            cursor = db.cursor()
            query = "SELECT * FROM PUEST WHERE pue_IdPuesto = ?"
            cursor.execute(query, (id_puesto,))
            rows = cursor.fetchall()
            dicc_Categoria = []
            #print(f"{row[0]}")
            for row in rows:
                dicc_Categoria.append(EntPuesto(
                    ent_IdPuesto=row[0], ent_IdCategoria=row[1], ent_Categoria=row[2], ent_Puesto=row[3], 
                    ent_SueldoDiario=row[4], ent_TipoSueldo=row[5], ent_SueldoMensual=row[6], ent_SueldoIMSS=row[7], 
                    ent_SueldoMonedero=row[8], ent_HoraExtra=row[9], ent_is_blocked=row[10],
                    ent_Sueldo=row[11]
                    ))
            return dicc_Categoria
        except Exception as ex:
            raise Exception(ex)
                
    @classmethod
    def get_empresas_not_block(cls, db):
        try:
            cursor = db.cursor()
            #query = "SELECT * FROM empresas WHERE is_blocked = 'False'"
            query = "SELECT * FROM PUEST"
            cursor.execute(query)
            rows = cursor.fetchall()
            empresas = []
            for row in rows:
                empresas.append(EntPuesto(
                    id=row[0], repse=row[1], razon_social=row[2], rfc=row[3], noregis1=row[4], 
                    nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8], cp=row[9],
                    nombre_representante2=row[10], apellido_representante2=row[11], telefono_representante2=row[12], correo_representante2=row[13],
                    nombre_apoderado=row[14], apellido_apoderado=row[15], telefono_apoderado=row[16], correo_apoderado=row[17],
                    noregis2=row[18], noregis3=row[19], noregis4=row[20], estado=row[21], ciudad=row[22], direccion=row[23]
                    #,is_blocked=row[24] 
                ))
            return empresas
        except Exception as ex:
            raise Exception(ex)
        pass

    @classmethod
    def get_empresa_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM empresas WHERE ID_EMPRESA = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return EntPuesto(
                    id=row[0], repse=row[1], razon_social=row[2], rfc=row[3], noregis1=row[4],
                    nombre_representante1=row[5], apellido_representante1=row[6], telefono_representante1=row[7], correo_representante1=row[8], cp=row[9],
                    nombre_representante2=row[10], apellido_representante2=row[11], telefono_representante2=row[12], correo_representante2=row[13],
                    nombre_apoderado=row[14], apellido_apoderado=row[15], telefono_apoderado=row[16], correo_apoderado=row[17],
                    noregis2=row[18], noregis3=row[19], noregis4=row[20], estado=row[21], ciudad=row[22], direccion=row[23],is_blocked=row[24] 
                )
            return None
        except Exception as ex:
            raise Exception(ex)
        
    

    @classmethod
    def update_empresa(cls, db, empresa):
        try:
            cursor = db.cursor()
            query = """
                UPDATE empresas
                SET REPSE = ?, RAZON_SOCIAL = ?, RFC = ?, NOREGIS1 = ?, NOMBRE_REPRESENTANTE1 = ?, APELLIDO_REPRESENTANTE1 = ?, TELEFONO_REPRESENTANTE1 = ?, CORREO_REPRESENTANTE1 = ?, CP = ?,
                    NOMBRE_REPRESENTANTE2 = ?, APELLIDO_REPRESENTANTE2 = ?, TELEFONO_REPRESENTANTE2 = ?, CORREO_REPRESENTANTE2 = ?,
                    NOMBRE_APODERADO = ?, APELLIDO_APODERADO = ?, TELEFONO_APODERADO = ?, CORREO_APODERADO = ?, NOREGIS2 = ?, NOREGIS3 = ?, NOREGIS4 = ?, ESTADO = ?, CIUDAD = ?, DIRECCION = ?
                WHERE ID_EMPRESA = ?;
            """
            cursor.execute(query, (
                empresa.repse, empresa.razon_social, empresa.rfc, empresa.noregis1, empresa.nombre_representante1, empresa.apellido_representante1, empresa.telefono_representante1, empresa.correo_representante1, empresa.cp,
                empresa.nombre_representante2, empresa.apellido_representante2, empresa.telefono_representante2, empresa.correo_representante2,
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
            query = "UPDATE Puesto SET pue_is_blocked = ? WHERE pue_IdPuesto = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex) 


    # Añadir el método de filtrado en la clase ModelEmpresas
    @classmethod
    def filter_puesto(cls, db, categoria, IdCategoria, Categoria, Puesto, SueldoDiario, TipoSueldo, SueldoMensual, SueldoIMSS, SueldoMonedero, HoraExtra):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM Puesto"
            params = []
            
            if Puesto:
                query += " AND pue_Puesto LIKE ?"
                params.append(f'%{Puesto}%')

            cursor.execute(query, params)
            rows = cursor.fetchall()
            list_puesto = []
            for row in rows:
                # Ocupa la entidad "Bancos" para cargarle los datos obtenidos en la consulta, "EntBancos" a su vez
                # es agregado a la varibale "list_bancos" y es retornado como valor
                list_puesto.append(EntPuesto(
                    ent_IdPuesto=row[0], ent_IdCategoria=row[1], ent_Puesto=row[2], ent_TipoEmpleado=row[3],
                    ent_TipoSueldo=row[4], ent_Sueldo=row[5], ent_SueldoDiario=row[6], ent_SueldoMensual=row[7],
                    ent_SueldoIMSS=row[8], ent_SueldoMonedero=row[9], ent_HoraExtra=row[10],
                ))
            cursor.close()
            return list_puesto
        except Exception as ex:
            raise Exception(ex)