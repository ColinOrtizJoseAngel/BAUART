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
                    FECHA_REGISTRO, IS_BLOCKED
                ) 
                VALUES (
                    ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?
                )
                """
                cursor.execute(query, (
                    empleado.nombre, empleado.apellido, empleado.id_empresa, empleado.puesto, empleado.tipo_empleado,
                    empleado.tipo_nomina, empleado.sueldo_imss, empleado.monedero, empleado.nomina, empleado.banco,
                    empleado.numero_cuenta, empleado.clabe, empleado.alta_empleado, empleado.baja_empleado,
                    empleado.fecha_registro, empleado.is_blocked
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
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
        