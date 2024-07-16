from .entities.RegistroPatronal import ResgistroPatronal

class ModelRegistroPatronal():

    @classmethod
    def newRegistroPatronal(self,db,resgistroPatronal):
        try:
            cursor = db.cursor()
            query = """
                    INSERT INTO REGISTROS_PATRONALES (
                    NUMERO_REGISTRO_PATRONAL,ID_EMPRESA,ESTADO ) VALUES (?,?,?);
                    """
            cursor.execute(query, (
                resgistroPatronal.registro_patronal,
                resgistroPatronal.empresa,
                resgistroPatronal.estado
            ))
            db.commit()
        
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_registroPatronal(cls, db):
        try:
            cursor = db.cursor()
            query = """
                SELECT REGISTROS_PATRONALES.ID,REGISTROS_PATRONALES.NUMERO_REGISTRO_PATRONAL,REGISTROS_PATRONALES.ID_EMPRESA,
                EMPRESAS.RAZON_SOCIAL,REGISTROS_PATRONALES.ESTADO,REGISTROS_PATRONALES.is_blocked 
                FROM REGISTROS_PATRONALES 
                INNER JOIN EMPRESAS 
                ON REGISTROS_PATRONALES.ID_EMPRESA = EMPRESAS.ID_EMPRESA

                """
            cursor.execute(query)
            rows = cursor.fetchall()
            registrospatronales = []
            for row in rows:
                registrospatronales.append(ResgistroPatronal(
                    id_registro=row[0], registro_patronal=row[1], empresa=row[3],estado=row[4],
                    is_blocked=row[5] 
                    ))
            return registrospatronales
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_RegistroPatronal_empresa(cls, db, id_empresa):
        try:
            cursor = db.cursor()
            query = """
                SELECT REGISTROS_PATRONALES.ID,REGISTROS_PATRONALES.NUMERO_REGISTRO_PATRONAL,REGISTROS_PATRONALES.ID_EMPRESA,
                EMPRESAS.RAZON_SOCIAL,REGISTROS_PATRONALES.ESTADO,REGISTROS_PATRONALES.is_blocked 
                FROM REGISTROS_PATRONALES 
                INNER JOIN EMPRESAS 
                ON REGISTROS_PATRONALES.ID_EMPRESA = EMPRESAS.ID_EMPRESA WHERE EMPRESAS.ID_EMPRESA = ?;

            """
            cursor.execute(query, (id_empresa,))
            rows = cursor.fetchall()
            registrospatronales = []
            for row in rows:
                registrospatronales.append(ResgistroPatronal(
                    id_registro=row[0], 
                    registro_patronal=row[1], 
                    empresa=row[3],
                    estado=row[4],
                    is_blocked=row[5] 
                ))
            return registrospatronales
        except Exception as ex:
            raise Exception(ex)

    
    #ACTUALIAZA REGISTRO PATRONAL
    @classmethod
    def update_registro_patronal(cls, db, registro_patronal):
        try:
            cursor = db.cursor()
            query = """
                UPDATE REGISTROS_PATRONALES
                SET  NUMERO_REGISTRO_PATRONAL,ESTADO) VALUES (?,?,?) WHERERE ID = ?;
                
            """
            print(registro_patronal.id_registro)
            cursor.execute(query, (
                registro_patronal.registro_patronal,
                registro_patronal.estado,
                registro_patronal.id_registro
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(ex)
        
    @classmethod
    def get_all_registros_patronales(cls, db):
        try:
                cursor = db.cursor()
                query = "SELECT * FROM REGISTROS_PATRONALES"
                cursor.execute(query)
                rows = cursor.fetchall()
                registrospatronales = []
                for row in rows:
                    registrospatronales.append(ResgistroPatronal(
                        id_registro=row[0], registro_patronal=row[1], empresa=row[2],estado=row[3],
                        is_blocked=row[4] 
                        ))
                return registrospatronales
        except Exception as ex:
                raise Exception(ex)