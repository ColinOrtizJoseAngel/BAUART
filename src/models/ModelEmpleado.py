from .entities.Empleados import Empleados

class ModelEmpleado:

    @classmethod
    def alta_empleado(cls, db, empleado):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO EMPLEADOS (
                    NOMBRE, APELLIDO, ID_EMPRESA, PUESTO, TIPO_EMPLEADO, 
                    TIPO_NOMINA, SUELDO_IMSS, MONEDERO, NOMINA, BANCO, 
                    NUMERO_CUENTA, CLABE, ALTA_EMPLEADO, BAJA_EMPLEADO, 
                    FECHA_REGISTRO, IS_BLOCKED, CATEGORIA, NO_IMSS, CURP, INE, 
                    RFC, CEDULA_PROFESIONAL, ESTADO_CIVIL, FECHA_NACIMIENTO, TELEFONO_CONTACTO, 
                    DOMICILIO, TOPE_HORAS_EXTRA, FOTO_BASE64, TIPO_SANGRE,
                    LUGAR_NACIMIENTO, SEXO, CALLE, MANZANA, LOTE, NUMERO_EXTERIOR, 
                    NUMERO_INTERIOR, COLONIA, CODIGO_POSTAL, ESTADO, TELEFONO_DOMICILIO,
                    CUENTA_CORREO, SALARIO_DIARIO_INTEGRADO, NUMERO_CREDITO_INFONAVIT, 
                    TIPO_DESCUENTO_INFONAVIT, FACTOR_INFONAVIT, FECHA_INGRESO, 
                    TURNO, TIPO_CONTRATO, CONTACTO_ACCIDENTE, ALERGIAS, ENFERMEDADES_CONTROLADAS,
                    EDIFICIO, ALCALDIA, MUNICIPIO, REGISTRO_PATRONAL, CUENTA, CONTRATABLE, OBSERVACIONES
                ) 
                VALUES (
                    ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
                """
                cursor.execute(query, (
                    empleado.nombre, empleado.apellido, empleado.id_empresa, empleado.puesto, empleado.tipo_empleado,
                    empleado.tipo_nomina, empleado.sueldo_imss, empleado.monedero, empleado.nomina, empleado.banco,
                    empleado.numero_cuenta, empleado.clabe, empleado.alta_empleado, empleado.baja_empleado,
                    empleado.fecha_registro, empleado.is_blocked, empleado.categoria, empleado.no_imss, empleado.curp, empleado.ine,
                    empleado.rfc, empleado.cedula_profesional, empleado.estado_civil, empleado.fecha_nacimiento,
                    empleado.telefono_contacto, empleado.domicilio, empleado.tope_horas_extra, empleado.foto_base64,
                    empleado.tipo_sangre, empleado.lugar_nacimiento, empleado.sexo, empleado.calle, empleado.manzana,
                    empleado.lote, empleado.numero_exterior, empleado.numero_interior, empleado.colonia, empleado.codigo_postal,
                    empleado.estado, empleado.telefono_domicilio, empleado.cuenta_correo, empleado.salario_diario_integrado,
                    empleado.numero_credito_infonavit, empleado.tipo_descuento_infonavit, empleado.factor_infonavit,
                    empleado.fecha_ingreso, empleado.turno, empleado.tipo_contrato, empleado.contacto_accidente,
                    empleado.alergias, empleado.enfermedades_controladas, empleado.edificio, empleado.alcaldia, empleado.municipio,
                    empleado.registro_patronal, empleado.cuenta, empleado.contratable, empleado.observaciones
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_empleados(cls, db):
        try:
            with db.cursor() as cursor:
                query = """ SELECT * FROM EMPLEADOS """
                cursor.execute(query)
                rows = cursor.fetchall()
                empleados = []
                for row in rows:
                    empleados.append(Empleados(*row))
                return empleados
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_empleados_por_categoria(cls, db, categoria):
        """
        Obtiene los empleados que pertenecen a la categoría seleccionada en la nómina presupuestada.
        """
        try:
            with db.cursor() as cursor:
                query = """ 
                SELECT * FROM EMPLEADOS 
                WHERE categoria = ?
                """
                cursor.execute(query, (categoria,))
                rows = cursor.fetchall()
                empleados = [Empleados(*row) for row in rows]
                return empleados
        except Exception as ex:
            raise Exception(f"Error al obtener empleados por categoría: {ex}")
    
    @classmethod
    def get_empleado_by_id(cls, db, id):
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM EMPLEADOS WHERE ID = ?"""
                cursor.execute(query, (id,))
                row = cursor.fetchone()

                print("🔍 Datos obtenidos de la DB:", row)  # Debug para ver el orden

                if row:
                    return Empleados(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        id_empresa=row[3],
                        puesto=row[4],
                        tipo_empleado=row[5],
                        tipo_nomina=row[6],
                        monedero=row[7],   
                        nomina=row[8],
                        banco=row[9],
                        clabe=row[10],
                        alta_empleado=row[11],
                        baja_empleado=row[12],
                        fecha_registro=row[13],
                        is_blocked=row[14],
                        categoria=row[15],
                        no_imss=row[16],
                        curp=row[17],
                        ine=row[18],
                        rfc=row[19],
                        cedula_profesional=row[20],
                        estado_civil=row[21],
                        fecha_nacimiento=row[22],
                        telefono_contacto=row[23], 
                        domicilio=row[24],  
                        tope_horas_extra=row[25],  
                        numero_cuenta=row[26],
                        sueldo_imss=row[27],
                        foto_base64=row[28],
                        tipo_sangre=row[29],
                        lugar_nacimiento=row[30],
                        sexo=row[31],
                        calle=row[32],
                        manzana=row[33],
                        lote=row[34],
                        numero_exterior=row[35],
                        numero_interior=row[36],
                        colonia=row[37],
                        codigo_postal=row[38],
                        estado=row[39],
                        telefono_domicilio=row[40],
                        cuenta_correo=row[41],
                        salario_diario_integrado=row[42],
                        numero_credito_infonavit=row[43],
                        tipo_descuento_infonavit=row[44],
                        factor_infonavit=row[45],
                        fecha_ingreso=row[46],
                        turno=row[47],
                        tipo_contrato=row[48],
                        contacto_accidente=row[49],
                        alergias=row[50],
                        enfermedades_controladas=row[51],
                        edificio=row[52],
                        alcaldia=row[53],
                        municipio=row[54],
                        cuenta=row[55],  
                        registro_patronal=row[56],  
                        motivo_baja=row[57],
                        id_monedero=row[58],
                        contratable=row[59],
                        observaciones=row[60]
                    )
        except Exception as ex:
            print(f"❌ Error en get_empleado_by_id: {ex}")
            raise Exception(ex)



    @classmethod
    def update_empleado(cls, db, empleado):
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE EMPLEADOS
                    SET 
                        NOMBRE = ?, APELLIDO = ?, ID_EMPRESA = ?, PUESTO = ?, 
                        TIPO_EMPLEADO = ?, TIPO_NOMINA = ?, SUELDO_IMSS = ?, MONEDERO = ?, 
                        NOMINA = ?, BANCO = ?, NUMERO_CUENTA = ?, CLABE = ?, 
                        ALTA_EMPLEADO = ?, BAJA_EMPLEADO = ?, FECHA_REGISTRO = ?, IS_BLOCKED = ?, 
                        CATEGORIA = ?, NO_IMSS = ?, CURP = ?, INE = ?, RFC = ?, 
                        CEDULA_PROFESIONAL = ?, ESTADO_CIVIL = ?, FECHA_NACIMIENTO = ?, 
                        TELEFONO_CONTACTO = ?, DOMICILIO = ?, TOPE_HORAS_EXTRA = ?, 
                        FOTO_BASE64 = ?, TIPO_SANGRE = ?, LUGAR_NACIMIENTO = ?, SEXO = ?, 
                        CALLE = ?, MANZANA = ?, LOTE = ?, NUMERO_EXTERIOR = ?, 
                        NUMERO_INTERIOR = ?, COLONIA = ?, CODIGO_POSTAL = ?, ESTADO = ?, 
                        TELEFONO_DOMICILIO = ?, CUENTA_CORREO = ?, SALARIO_DIARIO_INTEGRADO = ?, 
                        NUMERO_CREDITO_INFONAVIT = ?, TIPO_DESCUENTO_INFONAVIT = ?, 
                        FACTOR_INFONAVIT = ?, FECHA_INGRESO = ?, TURNO = ?, 
                        TIPO_CONTRATO = ?, CONTACTO_ACCIDENTE = ?, ALERGIAS = ?, 
                        ENFERMEDADES_CONTROLADAS = ?, EDIFICIO = ?, ALCALDIA = ?, 
                        MUNICIPIO = ?, REGISTRO_PATRONAL = ?, CUENTA = ?, 
                        MOTIVO_BAJA = ?, ID_MONEDERO = ?, CONTRATABLE = ?, OBSERVACIONES = ?
                    WHERE 
                        ID = ?
                """
                cursor.execute(query, (
                    empleado.nombre, empleado.apellido, empleado.id_empresa, empleado.puesto, 
                    empleado.tipo_empleado, empleado.tipo_nomina, empleado.sueldo_imss, empleado.monedero, 
                    empleado.nomina, empleado.banco, empleado.numero_cuenta, empleado.clabe, 
                    empleado.alta_empleado, empleado.baja_empleado, empleado.fecha_registro, empleado.is_blocked, 
                    empleado.categoria, empleado.no_imss, empleado.curp, empleado.ine, empleado.rfc, 
                    empleado.cedula_profesional, empleado.estado_civil, empleado.fecha_nacimiento, 
                    empleado.telefono_contacto, empleado.domicilio, empleado.tope_horas_extra, 
                    empleado.foto_base64, empleado.tipo_sangre, empleado.lugar_nacimiento, empleado.sexo, 
                    empleado.calle, empleado.manzana, empleado.lote, empleado.numero_exterior, 
                    empleado.numero_interior, empleado.colonia, empleado.codigo_postal, empleado.estado, 
                    empleado.telefono_domicilio, empleado.cuenta_correo, empleado.salario_diario_integrado, 
                    empleado.numero_credito_infonavit, empleado.tipo_descuento_infonavit, empleado.factor_infonavit, 
                    empleado.fecha_ingreso, empleado.turno, empleado.tipo_contrato, empleado.contacto_accidente, 
                    empleado.alergias, empleado.enfermedades_controladas, empleado.edificio, empleado.alcaldia, 
                    empleado.municipio, empleado.registro_patronal, empleado.cuenta, empleado.motivo_baja, 
                    empleado.id_monedero, empleado.contratable, empleado.observaciones, empleado.id
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al actualizar el empleado: {str(ex)}")


    @classmethod
    def update_id_monedero(cls, db, empleado_id, new_id_monedero):
        """
        Actualiza solo el campo id_monedero para un empleado en la base de datos.

        Args:
            db: conexión a la base de datos.
            empleado_id: ID del empleado cuyo id_monedero se actualizará.
            new_id_monedero: Nuevo valor para el id_monedero.
        """
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE EMPLEADOS
                    SET ID_MONEDERO = ?
                    WHERE ID = ?
                """
                cursor.execute(query, (new_id_monedero, empleado_id))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al actualizar id_monedero: {str(ex)}")
        
    @classmethod
    def filter_empleados(cls, db, nombre, apellido,tipo_empleado, estado):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM EMPLEADOS WHERE 1=1"
                params = []
                
                if nombre:
                    query += " AND NOMBRE LIKE ?"
                    params.append(f'%{nombre}%')
                if apellido:
                    query += " AND APELLIDO LIKE ?"
                    params.append(f'%{apellido}%')

                if tipo_empleado:
                    query += " AND TIPO_EMPLEADO LIKE ?"
                    params.append(f'%{tipo_empleado}%')
               
                    
                if estado:
                    if estado == '0':
                        query += " AND is_blocked = 0"
                    elif estado == '1':
                        query += " AND is_blocked = 1"
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                empleados = []
                for row in rows:
                    empleados.append(Empleados(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        id_empresa=row[3],
                        puesto=row[4],
                        tipo_empleado=row[5],
                        tipo_nomina=row[6],
                        sueldo_imss=row[7],
                        monedero=row[8],
                        nomina=row[9],
                        banco=row[10],
                        numero_cuenta=row[11],
                        clabe=row[12],
                        alta_empleado=row[13],
                        baja_empleado=row[14],
                        fecha_registro=row[15],
                        is_blocked=row[16]
                    ))
                return empleados
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            cursor = db.cursor()
            query = "UPDATE EMPLEADOS SET IS_BLOCKED = ? WHERE ID = ?"
            cursor.execute(query, (is_blocked, id))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        

    @classmethod
    def obtener_directores(cls,db):
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM EMPLEADOS WHERE PUESTO = 39"""
                cursor.execute(query)
                rows = cursor.fetchall()
                empleados = []
                for row in rows:
                    empleados.append(Empleados(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        id_empresa=row[3],
                        puesto=row[4],
                        tipo_empleado=row[5],
                        tipo_nomina=row[6],
                        sueldo_imss=row[7],
                        monedero=row[8],
                        nomina=row[9],
                        banco=row[10],
                        numero_cuenta=row[11],
                        clabe=row[12],
                        alta_empleado=row[13],
                        baja_empleado=row[14],
                        fecha_registro=row[15],
                        is_blocked=row[16]
                    ))
                return empleados
        
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def obtener_lideres(cls,db):
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM EMPLEADOS WHERE PUESTO = 40"""
                cursor.execute(query)
                rows = cursor.fetchall()
                empleados = []
                for row in rows:
                    empleados.append(Empleados(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        id_empresa=row[3],
                        puesto=row[4],
                        tipo_empleado=row[5],
                        tipo_nomina=row[6],
                        sueldo_imss=row[7],
                        monedero=row[8],
                        nomina=row[9],
                        banco=row[10],
                        numero_cuenta=row[11],
                        clabe=row[12],
                        alta_empleado=row[13],
                        baja_empleado=row[14],
                        fecha_registro=row[15],
                        is_blocked=row[16]
                    ))
                return empleados
        
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def obtener_gerentes(cls,db):
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM EMPLEADOS WHERE PUESTO = 41"""
                cursor.execute(query)
                rows = cursor.fetchall()
                empleados = []
                for row in rows:
                    empleados.append(Empleados(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        id_empresa=row[3],
                        puesto=row[4],
                        tipo_empleado=row[5],
                        tipo_nomina=row[6],
                        sueldo_imss=row[7],
                        monedero=row[8],
                        nomina=row[9],
                        banco=row[10],
                        numero_cuenta=row[11],
                        clabe=row[12],
                        alta_empleado=row[13],
                        baja_empleado=row[14],
                        fecha_registro=row[15],
                        is_blocked=row[16]
                    ))
                return empleados
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def obtener_director_por_id(cls,db,id):
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM EMPLEADOS WHERE ID = ?"""
                cursor.execute(query,(id,))
                row = cursor.fetchone()
                
                director = Empleados(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        id_empresa=row[3],
                        puesto=row[4],
                        tipo_empleado=row[5],
                        tipo_nomina=row[6],
                        sueldo_imss=row[7],
                        monedero=row[8],
                        nomina=row[9],
                        banco=row[10],
                        numero_cuenta=row[11],
                        clabe=row[12],
                        alta_empleado=row[13],
                        baja_empleado=row[14],
                        fecha_registro=row[15],
                        is_blocked=row[16]
                    )
                return director
        
        except Exception as ex:
            raise Exception(ex)