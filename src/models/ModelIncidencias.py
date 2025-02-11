from .entities.Incidencias import Incidencia
from datetime import datetime, timedelta

class IncidenciaModel:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    @staticmethod
    def create_incidencia(connection, incidencia: Incidencia):
        try:
            print("Datos que se intentan insertar:")
            print(f"IdEmpleado: {incidencia.idEmpleado}")
            print(f"TipoIncidencia: {incidencia.tipoIncidencia}")
            print(f"FechaInicial: {incidencia.fechaInicial}")
            print(f"FechaFinal: {incidencia.fechaFinal}")
            print(f"DiasSolicitados: {incidencia.diasSolicitados}")
            print(f"Comentarios: {incidencia.comentarios}")
            print(f"FechaRegistro: {incidencia.fechaRegistro}")

            cursor = connection.cursor()

            # Inserción en la tabla
            sql_insert = """
                INSERT INTO Incidencias (
                    IdEmpleado, TipoIncidencia, FechaInicial, FechaFinal, 
                    DiasSolicitados, Comentarios, FechaRegistro
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            cursor.execute(sql_insert, (
                incidencia.idEmpleado,
                incidencia.tipoIncidencia,
                incidencia.fechaInicial,
                incidencia.fechaFinal,
                incidencia.diasSolicitados,
                incidencia.comentarios,
                incidencia.fechaRegistro
            ))

            connection.commit()

            # Consultar el ID recién generado basado en los datos únicos
            sql_select = """
                SELECT IdIncidencia
                FROM Incidencias
                WHERE IdEmpleado = ? AND TipoIncidencia = ? 
                AND FechaInicial = ? AND FechaFinal = ?
                ORDER BY FechaRegistro DESC
            """

            cursor.execute(sql_select, (
                incidencia.idEmpleado,
                incidencia.tipoIncidencia,
                incidencia.fechaInicial,
                incidencia.fechaFinal
            ))

            result = cursor.fetchone()
            if result:
                return result[0]  # Retornar el ID de la incidencia
            else:
                return None

        except Exception as e:
            print(f"Error al insertar la incidencia: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()

    @staticmethod
    def create_asistencia(connection, id_empleado=None, id_proyecto=None, dia=None, es_incidencia=None, id_incidencia=None):
        """
        Inserta un registro en la tabla Asistencia con las columnas seleccionadas.

        Args:
            connection: Conexión a la base de datos.
            id_empleado (int, opcional): ID del empleado.
            id_proyecto (int, opcional): ID del proyecto.
            dia (datetime, opcional): Fecha del día.
            es_incidencia (bool, opcional): Indica si es una incidencia.
            id_incidencia (int, opcional): ID de la incidencia.

        Returns:
            dict: Resultado de la operación, incluyendo el ID del registro insertado o un mensaje de error.
        """
        try:
            cursor = connection.cursor()

            # Consulta SQL para insertar
            sql_insert = """
                INSERT INTO [Asistencia] ([ID_Empleado], [ID_Proyecto], [DIA], [Es_Incidencia], [ID_Incidencia])
                VALUES (?, ?, ?, ?, ?)
            """

            # Ejecutar la inserción
            cursor.execute(sql_insert, (id_empleado, id_proyecto, dia, es_incidencia, id_incidencia))
            connection.commit()

            # Consultar el ID del registro recién insertado
            sql_select = "SELECT SCOPE_IDENTITY()"
            cursor.execute(sql_select)
            new_id = cursor.fetchone()[0]

            return {"message": "Registro insertado exitosamente", "id": new_id}

        except Exception as e:
            print(f"Error al insertar en Asistencia: {str(e)}")
            connection.rollback()
            return {"error": str(e)}
        finally:
            cursor.close()



    @staticmethod
    def obtener_incidencias_por_empleado_y_fecha(connection, id_empleado, fecha):
        try:
            cursor = connection.cursor()
            query = """
                SELECT TipoIncidencia, Comentarios
                FROM Incidencias
                WHERE IdEmpleado = ? AND ? BETWEEN FechaInicial AND FechaFinal
            """
            cursor.execute(query, (id_empleado, fecha))
            rows = cursor.fetchall()
            print(f"Filas obtenidas: {rows}")  # Esto imprimirá las filas completas desde la base de datos
            incidencias = [{"tipo": row[0], "comentarios": row[1]} for row in rows]
            return incidencias
        except Exception as e:
            print(f"Error al obtener incidencias: {e}")
            return []


    def obtener_incidencias_por_rango(self, fecha_inicio, fecha_fin):
        """
        Obtiene las incidencias registradas en un rango de fechas.

        Args:
            fecha_inicio (date): Fecha inicial del rango.
            fecha_fin (date): Fecha final del rango.

        Returns:
            dict: Diccionario de incidencias agrupadas por empleado.
        """
        try:
            # Convertir fechas a cadenas en formato ISO (YYYY-MM-DD)
            fecha_inicio_str = fecha_inicio.strftime('%Y-%m-%d')
            fecha_fin_str = fecha_fin.strftime('%Y-%m-%d')

            query = """
                SELECT 
                    i.IdEmpleado AS empleado_id,
                    CONCAT(e.NOMBRE, ' ', e.APELLIDO) AS nombre_completo,
                    i.TipoIncidencia AS tipo_incidencia,
                    i.Comentarios AS comentarios,
                    i.FechaInicial AS fecha_inicial,
                    i.FechaFinal AS fecha_final
                FROM Incidencias i
                INNER JOIN Empleados e ON i.IdEmpleado = e.ID
                WHERE i.FechaInicial <= ? AND i.FechaFinal >= ?
            """

            # Usar las cadenas en los parámetros
            params = [fecha_fin_str, fecha_inicio_str]

            with self.db_connection.cursor() as cursor:
                cursor.execute(query, params)
                rows = cursor.fetchall()

                # Organizar las incidencias por empleado y día
                dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
                incidencias = {}

                for row in rows:
                    empleado_id = row.empleado_id

                    if empleado_id not in incidencias:
                        incidencias[empleado_id] = {
                            "nombre_empleado": row.nombre_completo,
                            "incidencias": {}
                        }

                    # Rango de días afectado por la incidencia
                    fecha_inicial = row.fecha_inicial
                    fecha_final = row.fecha_final

                    for i in range((fecha_fin - fecha_inicio).days + 1):
                        dia_actual = fecha_inicio + timedelta(days=i)

                        if fecha_inicial <= dia_actual <= fecha_final:
                            dia_semana = dias_semana[dia_actual.weekday()]  # Convertir fecha a día de la semana
                            incidencias[empleado_id]["incidencias"][dia_actual.strftime('%Y-%m-%d')] = {
                                "tipo_incidencia": row.tipo_incidencia,
                                "comentarios": row.comentarios
                            }

                return incidencias

        except Exception as e:
            print(f"Error al obtener incidencias por rango: {str(e)}")
            return {"error": str(e)}

    def agregar_incidencia(self, id_empleado, tipo_incidencia, fecha_inicial, fecha_final, comentarios):
        """
        Agrega una nueva incidencia a la base de datos.

        Args:
            id_empleado (int): ID del empleado.
            tipo_incidencia (str): Tipo de incidencia.
            fecha_inicial (date): Fecha inicial de la incidencia.
            fecha_final (date): Fecha final de la incidencia.
            comentarios (str): Comentarios adicionales.

        Returns:
            dict: Resultado de la operación.
        """
        try:
            query = """
                INSERT INTO Incidencias (IdEmpleado, TipoIncidencia, FechaInicial, FechaFinal, Comentarios)
                VALUES (?, ?, ?, ?, ?)
            """

            params = [
                id_empleado,
                tipo_incidencia,
                fecha_inicial.strftime('%Y-%m-%d'),
                fecha_final.strftime('%Y-%m-%d'),
                comentarios
            ]

            with self.db_connection.cursor() as cursor:
                cursor.execute(query, params)
                self.db_connection.commit()

            return {"message": "Incidencia registrada exitosamente"}

        except Exception as e:
            print(f"Error al agregar incidencia: {str(e)}")
            return {"error": str(e)}
