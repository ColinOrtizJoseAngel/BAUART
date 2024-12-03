from datetime import datetime, timedelta
from math import radians, sin, cos, sqrt, atan2


class AsistenciaModel:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def _calcular_distancia(self, lat1, lon1, lat2, lon2):
        """
        Calcula la distancia entre dos puntos geográficos utilizando la fórmula haversine.
        """
        R = 6371  # Radio de la Tierra en kilómetros
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

    def registrar_asistencia(self, asistencia):
        """
        Registra la asistencia del empleado si está a menos de 2 km del proyecto.
        """
        try:
            query_proyecto = """
                SELECT LATITUD, LONGITUD 
                FROM Proyectos 
                WHERE ID = ?
            """
            with self.db_connection.cursor() as cursor:
                cursor.execute(query_proyecto, (asistencia['id_proyecto'],))
                proyecto = cursor.fetchone()
                if not proyecto:
                    return {"error": "El proyecto seleccionado no existe."}

                lat_proyecto = float(proyecto.LATITUD)
                lon_proyecto = float(proyecto.LONGITUD)

            lat_empleado = float(asistencia['latitud'])
            lon_empleado = float(asistencia['longitud'])
            distancia = self._calcular_distancia(
                lat_proyecto, lon_proyecto, lat_empleado, lon_empleado
            )

            if distancia > 2:
                return {"error": f"La distancia al proyecto es de {distancia:.2f} km. Solo puedes registrar asistencia si estás a menos de 2 km."}

            query = """
                INSERT INTO Asistencia (ID_EMPLEADO, ID_PROYECTO, DIA, HORA_ENTRADA, LATITUD, LONGITUD, FOTO_BASE64)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            with self.db_connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        asistencia['id_empleado'],
                        asistencia['id_proyecto'],
                        asistencia['dia'],
                        asistencia['hora_entrada'],
                        asistencia['latitud'],
                        asistencia['longitud'],
                        asistencia['foto_base64'],
                    )
                )
            self.db_connection.commit()
            return {"mensaje": "Asistencia registrada exitosamente"}
        except Exception as e:
            print(f"Error al registrar asistencia: {str(e)}")
            return {"error": str(e)}

    def actualizar_hora_salida(self, id_empleado):
        """
        Actualiza la hora de salida del empleado.
        """
        try:
            hora_salida = datetime.now().strftime('%H:%M:%S')

            # Verificar si ya existe un registro para hoy
            query_verificar = """
                SELECT HORA_SALIDA
                FROM Asistencia
                WHERE ID_EMPLEADO = ? AND DIA = CAST(GETDATE() AS DATE)
            """
            with self.db_connection.cursor() as cursor:
                cursor.execute(query_verificar, (id_empleado,))
                row = cursor.fetchone()

                if not row:
                    return {"error": "No se encontró un registro pendiente de salida para este empleado hoy."}
                if row.HORA_SALIDA is not None:
                    return {"error": "La hora de salida ya ha sido registrada para este empleado hoy."}

            # Actualizar HORA_SALIDA si está pendiente
            query_actualizar = """
                UPDATE Asistencia
                SET HORA_SALIDA = ?
                WHERE ID_EMPLEADO = ? AND DIA = CAST(GETDATE() AS DATE) AND HORA_SALIDA IS NULL
            """
            with self.db_connection.cursor() as cursor:
                cursor.execute(query_actualizar, (hora_salida, id_empleado))
                if cursor.rowcount == 0:
                    return {"error": "No se encontró un registro pendiente de salida para este empleado hoy."}

            self.db_connection.commit()
            return {"mensaje": "Hora de salida registrada correctamente"}
        except Exception as e:
            print(f"Error al actualizar hora de salida: {str(e)}")
            return {"error": str(e)}

    def verificar_asistencia(self, id_empleado):
        """
        Verifica si el empleado ha registrado asistencia hoy.
        """
        try:
            query = """
                SELECT HORA_ENTRADA, HORA_SALIDA
                FROM Asistencia
                WHERE ID_EMPLEADO = ? AND DIA = CAST(GETDATE() AS DATE)
            """
            with self.db_connection.cursor() as cursor:
                cursor.execute(query, (id_empleado,))
                row = cursor.fetchone()
                if row:
                    return {
                        "asistencia_registrada": True,
                        "hora_entrada": str(row.HORA_ENTRADA),
                        "hora_salida": str(row.HORA_SALIDA) if row.HORA_SALIDA else None,
                    }
                else:
                    return {"asistencia_registrada": False}
        except Exception as e:
            print(f"Error al verificar asistencia: {str(e)}")
            return {"error": str(e)}

    def obtener_asistencias_por_rango(self, fecha_inicio, fecha_fin, id_proyecto=None):
        """
        Obtiene las asistencias registradas en un rango de fechas, con filtro opcional por proyecto.

        Args:
            fecha_inicio (date): Fecha inicial del rango.
            fecha_fin (date): Fecha final del rango.
            id_proyecto (int, optional): ID del proyecto para filtrar. Default es None.

        Returns:
            list: Lista de asistencias agrupadas por empleado y día.
        """
        try:
            query = """
                SELECT 
                    e.ID AS empleado_id,
                    CONCAT(e.NOMBRE, ' ', e.APELLIDO) AS nombre_completo, -- Concatenación de nombre y apellido
                    p.NOMBRE_PROYECTO AS nombre_proyecto,
                    a.DIA AS fecha,
                    a.HORA_ENTRADA AS hora_entrada,
                    a.HORA_SALIDA AS hora_salida,
                    a.FOTO_BASE64 AS foto_base64,
                    a.LATITUD AS latitud,
                    a.LONGITUD AS longitud,
                    a.DIA AS dia
                FROM Empleados e
                LEFT JOIN Asistencia a ON e.ID = a.ID_EMPLEADO AND a.DIA BETWEEN ? AND ?
                LEFT JOIN Proyectos p ON a.ID_PROYECTO = p.ID
            """

            params = [fecha_inicio, fecha_fin]

            if id_proyecto:
                query += " WHERE a.ID_PROYECTO = ?"
                params.append(id_proyecto)

            query += " ORDER BY e.NOMBRE, a.DIA"

            with self.db_connection.cursor() as cursor:
                cursor.execute(query, tuple(params))
                rows = cursor.fetchall()

                dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
                asistencias = {}
                fecha_actual = datetime.now().date()

                for row in rows:
                    empleado_id = row.empleado_id
                    if empleado_id not in asistencias:
                        asistencias[empleado_id] = {
                            "nombre_empleado": row.nombre_completo,  # Usar el nombre completo concatenado
                            "nombre_proyecto": row.nombre_proyecto,
                        }
                        for i in range(5):
                            dia = fecha_inicio + timedelta(days=i)
                            estado = "N/A" if dia > fecha_actual else "F"
                            dia_semana = dias_semana[i]
                            asistencias[empleado_id][dia_semana] = {
                                "estado": estado,
                                "hora_entrada": None,
                                "hora_salida": None,
                                "foto_base64": None,
                                "latitud": None,
                                "longitud": None
                            }

                    if row.fecha:
                        dia_semana = dias_semana[(row.fecha - fecha_inicio).days]
                        asistencias[empleado_id][dia_semana] = {
                            "estado": "A" if row.hora_entrada and row.hora_salida else "F",
                            "hora_entrada": row.hora_entrada.strftime("%H:%M") if row.hora_entrada else None,
                            "hora_salida": row.hora_salida.strftime("%H:%M") if row.hora_salida else None,
                            "foto_base64": row.foto_base64,
                            "latitud": row.latitud,
                            "longitud": row.longitud,
                            "dia": row.dia
                        }

                return list(asistencias.values())
        except Exception as e:
            print(f"Error al obtener asistencias por rango: {str(e)}")
        return {"error": str(e)}
