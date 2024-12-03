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
                query = "SELECT * FROM PUESTOS WHERE IS_BLOCKED = 0"
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