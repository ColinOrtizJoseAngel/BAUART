from .entities.Nomina import Nomina

class ModelNomina:

    @classmethod
    def create_nomina(cls, db, nomina):
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO Nomina (
                    ID_Empleado, Fecha_Inicio, Fecha_Final, Extra, Deuda, Total_Nomina, Fecha_Registro, Observaciones
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                nomina.id_empleado,
                nomina.fecha_inicio,
                nomina.fecha_final,
                nomina.extra,
                nomina.deuda,
                nomina.total_nomina,
                nomina.fecha_registro,
                nomina.observaciones
            ))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al crear la nómina: {ex}")

    @classmethod
    def get_all_nominas(cls, db):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM Nomina ORDER BY Fecha_Registro DESC"
            cursor.execute(query)
            rows = cursor.fetchall()
            nominas = []
            for row in rows:
                nominas.append(Nomina(
                    id=row[0],
                    id_empleado=row[1],
                    fecha_inicio=row[2],
                    fecha_final=row[3],
                    extra=row[4],
                    deuda=row[5],
                    total_nomina=row[6],
                    fecha_registro=row[7],
                    observaciones=row[8]  # Nuevo campo
                ))
            return nominas
        except Exception as ex:
            raise Exception(f"Error al obtener las nóminas: {ex}")

    @classmethod
    def get_nomina_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT * FROM Nomina WHERE ID = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Nomina(
                    id=row[0],
                    id_empleado=row[1],
                    fecha_inicio=row[2],
                    fecha_final=row[3],
                    extra=row[4],
                    deuda=row[5],
                    total_nomina=row[6],
                    fecha_registro=row[7],
                    observaciones=row[8]  # Nuevo campo
                )
            return None
        except Exception as ex:
            raise Exception(f"Error al obtener la nómina: {ex}")


    @classmethod
    def delete_nomina(cls, db, id):
        try:
            cursor = db.cursor()
            query = "DELETE FROM Nomina WHERE ID = ?"
            cursor.execute(query, (id,))
            db.commit()
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al eliminar la nómina: {ex}")

    @classmethod
    def update_nomina_by_empleado(cls, db, id_empleado, **kwargs):
        """
        Actualiza los campos opcionales de una nómina basada en el ID del empleado.

        Args:
            db: Conexión a la base de datos.
            id_empleado: ID del empleado cuya nómina será actualizada.
            kwargs: Campos opcionales a actualizar (ejemplo: Fecha_Final, Extra, Observaciones).

        Returns:
            bool: True si la actualización fue exitosa, False si no se encontraron registros.
        """
        try:
            cursor = db.cursor()

            # Filtrar campos a actualizar
            updates = ", ".join(f"{key} = ?" for key in kwargs.keys())
            values = list(kwargs.values())
            query = f"UPDATE Nomina SET {updates} WHERE ID_Empleado = ?"
            values.append(id_empleado)

            cursor.execute(query, tuple(values))
            db.commit()

            if cursor.rowcount == 0:
                return False  # No se encontraron registros para actualizar
            return True
        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al actualizar la nómina del empleado: {ex}")

    @classmethod
    def check_existing_nomina(cls, db, id_empleado, fecha_inicio, fecha_final):
        """
        Verifica si ya existe un registro en la tabla Nomina para un empleado en un rango de fechas.

        Args:
            db: Conexión a la base de datos.
            id_empleado: ID del empleado.
            fecha_inicio: Fecha inicial del rango.
            fecha_final: Fecha final del rango.

        Returns:
            bool: True si existe un registro, False si no existe.
        """
        try:
            cursor = db.cursor()

            # Verificar si ya existe un registro en el rango de fechas para el empleado
            query_check = """
                SELECT ID
                FROM Nomina
                WHERE ID_Empleado = ? AND Fecha_Inicio = ? AND Fecha_Final = ?
            """
            cursor.execute(query_check, (id_empleado, fecha_inicio, fecha_final))
            existing_record = cursor.fetchone()

            return existing_record is not None

        except Exception as ex:
            raise Exception(f"Error al verificar el registro de la nómina: {ex}")

    @classmethod
    def update_nomina(cls, db, id_empleado, fecha_inicio, fecha_final, **kwargs):
        """
        Actualiza un registro en la tabla Nomina basado en el ID del empleado y el rango de fechas.

        Args:
            db: Conexión a la base de datos.
            id_empleado: ID del empleado.
            fecha_inicio: Fecha inicial del rango.
            fecha_final: Fecha final del rango.
            kwargs: Campos a actualizar (por ejemplo: Extra, Deuda, Observaciones).

        Returns:
            dict: Detalles del registro actualizado.
        """
        try:
            cursor = db.cursor()

            # Verificar si existe un registro con el ID del empleado y el rango de fechas
            query_check = """
                SELECT ID FROM Nomina
                WHERE ID_Empleado = ? AND Fecha_Inicio = ? AND Fecha_Final = ?
            """
            cursor.execute(query_check, (id_empleado, fecha_inicio, fecha_final))
            existing_record = cursor.fetchone()

            if existing_record:
                # Si existe, actualizamos los campos
                updates = ", ".join(f"{key} = ?" for key in kwargs.keys())
                values = list(kwargs.values())
                query_update = f"""
                    UPDATE Nomina SET {updates}
                    WHERE ID_Empleado = ? AND Fecha_Inicio = ? AND Fecha_Final = ?
                """
                values.append(id_empleado)  # ID del empleado
                values.append(fecha_inicio)  # Fecha de inicio
                values.append(fecha_final)   # Fecha final
                cursor.execute(query_update, tuple(values))
                db.commit()

                return {"action": "updated", "id_nomina": existing_record[0]}  # Devolver el ID del registro actualizado

            else:
                return {"action": "not_found", "message": "No se encontró el registro con los datos proporcionados."}

        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al actualizar la nómina: {ex}")

    @classmethod
    def create_nomina(cls, db, id_empleado, fecha_inicio, fecha_final, **kwargs):
        """
        Crea un nuevo registro en la tabla Nomina basado en los datos proporcionados.

        Args:
            db: Conexión a la base de datos.
            id_empleado: ID del empleado.
            fecha_inicio: Fecha inicial del rango.
            fecha_final: Fecha final del rango.
            kwargs: Campos adicionales (Ejemplo: Extra, Deuda, Observaciones).

        Returns:
            dict: Detalles del nuevo registro creado.
        """
        try:
            cursor = db.cursor()

            # Insertar un nuevo registro si no existe
            columns = ", ".join(["ID_Empleado", "Fecha_Inicio", "Fecha_Final"] + list(kwargs.keys()))
            placeholders = ", ".join(["?"] * (3 + len(kwargs)))
            values = [id_empleado, fecha_inicio, fecha_final] + list(kwargs.values())
            query_insert = f"INSERT INTO Nomina ({columns}) VALUES ({placeholders})"
            cursor.execute(query_insert, tuple(values))
            db.commit()

            # Obtener el ID de la última fila insertada utilizando SCOPE_IDENTITY()
            cursor.execute("SELECT SCOPE_IDENTITY()")
            last_id = cursor.fetchone()[0]

            return {"action": "created", "id_nomina": last_id}

        except Exception as ex:
            db.rollback()
            raise Exception(f"Error al crear la nómina: {ex}")

    @classmethod
    def upsert_nomina(cls, db, id_empleado, fecha_inicio, fecha_final, **kwargs):
        """
        Actualiza o crea un registro en la tabla Nomina basado en el ID del empleado y el rango de fechas.
        """
        try:
            # Verificar si existe un registro en el rango de fechas para el empleado
            if cls.check_existing_nomina(db, id_empleado, fecha_inicio, fecha_final):
                # Si existe, actualizamos
                return cls.update_nomina(db, id_empleado, fecha_inicio, fecha_final, **kwargs)
            else:
                # Si no existe, creamos un nuevo registro
                return cls.create_nomina(db, id_empleado, fecha_inicio, fecha_final, **kwargs)

        except Exception as ex:
            raise Exception(f"Error al realizar upsert de la nómina: {ex}")
