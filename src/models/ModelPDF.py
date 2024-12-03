from flask_login import current_user
from models.ModelOrden import MyOrdendeCompra
from flask import render_template
import base64
import pdfkit

class ModelPDF:
    @staticmethod
    def generar_pdf(db, id, proveedor_id=None):
        try:
            # Consulta para obtener los detalles de la orden
            query = """
                SELECT 
                    ID_REQUISICION, 
                    FechaHoraEntrega, 
                    DireccionEntrega, 
                    Contacto, 
                    Telefono, 
                    PorcentajeDescuento  -- Incluimos el campo del descuento
                FROM ORDENES
                WHERE ID = ?
            """
            cursor = db.cursor()
            cursor.execute(query, (id,))
            result = cursor.fetchone()

            if not result:
                raise Exception(f"No se encontró la orden con ID: {id}")

            # Asignar valores obtenidos
            id_requisicion = result[0]
            fecha_hora_entrega = result[1] or "No especificada"
            direccion_entrega = result[2] or "No especificada"
            contacto = result[3] or "No especificado"
            telefono = result[4] or "No especificado"
            porcentaje_descuento = float(result[5]) if result[5] is not None else 0  # Descuento en porcentaje

            # Obtener datos de la empresa
            id_empresa = current_user.id_empresa
            empresa_query = """
                SELECT 
                    RAZON_SOCIAL, 
                    RFC, 
                    REPSE, 
                    REGIMEN_FISCAL_ID, 
                    NOMBRE_REPRESENTANTE1, 
                    APELLIDO_REPRESENTANTE1, 
                    TELEFONO_REPRESENTANTE1, 
                    CORREO_REPRESENTANTE1, 
                    NOMBRE_REPRESENTANTE2, 
                    APELLIDO_REPRESENTANTE2, 
                    TELEFONO_REPRESENTANTE2, 
                    CORREO_REPRESENTANTE2, 
                    NOMBRE_APODERADO, 
                    APELLIDO_APODERADO, 
                    TELEFONO_APODERADO, 
                    CORREO_APODERADO, 
                    CP, 
                    ESTADO, 
                    CIUDAD, 
                    DIRECCION
                FROM EMPRESAS
                WHERE ID = ?
            """
            cursor.execute(empresa_query, (id_empresa,))
            empresa = cursor.fetchone()

            if not empresa:
                raise Exception(f"No se encontró la empresa con ID: {id_empresa}")

            # Consulta para obtener los datos de facturación de CUENTAS_EMPRESAS
            cuentas_query = """
                SELECT 
                    NUMERO_CUENTA, 
                    CLABE
                FROM CUENTAS_EMPRESAS
                WHERE ID_EMPRESA = ?
            """
            cursor.execute(cuentas_query, (id_empresa,))
            cuentas = cursor.fetchone()

            empresa_datos = {
                "razon_social": empresa[0],
                "rfc": empresa[1],
                "repse": empresa[2],
                "regimen_fiscal": empresa[3],
                "representante1_nombre": empresa[4],
                "representante1_apellido": empresa[5],
                "representante1_telefono": empresa[6],
                "representante1_correo": empresa[7],
                "representante2_nombre": empresa[8],
                "representante2_apellido": empresa[9],
                "representante2_telefono": empresa[10],
                "representante2_correo": empresa[11],
                "apoderado_nombre": empresa[12],
                "apoderado_apellido": empresa[13],
                "apoderado_telefono": empresa[14],
                "apoderado_correo": empresa[15],
                "cp": empresa[16],
                "estado": empresa[17],
                "ciudad": empresa[18],
                "direccion": empresa[19],
                "numero_cuenta": cuentas[0] if cuentas else "No disponible",
                "clabe": cuentas[1] if cuentas else "No disponible"
            }

            # Obtener las partidas y calcular subtotales dinámicamente
            partidas = MyOrdendeCompra.get_partidas_by_orden_id(db, id)
            for partida in partidas:
                partida['total'] = float(partida['cantidad']) * float(partida['precio_unitario'])

            subtotal = sum(partida['total'] for partida in partidas if partida['total'])
            descuento = subtotal * (porcentaje_descuento / 100)  # Calcular descuento según el porcentaje
            subtotal_descuento = subtotal - descuento
            iva = subtotal_descuento * 0.16
            total = subtotal_descuento + iva

            # Generar contenido HTML
            html_content = render_template(
                'orden_compra_pdf.html',
                requisicion=MyOrdendeCompra.get_requisicion_by_id(db, id_requisicion),
                partidas=partidas,
                proveedor=MyOrdendeCompra.get_proveedor_by_id(db, proveedor_id),
                contactos=MyOrdendeCompra.get_contactos_by_proveedor_id(db, proveedor_id),
                base64_logo=base64.b64encode(open('static/img/Bauart-Logo-Pantalla-RGB.MED.jpg', 'rb').read()).decode('utf-8'),
                subtotal=subtotal,
                descuento=descuento,
                subtotal_descuento=subtotal_descuento,
                iva=iva,
                total=total,
                fecha_hora_entrega=fecha_hora_entrega,
                direccion_entrega=direccion_entrega,
                contacto=contacto,
                telefono=telefono,
                empresa=empresa_datos,
                porcentaje_descuento=porcentaje_descuento  # Agregar el porcentaje al render
            )

            # Generar PDF
            pdf_options = {
                'page-size': 'A4',
                'margin-top': '10mm',
                'margin-right': '10mm',
                'margin-bottom': '10mm',
                'margin-left': '10mm',
                'encoding': "UTF-8",
                'enable-local-file-access': True
            }

            pdf = pdfkit.from_string(html_content, False, options=pdf_options)

            return pdf

        except Exception as e:
            raise Exception(f"Error al generar el PDF: {str(e)}")
