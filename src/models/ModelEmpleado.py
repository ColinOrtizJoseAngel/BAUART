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
                    EDIFICIO, ALCALDIA, MUNICIPIO, REGISTRO_PATRONAL, CUENTA
                ) 
                VALUES (
                    ?, ?, ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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
                    empleado.registro_patronal, empleado.cuenta
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
    def get_all_empleados(cls,db):
        try:
            with db.cursor() as cursor:
                query = """ SELECT * FROM EMPLEADOS"""
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
    def get_empleado_by_id(cls,db,id):
        try:
            with db.cursor() as cursor:
                query = """SELECT * FROM EMPLEADOS WHERE ID = ?"""
                cursor.execute(query, (id,))
                row = cursor.fetchone()       
                if row:
                    return Empleados(
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
                
        except Exception as ex:
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
                        ALTA_EMPLEADO = ?, BAJA_EMPLEADO = ?, IS_BLOCKED = ?
                    WHERE 
                        ID = ?
                """
                cursor.execute(query, (
                    empleado.nombre, empleado.apellido, empleado.id_empresa, empleado.puesto, empleado.tipo_empleado,
                    empleado.tipo_nomina, empleado.sueldo_imss, empleado.monedero, empleado.nomina, empleado.banco,
                    empleado.numero_cuenta, empleado.clabe, empleado.alta_empleado, empleado.baja_empleado, 
                    empleado.is_blocked, empleado.id
                    ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al actualizar el empleado: {str(ex)}")

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
        