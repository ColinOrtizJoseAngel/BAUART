from flask import Flask, render_template, request, url_for,redirect, flash, jsonify
from database import db_sql_server
from flask_wtf.csrf import CSRFProtect


# Configuracion
from config import config

# Models
from models.ModelEmpresas import ModelEmpresas
from  models.ModelClientes import Modelclientes
from models.ModelCategoria import ModelCategoria
from models.ModelPuesto import ModelPuesto
from models.ModelBanco import ModelBanco
from models.ModelRegistroPatronal import ModelRegistroPatronal

# Entities
from models.entities.Empresas import Empresas
from models.entities.Clientes import Clientes
from models.entities.Categoria import Categoria
from models.entities.Puestos import Puesto
from models.entities.Banco import Banco
from models.entities.RegistroPatronal import ResgistroPatronal

app = Flask(__name__)

# CONEXIÓN BASE DE DATOS
db = db_sql_server.get_connection()

csrf = CSRFProtect()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/Periodos')
def periodos():
    return render_template('periodos.html')

@app.route('/Empresas', methods=['GET', 'POST'])
def empresas():
    if request.method == 'POST':
        repse = request.form.get('REPSE', '')
        razon_social = request.form.get('RAZON_SOCIAL', '')
        rfc = request.form.get('RFC', '')
        noregis1 = request.form.get('NOREGIS1', '')
        cp = request.form.get('CP', '')
        estado = request.form.get('ESTATUS', '')

        empresas = ModelEmpresas.filter_empresas(db, repse, razon_social, rfc, noregis1, cp,estado)
        return render_template('empresas.html', empresas=empresas)
    
    
    empresa = ModelEmpresas.get_all_empresas(db)
    print(f"Estas son las empresas{empresa}")
    return render_template('empresas.html', empresas=empresa)



@app.route('/edit_empresa/<int:id>', methods=['GET', 'POST'])
def edit_empresa(id):

    if request.method == 'POST':
        empresa = Empresas(
            id=id,
            repse=request.form['REPSE'],
            razon_social=request.form['RAZON_SOCIAL'],
            rfc=request.form['RFC'],
            noregis1="",
            nombre_representante1=request.form['NOMBRE_REPRESENTANTE1'],
            apellido_representante1=request.form['APELLIDO_REPRESENTANTE1'],
            telefono_representante1=request.form['TELEFONO_REPRESENTANTE1'],
            correo_representante1=request.form['CORREO_REPRESENTANTE1'],
            cp=request.form['CP'],
            reg_fiscal=request.form['REG_FISCAL'],
            nombre_representante2=request.form.get('NOMBRE_REPRESENTANTE2', ""),
            apellido_representante2=request.form.get('APELLIDO_REPRESENTANTE2', ""),
            telefono_representante2=request.form.get('TELEFONO_REPRESENTANTE2', ""),
            correo_representante2=request.form.get('CORREO_REPRESENTANTE2', ""),
            nombre_apoderado=request.form.get('NOMBRE_APODERADO', ""),
            apellido_apoderado=request.form.get('APELLIDO_APODERADO', ""),
            telefono_apoderado=request.form.get('TELEFONO_APODERADO', ""),
            correo_apoderado=request.form.get('CORREO_APODERADO', ""),
            noregis2="",
            noregis3="",
            noregis4="",
            estado=request.form.get('ESTADO', ""),
            ciudad=request.form.get('CIUDAD', ""),
            direccion=request.form.get('DIRECCION', "")
        )
        ModelEmpresas.update_empresa(db, empresa)
        return redirect(url_for('empresas'))
    
    empresa = ModelEmpresas.get_empresa_by_id(db, id)
    registrosPatronales = ModelRegistroPatronal.get_RegistroPatronal_empresa(db,empresa.id)
    print(f"Esta es la empresa a editar {empresa}")
    return render_template('edit_empresa.html', empresa=empresa, registrosPatronales=registrosPatronales)

@app.route('/block_empresa/<int:id>', methods=['POST'])
def block_empresa(id):
    if request.method == 'POST':
        try:
            print("BLOQUA EMPRESA")
            ModelEmpresas.change_status(db, id, True)
            return redirect(url_for('empresas'))
        except Exception as e:
            print(e)
            return redirect(url_for('empresas'))

@app.route('/unblock_empresa/<int:id>', methods=['POST'])
def unblock_empresa(id):
    if request.method == 'POST':
        try:
            print("DESBLOQUA EMPRESA")
            ModelEmpresas.change_status(db, id, False)
            return redirect(url_for('empresas'))
        except Exception as e:
            print(e)
            return redirect(url_for('empresas'))


@app.route('/Altaempresas',methods=['GET', 'POST'])
def altaempresas():
    if request.method == 'POST':
        new_empresa = Empresas(
            id=0, 
            repse=request.form['REPSE'],
            razon_social=request.form['RAZON_SOCIAL'],
            rfc=request.form['RFC'],
            noregis1="",
            nombre_representante1=request.form['NOMBRE_REPRESENTANTE1'],
            apellido_representante1=request.form['APELLIDO_REPRESENTANTE1'],
            telefono_representante1=request.form['TELEFONO_REPRESENTANTE1'],
            correo_representante1=request.form['CORREO_REPRESENTANTE1'],
            cp=request.form['CP'],
            reg_fiscal=request.form['REG_FISCAL'],
            nombre_representante2=request.form.get('NOMBRE_REPRESENTANTE2', ""),
            apellido_representante2=request.form.get('APELLIDO_REPRESENTANTE2', ""),
            telefono_representante2=request.form.get('TELEFONO_REPRESENTANTE2', ""),
            correo_representante2=request.form.get('CORREO_REPRESENTANTE2', ""),
            nombre_apoderado=request.form.get('NOMBRE_APODERADO', ""),
            apellido_apoderado=request.form.get('APELLIDO_APODERADO', ""),
            telefono_apoderado=request.form.get('TELEFONO_APODERADO', ""),
            correo_apoderado=request.form.get('CORREO_APODERADO', ""),
            noregis2="",
            noregis3="",
            noregis4="",
            estado=request.form.get('ESTADO', ""),
            ciudad=request.form.get('CIUDAD', ""),
            direccion=request.form.get('DIRECCION', "")
        )

       

        estados = request.form.getlist('estado[]')
        registros_patronales = request.form.getlist('noRegistro[]')

        print(estados)
        print(registros_patronales)
        
        for r in registros_patronales:
            for e in estados:
                nuevo_regis = ResgistroPatronal(id_registro=0,
                                                registro_patronal= r,
                                                empresa= request.form['ID_EMPRESA'],
                                                estado= e
                )

            ModelRegistroPatronal.newRegistroPatronal(db,nuevo_regis)

        
        ModelEmpresas.crearEmpresa(db, new_empresa)
        return redirect(url_for('empresas'))

    else:
        ultima_empresa = ModelEmpresas.get_empresa_last_by_id(db)
        ultima_empresa = ultima_empresa + 1
        print(f"Estas es la ultima empresa{ultima_empresa}")
        return render_template('altaEmpresas.html',numero_empresa = ultima_empresa)

#REGISTROS PATRONALES
@app.route('/RegistosPatronales', methods=['GET', 'POST'])
def registosPatronales():
    if request.method == 'POST':
        new_regis_patronal = ResgistroPatronal(id_registro=0,
                                  registro_patronal=request.form['NO_REGISTRO_PATRONAL'],
                                  empresa=request.form['EMPRESA'],
                                  estado=request.form['ESTADO_REGISTRO']
                                  )
        
      
        ModelRegistroPatronal.newRegistroPatronal(db,new_regis_patronal)
        return redirect(url_for('registosPatronales'))
        
        
    empresas = ModelEmpresas.get_all_empresas(db)
    regis_patronales = ModelRegistroPatronal.get_all_registroPatronal(db)
    for r in regis_patronales:
        print(f"ESTAS CON LAC CATEGORIAS {r.empresa}")
    
    return render_template('registrosPatronales.html', regis_patronales = regis_patronales, empresas=empresas)

# EDIT REGISTRO PATRONAL
@app.route('/edit_registro_patronal/<int:id>', methods=['GET', 'POST'])
def edit_registro_patronal(id):
    if request.method == 'POST':
        regis_patronal = ResgistroPatronal(
            id_registro = id,
            registro_patronal=request.form['NO_REGISTRO_PATRONAL'],
            empresa=request.form['ID_EMPRESA'],
            estado= request.form['ESTADO_REPRESENTANTE']   
        )
        
        print(f"ESTA ES LA CATEGORIA{regis_patronal.id_registro}")
        ModelRegistroPatronal.update_registro_patronal(db, regis_patronal)
        return redirect(url_for(''))
    
@app.route('/Altacliente',methods=['GET', 'POST'])
def altaclientes():

    if request.method == 'POST':
        cliente = Clientes(id = 0,
                           razon_social=request.form['RAZON_SOCIAL'],
                           rfc=request.form['RFC'],
                           empresa=request.form['EMPRESA'],
                           cp=request.form['CP'],
                           estado=request.form['ESTADO'],
                           municipio=request.form['MUNCICIPIO'],
                           pais=request.form['PAIS'],
                           calle=request.form['CALLE'],
                           nombre_contacto=request.form['NOMBRE_CONTACTO1'],
                           apellido_contacto=request.form['APELLIDO_CONTACTO1'],
                           telefono_contacto=request.form['TELEFONO_CONTACTO1'],
                           correo_contacto=request.form['CORREO_CONTACTO1'],
                           responsable_proyecto=request.form['RESPONSABLE_PROYECTO_DIRECTORIO'],
                           telfono_responsable_proyecto= request.form['TELEFONO_DIRECTORIO'],
                           correo_responsable_proyecto=request.form['CORREO_CONTATO_DIRECTORIO'],
                           contacto_emergencia= request.form['EMERGENCIA_CONTATO_DIRECTORIO'],
                           puesto_empresa=request.form['PUESTO_CONTACTO_DIRECTROIO'],
                           regimen_fiscal=request.form['REGIMEN_FISCAL'],
                           uso_cfdi=request.form['USO_CFDI'],
                           forma_pago=request.form['FORMA_PAGO'],
                           dias_credito=request.form['DIAS_CREDITO'],
                           banco=request.form['BANCO'],
                           cuenta_banco=request.form['CUENTA_BANCARIA'],
                           clabe=request.form['CLABE'],
                           no_Exterior=request.form.get('NO_EXTERIOR', ""),
                           no_Interior=request.form.get('NO_INTERIOR', ""))

        Modelclientes.crearCliente(db, cliente)
        return redirect(url_for('clientes'))
    
    empresas = ModelEmpresas.get_empresas_not_block(db)
    return render_template('altaClientes.html',empresas=empresas)

@app.route('/edit_cliente/<int:id>', methods=['GET', 'POST'])
def edit_cliente(id):
    if request.method == 'POST':
        clientes = Clientes(id = 0,
                           razon_social=request.form['RAZON_SOCIAL'],
                           rfc=request.form['RFC'],
                           empresa=request.form['EMPRESA'],
                           cp=request.form['CP'],
                           estado=request.form['ESTADO'],
                           municipio=request.form['MUNCICIPIO'],
                           pais=request.form['PAIS'],
                           calle=request.form['CALLE'],
                           nombre_contacto=request.form['NOMBRE_CONTACTO1'],
                           apellido_contacto=request.form['APELLIDO_CONTACTO1'],
                           telefono_contacto=request.form['TELEFONO_CONTACTO1'],
                           correo_contacto=request.form['CORREO_CONTACTO1'],
                           responsable_proyecto=request.form['RESPONSABLE_PROYECTO_DIRECTORIO'],
                           telfono_responsable_proyecto= request.form['TELEFONO_DIRECTORIO'],
                           correo_responsable_proyecto=request.form['CORREO_CONTATO_DIRECTORIO'],
                           contacto_emergencia= request.form['EMERGENCIA_CONTATO_DIRECTORIO'],
                           puesto_empresa=request.form['PUESTO_CONTACTO_DIRECTROIO'],
                           regimen_fiscal=request.form['REGIMEN_FISCAL'],
                           uso_cfdi=request.form['USO_CFDI'],
                           forma_pago=request.form['FORMA_PAGO'],
                           dias_credito=request.form['DIAS_CREDITO'],
                           banco=request.form['BANCO'],
                           cuenta_banco=request.form['CUENTA_BANCARIA'],
                           clabe=request.form['CLABE'],
                           no_Exterior=request.form.get('NO_EXTERIOR', ""),
                           no_Interior=request.form.get('NO_INTERIOR', ""))
        Modelclientes.update_cliente(db, clientes)
        return redirect(url_for('clientes'))
    
    cliente = Modelclientes.get_cliente_by_id(db, id)
    empresa_selecionada = ModelEmpresas.get_empresa_by_id(db, cliente.empresa)
    empresas = ModelEmpresas.get_all_empresas(db)
    print(f"Esta es la empresa actual {empresa_selecionada.razon_social}")
    return render_template('edit_cliente.html', cliente=cliente, empresas = empresas, empresa_selecionada=empresa_selecionada)

@app.route('/Clientes',  methods=['GET', 'POST'])
def clientes():
    cliente = Modelclientes.get_all_clientes(db)
    print(f"Estas son las cliente{cliente}")
    return render_template('clientes.html', clientes=cliente)


@app.route('/block_cliente/<int:id>', methods=['POST'])
def block_cliente(id):
    if request.method == 'POST':
        try:
            print("BLOQUA ClIENTE")
            Modelclientes.change_status(db, id, True)
            return redirect(url_for('clientes'))
        except Exception as e:
            print(e)
            return redirect(url_for('clientes'))

@app.route('/unblock_cliente/<int:id>', methods=['POST'])
def unblock_cliente(id):
    if request.method == 'POST':
        try:
            Modelclientes.change_status(db, id, False)
            return redirect(url_for('clientes'))
        except Exception as e:
            print(e)
            return redirect(url_for('clientes'))
#CATEGORIAS

@app.route('/Categorias', methods=['GET', 'POST'])
def categorias():
    if request.method == 'POST':
        new_categoria = Categoria(idCategoria=0,
                                  categoria=request.form['CATEGORIA'])
        
        ModelCategoria.newCategoria(db,new_categoria)
        return redirect(url_for('categorias'))
        
   
    categorias = ModelCategoria.get_all_categorias(db)
    print(f"ESTAS CON LAC CATEGORIAS {categorias}")
    for c in categorias:
        print(f"HOAL ESTA ES LA CATEGORIA: {c._is_blocked}")
    return render_template('Categorias.html', categorias = categorias)

#BLOCK CATEGORIA
@app.route('/block_categoria/<int:id>', methods=['POST'])
def block_categoria(id):
    if request.method == 'POST':
        try:
            print("BLOQUEA CATEGORIA")
            ModelCategoria.change_status(db, id, True)
            return redirect(url_for('categorias'))
        except Exception as e:
            print(e)
            return redirect(url_for('categorias'))

#UNBLOCK CATEGORIA
@app.route('/unblock_categoria/<int:id>', methods=['POST'])
def unblock_categoria(id):
    if request.method == 'POST':
        try:
            print("BLOQUEA CATEGORIA")
            ModelCategoria.change_status(db, id, False)
            return redirect(url_for('categorias'))
        except Exception as e:
            print(e)
            return redirect(url_for('categorias'))

# EDIT CATEGORIA
@app.route('/edit_categoria/<int:id>', methods=['GET', 'POST'])
def edit_categoria(id):
    if request.method == 'POST':
        categoria = Categoria(
            idCategoria=id,
            categoria=request.form['EDIT_CATEGORIA']
        )
        
        print(f"ESTA ES LA CATEGORIA{categoria.idCategoria}")
        ModelCategoria.update_categoria(db, categoria)
        return redirect(url_for('categorias'))
    
    categoria = ModelCategoria.get_categoria_by_id(db, id)
    print(f"Esta es la empresa a editar {categoria.categoria}")
    
    return render_template('edit_categoria.html')

#BANCOS
@app.route('/Bancos', methods=['GET', 'POST'])
def bancos():
    if request.method == 'POST':
        new_banco = Banco(id_banco= 0,
                      banco = request.form['BANCO'])
        
        ModelBanco.newBanco(db,new_banco)
        return redirect(url_for('bancos'))
        
   
    bancos = ModelBanco.get_all_banco(db)
    print(f"ESTAS CON LAC CATEGORIAS {bancos}")
   
    return render_template('Bancos.html', bancos = bancos)

#PUESTO
@app.route('/Puestos', methods=['GET','POST'])
def puestos():
    if request.method == 'POST':
        new_puesto = Puesto(
    ent_IdPuesto=0,
    ent_IdCategoria=request.form['id_ht_Categoria'],
    ent_Puesto=request.form['ht_Puesto'],
    ent_TipoEmpleado=request.form['ht_Tipo_Empleado'],
    ent_TipoSueldo=request.form['ht_Tipo_sueldo'],
    ent_Sueldo=float(request.form['ht_Sueldo'].replace(',', '').replace('$', '').strip()),
    ent_SueldoDiario=float(request.form['ht_Sueldo_diario'].replace(',', '').replace('$', '').strip()),
    ent_SueldoMensual=float(request.form['ht_Sueldo_mensual'].replace(',', '').replace('$', '').strip()),
    ent_SueldoIMSS=float(request.form['ht_Sueldo_imss'].replace(',', '').replace('$', '').strip()),
    ent_SueldoMonedero=float(request.form['ht_Sueldo_monedero'].replace(',', '').replace('$', '').strip()),
    ent_HoraExtra=float(request.form['ht_horas_extra'].replace(',', '').replace('$', '').strip())
    #ent_HoraExtra=request.form['ht_Horas_extra']
)
        puestos = ModelPuesto.crearPuesto(db,new_puesto)
        return redirect(url_for('puestos'))
    
    puestos = ModelPuesto.get_all_puestos(db)
    return render_template('puestos.html', puestos=puestos)

@app.route('/home1')
def home1():
    return render_template('layout copy.html')


if __name__ == '__main__':

    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.run()
