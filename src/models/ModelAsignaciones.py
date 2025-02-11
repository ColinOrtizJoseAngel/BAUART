from .entities.Asignacion import Asignacion
from .entities.ProyectoObra import ProyectoObra
from datetime import datetime, timedelta

class ModelAsignaciones:

    @staticmethod
    def get_all_asignaciones(cursor):
        query = """
            SELECT ID, ID_EMPLEADO, ID_PROYECTO, SUELDO_BASE, SUELDO_IMSS, MONEDERO, FECHA_ASIGNACION, FECHA_FIN
            FROM ASIGNACIONES
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Asignacion(*row) for row in rows]  # 🔹 Simplificación con un generador

    @staticmethod
    def get_asignacion_by_id(cursor, asignacion_id):
        query = """
            SELECT ID, ID_EMPLEADO, ID_PROYECTO, SUELDO_BASE, SUELDO_IMSS, MONEDERO, FECHA_ASIGNACION, FECHA_FIN
            FROM ASIGNACIONES
            WHERE ID = ?
        """
        cursor.execute(query, (asignacion_id,))
        row = cursor.fetchone()
        return Asignacion(*row) if row else None  # 🔹 Más limpio


    @staticmethod
    def add_asignacion(cursor, asignacion):
        query = """
            INSERT INTO ASIGNACIONES (ID_EMPLEADO, ID_PROYECTO, SUELDO_BASE, SUELDO_IMSS, MONEDERO, FECHA_ASIGNACION, FECHA_FIN)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            asignacion.id_empleado,
            asignacion.id_proyecto,
            asignacion.sueldo_base,
            asignacion.sueldo_imss,
            asignacion.monedero,
            asignacion.fecha_asignacion,
            asignacion.fecha_fin
        ))
            
    @staticmethod
    def update_asignacion(cursor, asignacion):
        """ Actualiza los datos de una asignación existente. """
        query = """
            UPDATE ASIGNACIONES
            SET ID_EMPLEADO = ?, ID_PROYECTO = ?, SUELDO_BASE = ?, SUELDO_IMSS = ?, MONEDERO = ?, FECHA_ASIGNACION = ?, FECHA_FIN = ?, id_detalle = ?
            WHERE ID = ?
        """
        cursor.execute(query, (
            asignacion.id_empleado,
            asignacion.id_proyecto,
            asignacion.sueldo_base,
            asignacion.sueldo_imss,
            asignacion.monedero,
            asignacion.fecha_asignacion,
            asignacion.fecha_fin,
            asignacion.id_detalle,  # Se añadió este campo
            asignacion.id
        ))

    @staticmethod
    def delete_asignacion(cursor, asignacion_id):
        """ Elimina una asignación por su ID. """
        query = "DELETE FROM ASIGNACIONES WHERE ID = ?"
        cursor.execute(query, (asignacion_id,))

    @classmethod
    def get_proyectos_asignados(cls, db, id_empleado):
        """ Obtiene los proyectos asignados a un empleado. """
        try:
            with db.cursor() as cursor:
                query = """
                    SELECT p.* FROM PROYECTOS p
                    JOIN ASIGNACIONES a ON p.id = a.id_proyecto
                    WHERE a.id_empleado = ?
                """
                cursor.execute(query, (id_empleado,))
                rows = cursor.fetchall()
                return [ProyectoObra(*row) for row in rows]

        except Exception as ex:
            print(f"🚨 ERROR en get_proyectos_asignados: {ex}")
            raise Exception(f"Error al obtener proyectos asignados: {ex}")

    @staticmethod
    def get_project_details(cursor, id_proyecto):
        """ Obtiene los detalles de un proyecto, incluyendo presupuestos y asignaciones. """
        try:
            query = """
            WITH PresupuestosFiltrados AS (
                SELECT id_presupuesto, proyecto
                FROM [BAUART].[dbo].[Presupuestos]
                WHERE id_proyecto = ?
            ),
            DetallesPresupuestoFiltrados AS (
                SELECT id_detalle, id_presupuesto, concepto
                FROM [BAUART].[dbo].[DetallesPresupuesto]
                WHERE id_presupuesto IN (SELECT id_presupuesto FROM PresupuestosFiltrados)
                AND id_proveedor = 0
            ),
            DetallesBauartFiltrados AS (
                SELECT id_detalle_bauart, id_presupuesto_bauart, concepto
                FROM [BAUART].[dbo].[DetallesBauart]
                WHERE id_presupuesto_bauart IN (SELECT id_presupuesto FROM PresupuestosFiltrados)
                AND is_nomina = 1
                AND ID_ASIGNACION IS NULL
            )
            SELECT 'Presupuesto' AS Tipo, id_presupuesto AS ID, proyecto AS Descripcion FROM PresupuestosFiltrados
            UNION ALL
            SELECT 'DetallePresupuesto' AS Tipo, id_detalle AS ID, concepto AS Descripcion FROM DetallesPresupuestoFiltrados
            UNION ALL
            SELECT 'DetalleBauart' AS Tipo, id_detalle_bauart AS ID, concepto AS Descripcion FROM DetallesBauartFiltrados;
            """

            cursor.execute(query, (id_proyecto,))
            rows = cursor.fetchall()
            return [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]

        except Exception as ex:
            print(f"❌ ERROR en get_project_details: {ex}")
            raise Exception(f"Error al obtener los detalles del proyecto: {ex}")

from .entities.Asignacion import Asignacion
from .entities.ProyectoObra import ProyectoObra

class ModelAsignaciones:

    @staticmethod
    def get_all_asignaciones(cursor):
        query = """
            SELECT ID, ID_EMPLEADO, ID_PROYECTO, SUELDO_BASE, SUELDO_IMSS, MONEDERO, FECHA_ASIGNACION, FECHA_FIN
            FROM ASIGNACIONES
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Asignacion(*row) for row in rows]  # 🔹 Simplificación con un generador

    @staticmethod
    def get_asignacion_by_id(cursor, asignacion_id):
        query = """
            SELECT ID, ID_EMPLEADO, ID_PROYECTO, SUELDO_BASE, SUELDO_IMSS, MONEDERO, FECHA_ASIGNACION, FECHA_FIN
            FROM ASIGNACIONES
            WHERE ID = ?
        """
        cursor.execute(query, (asignacion_id,))
        row = cursor.fetchone()
        return Asignacion(*row) if row else None  # 🔹 Más limpio


    @staticmethod
    def add_asignacion(cursor, asignacion):
        query = """
            INSERT INTO ASIGNACIONES (ID_EMPLEADO, ID_PROYECTO, SUELDO_BASE, SUELDO_IMSS, MONEDERO, 
                                    FECHA_ASIGNACION, FECHA_FIN, id_detalle, hora_entrada_p, hora_salida_p)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            asignacion.id_empleado,
            asignacion.id_proyecto,
            asignacion.sueldo_base,
            asignacion.sueldo_imss,
            asignacion.monedero,
            asignacion.fecha_asignacion,
            asignacion.fecha_fin,
            asignacion.id_detalle,
            asignacion.hora_entrada_p if asignacion.hora_entrada_p else None,  
            asignacion.hora_salida_p if asignacion.hora_salida_p else None   
        ))
            
    @staticmethod
    def update_asignacion(cursor, asignacion):
        """ Actualiza los datos de una asignación existente, incluyendo hora_entrada_p y hora_salida_p opcionales. """
        query = """
            UPDATE ASIGNACIONES
            SET ID_EMPLEADO = ?, ID_PROYECTO = ?, SUELDO_BASE = ?, SUELDO_IMSS = ?, MONEDERO = ?, 
                FECHA_ASIGNACION = ?, FECHA_FIN = ?, hora_entrada_p = ?, hora_salida_p = ?
            WHERE ID = ?
        """
        cursor.execute(query, (
            asignacion.id_empleado,
            asignacion.id_proyecto,
            asignacion.sueldo_base,
            asignacion.sueldo_imss,
            asignacion.monedero,
            asignacion.fecha_asignacion,
            asignacion.fecha_fin,
            asignacion.hora_entrada_p if asignacion.hora_entrada_p else None,  # Valor opcional
            asignacion.hora_salida_p if asignacion.hora_salida_p else None,   # Valor opcional
            asignacion.id
        ))

    @staticmethod
    def delete_asignacion(cursor, asignacion_id):
        """ Elimina una asignación por su ID. """
        query = "DELETE FROM ASIGNACIONES WHERE ID = ?"
        cursor.execute(query, (asignacion_id,))

    @classmethod
    def get_proyectos_asignados(cls, db, id_empleado):
        try:
            with db.cursor() as cursor:
                # Consulta SQL para obtener todos los datos requeridos
                query = """
                    SELECT 
                        p.id, p.id_empresa, p.id_cliente, p.fecha_inicio, p.fecha_contrato, 
                        p.fecha_fin, p.nombre_proyecto, p.centro_comercial, p.pais, 
                        p.estado, p.municipio, p.colonia, p.calle, p.numero_exterior, 
                        p.numero_interior, p.director_proyecto, p.lider_proyecto, 
                        p.gerente_proyecto, p.lider1, p.lider2, p.tipo_id, p.cp, 
                        p.fecha_registro, p.usuario_id, p.is_blocked
                    FROM PROYECTOS p
                    JOIN ASIGNACIONES a ON p.id = a.id_proyecto
                    WHERE a.id_empleado = ?
                """
                # Ejecutar la consulta con el parámetro
                cursor.execute(query, (id_empleado,))
                rows = cursor.fetchall()

                # Construir objetos ProyectoObra
                proyectos = []
                for row in rows:
                    proyectos.append(ProyectoObra(
                        id=row[0],
                        id_empresa=row[1],
                        id_cliente=row[2],
                        fecha_inicio=row[3],
                        fecha_contrato=row[4],
                        fecha_fin=row[5],
                        nombre_proyecto=row[6],
                        centro_comercial=row[7],
                        pais=row[8],
                        estado=row[9],
                        municipio=row[10],
                        colonia=row[11],
                        calle=row[12],
                        numero_exterior=row[13],
                        numero_interior=row[14],
                        director_proyecto=row[15],
                        lider_proyecto=row[16],
                        gerente_proyecto=row[17],
                        lider1=row[18],
                        lider2=row[19],
                        tipo_id=row[20],
                        cp=row[21],
                        fecha_registro=row[22],
                        usuario_id=row[23],
                        is_blocked=bool(row[24])
                    ))

                return proyectos
        except Exception as ex:
            raise Exception(f"Error al obtener proyectos asignados: {ex}")

    @staticmethod
    def get_project_details(cursor, id_proyecto):
        """ Obtiene los detalles de un proyecto, incluyendo presupuestos y asignaciones, pero solo las nóminas sin asignación previa. """
        try:
            query = """
            WITH PresupuestosFiltrados AS (
                SELECT id_presupuesto, proyecto
                FROM [BAUART].[dbo].[Presupuestos]
                WHERE id_proyecto = ?  -- Parámetro de filtro para el proyecto
            ),
            PresupuestosBauartFiltrados AS (
                SELECT [id_presupuesto_bauart], [id_detalle], [nombre_presupuesto],
                    [total_presupuesto_cliente], [total_presupuesto_proveedor],
                    [diferencia_presupuesto], [is_blocked], [estatus], [id_presupuesto]
                FROM [BAUART].[dbo].[PresupuestosBauart]
                WHERE id_presupuesto IN (SELECT id_presupuesto FROM PresupuestosFiltrados)
            ),
            DetallesBauartFiltrados AS (
                SELECT [id_detalle_bauart], [id_presupuesto_bauart], [concepto]
                FROM [BAUART].[dbo].[DetallesBauart]
                WHERE id_presupuesto_bauart IN (SELECT id_presupuesto_bauart FROM PresupuestosBauartFiltrados)
                AND is_nomina = 1  -- Solo trae los detalles con nómina
            )
            SELECT 'Presupuesto' AS Tipo, id_presupuesto AS ID, proyecto AS Descripcion 
            FROM PresupuestosFiltrados
            UNION ALL
            SELECT 'PresupuestoBauart' AS Tipo, id_presupuesto_bauart AS ID, nombre_presupuesto AS Descripcion
            FROM PresupuestosBauartFiltrados
            UNION ALL
            SELECT 'DetalleBauart' AS Tipo, id_detalle_bauart AS ID, concepto AS Descripcion
            FROM DetallesBauartFiltrados;

            """

            cursor.execute(query, (id_proyecto,))
            rows = cursor.fetchall()
            return [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]

        except Exception as ex:
            print(f"❌ ERROR en get_project_details: {ex}")
            raise Exception(f"Error al obtener los detalles del proyecto: {ex}")


    @staticmethod
    def update_id_asignacion_detalle_bauart(cursor, id_detalle_bauart, id_asignacion):
        """ Asocia una asignación con un Detalle Bauart. """
        if not id_detalle_bauart or not id_asignacion:
            raise ValueError("❌ id_detalle_bauart e id_asignacion son requeridos.")

        try:
            query = """
                UPDATE [BAUART].[dbo].[DetallesBauart]
                SET id_asignacion = ?
                WHERE id_detalle_bauart = ?
            """
            cursor.execute(query, (id_asignacion, id_detalle_bauart))
            
            if cursor.rowcount == 0:
                raise Exception(f"🚨 No se encontró id_detalle_bauart {id_detalle_bauart} para actualizar.")

            

        except Exception as ex:
            print(f"❌ ERROR en update_id_asignacion_detalle_bauart: {ex}")
            raise Exception(f"Error al actualizar id_asignacion en DetallesBauart: {ex}")

    @staticmethod
    def desasignar_empleado(cursor, id_empleado, id_proyecto):
        """ Desasigna un empleado de un proyecto usando id_empleado y id_proyecto. """
        try:
            # Obtener el id_asignacion y id_detalle_bauart correspondientes al empleado y proyecto
            query_asignacion = """
                SELECT a.ID, db.id_detalle_bauart
                FROM ASIGNACIONES a
                LEFT JOIN [BAUART].[dbo].[DetallesBauart] db ON db.id_asignacion = a.ID
                WHERE a.ID_EMPLEADO = ? AND a.ID_PROYECTO = ? AND a.FECHA_FIN IS NULL
            """
            cursor.execute(query_asignacion, (id_empleado, id_proyecto))
            row = cursor.fetchone()

            if not row:
                raise Exception(f"🚨 No se encontró asignación activa para el empleado {id_empleado} en el proyecto {id_proyecto}.")

            id_asignacion, id_detalle_bauart = row

            # Actualizar la fecha de fin de la asignación
            query_update_asignacion = """
                UPDATE ASIGNACIONES
                SET FECHA_FIN = ?
                WHERE ID = ? AND ID_EMPLEADO = ?
            """
            fecha_fin = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha de desasignación actual
            cursor.execute(query_update_asignacion, (fecha_fin, id_asignacion, id_empleado))

            if cursor.rowcount == 0:
                raise Exception(f"🚨 No se pudo actualizar la fecha de fin de la asignación para el empleado {id_empleado}.")

            # Desasignar el detalle Bauart, es decir, poner su id_asignacion a NULL
            if id_detalle_bauart:
                query_update_detalle_bauart = """
                    UPDATE [BAUART].[dbo].[DetallesBauart]
                    SET id_asignacion = NULL
                    WHERE id_detalle_bauart = ?
                """
                cursor.execute(query_update_detalle_bauart, (id_detalle_bauart,))

                if cursor.rowcount == 0:
                    raise Exception(f"🚨 No se encontró DetalleBauart con ID {id_detalle_bauart} para desasignar.")

            # Confirmar transacciones
            cursor.connection.commit()

            return True  # Si todo ha ido bien, devolvemos True

        except Exception as ex:
            print(f"❌ ERROR en desasignar_empleado: {ex}")
            cursor.connection.rollback()  # Revertir cambios en caso de error
            return False  # En caso de error, retornamos False
