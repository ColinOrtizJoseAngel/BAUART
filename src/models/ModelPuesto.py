from .entities.Puestos import Puesto

class ModelPuesto():
     
    @classmethod
    def alta_puesto(cls,db,puesto):
        try:
            
            with db.cursor() as cursor:
                query = """
                    INSERT INTO PUESTOS (PUESTO, SUELDO_BASE, SUELDO_TARJETA,
                        HORA_EXTRA, FECHA_REGISTRO, CATEGORIA, IS_BLOCKED)
                    VALUES (?, ?, ?, ?, GETDATE(), ?, ?)
                """
                cursor.execute(query, (
                    puesto.puesto,
                    puesto.sueldo_base,
                    puesto.sueldo_tarjeta,
                    puesto.horas_extras,
                    puesto.categoria,
                    puesto.is_blocked
                ))

                db.commit()
                        
        except Exception as ex:
                db.rollback()
                raise Exception(ex)

    @classmethod
    def get_all_puestos(cls, db):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM PUESTOS"
                cursor.execute(query)
                rows = cursor.fetchall()
                puestos = []
                for row in rows:
                    puestos.append(Puesto(
                            id=row[0], 
                            puesto=row[1], 
                            sueldo_base=row[2],
                            sueldo_tarjeta=row[3],
                            horas_extras=row[4], 
                            categoria=row[6],
                            is_blocked=row[7]
                            
                            ))
                    
                return puestos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_all_puestos_no_block(cls, db):
        try:
            with db.cursor() as cursor:
                # Consulta con JOIN para obtener datos de PUESTOS y CATEGORIAS
                query = """
                    SELECT 
                        p.ID, 
                        p.PUESTO, 
                        p.SUELDO_BASE, 
                        p.SUELDO_TARJETA, 
                        p.HORA_EXTRA, 
                        p.CATEGORIA, 
                        p.IS_BLOCKED, 
                        c.CATEGORIA AS CATEGORIA_NOMBRE, 
                        c.FECHA_REGISTRO AS CATEGORIA_FECHA, 
                        c.IS_BLOCKED AS CATEGORIA_IS_BLOCKED
                    FROM PUESTOS p
                    LEFT JOIN CATEGORIAS c ON p.CATEGORIA = c.ID
                    WHERE p.IS_BLOCKED = 0
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                
                # Procesa los resultados
                puestos = []
                for row in rows:
                    puestos.append(Puesto(
                        id=row[0],
                        puesto=row[1],
                        sueldo_base=row[2],
                        sueldo_tarjeta=row[3],
                        horas_extras=row[4],
                        categoria={
                            "id": row[5],
                            "nombre": row[7],  # Nombre de la categoría
                            "fecha_registro": row[8],  # Fecha de registro de la categoría
                            "is_blocked": row[9]  # Estado de bloqueo de la categoría
                        },
                        is_blocked=row[6]
                    ))
                
                return puestos
        except Exception as ex:
            print(f"Error en get_all_puestos_no_block: {str(ex)}")
            raise Exception(ex)


    @classmethod
    def get_puestos_by_id(cls, db,id):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM PUESTOS WHERE ID = ?"
                cursor.execute(query, (id,))
                row = cursor.fetchone() 
                if row:
                    return Puesto(
                                id=row[0], 
                                puesto=row[1], 
                                sueldo_base=row[2],
                                sueldo_tarjeta=row[3],
                                horas_extras=row[4], 
                                categoria=row[6],
                                is_blocked=row[7]
                                
                                )
                    
                return None
        except Exception as ex:
            raise Exception(ex)

        

    @classmethod
    def change_status(cls, db, id, is_blocked):
        try:
            with db.cursor() as cursor:
                query = "UPDATE PUESTOS SET IS_BLOCKED = ? WHERE ID = ?"
                cursor.execute(query, (is_blocked, id))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex) 

    @classmethod
    def update_puesto(cls, db, puesto):
        try:
            with db.cursor() as cursor:
                query = """
                    UPDATE PUESTOS
                    SET PUESTO = ?, SUELDO_BASE = ?, SUELDO_TARJETA = ?, HORA_EXTRA = ?,
                    CATEGORIA = ?
                    WHERE ID = ?;
                """
                cursor.execute(query, (
                    puesto.puesto,
                    puesto.sueldo_base,
                    puesto.sueldo_tarjeta,
                    puesto.horas_extras,
                    puesto.categoria,
                    puesto.id
                ))
                db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)

    @classmethod
    def filter_puesto(cls, db, puesto, estado):
        try:
            with db.cursor() as cursor:
                cursor = db.cursor()
                query = "SELECT * FROM PUESTOS WHERE 1=1"
                params = []
                
                if puesto:
                    query += " AND PUESTO LIKE ?"
                    params.append(f'%{puesto}%')
                if estado:
                    if estado == 'activo':
                        query += " AND is_blocked = 0"
                    elif estado == 'bloqueado':
                        query += " AND is_blocked = 1"

                cursor.execute(query, params)
                rows = cursor.fetchall()
                puestos = []
                for row in rows:
                    puestos.append(Puesto(
                            id=row[0], 
                            puesto=row[1], 
                            sueldo_base=row[2],
                            sueldo_tarjeta=row[3],
                            horas_extras=row[4], 
                            categoria=row[6],
                            is_blocked=row[7]
                            
                            ))
                return puestos
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def get_puestos_by_category(cls, db,id):
        try:
            with db.cursor() as cursor:
                query = "SELECT * FROM PUESTOS WHERE CATEGORIA = ?"
                cursor.execute(query, (id,))
               
                rows = cursor.fetchall()
                puestos = []
                for row in rows:
                    puestos.append(Puesto(
                            id=row[0], 
                            puesto=row[1], 
                            sueldo_base=row[2],
                            sueldo_tarjeta=row[3],
                            horas_extras=row[4], 
                            categoria=row[6],
                            is_blocked=row[7]
                            
                            ))
                    
                return puestos
        except Exception as ex:
            raise Exception(ex)