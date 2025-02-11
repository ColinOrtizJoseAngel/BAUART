document.addEventListener("DOMContentLoaded", function () {
    var inputPROYECTO = document.querySelector("#PROYECTO");
    var inputPROYECTO_ID = document.querySelector("#PROYECTO_ID");
    var inputFECHA_INICIO = document.querySelector("#FECHA_INICIO");
    var inputFECHA_FIN = document.querySelector("#FECHA_FIN");
    var input_Id_Cliente = document.querySelector("#CLIENTE_ID");
    var inputDIAS_TOTALES = document.querySelector("#DIAS_TOTALES"); // Nuevo input para mostrar los días totales
  
  
    if (inputPROYECTO) {
      configurar_autocompletado(
        inputPROYECTO,
        inputPROYECTO_ID,
        inputFECHA_INICIO,
        inputFECHA_FIN,
        inputDIAS_TOTALES,
        input_Id_Cliente
      );
    }
  });
  
  function configurar_autocompletado(
    inputPROYECTO,
    inputPROYECTO_ID,
    inputFECHA_INICIO,
    inputFECHA_FIN,
    inputDIAS_TOTALES,
    inputCLIENTE_ID
  ) {
    var proyectosDisponibles = [];
    var opcionSeleccionada = false;
  
    inputPROYECTO.addEventListener("input", function () {
      var val = this.value;
  
      cerrarListaAutocompletado();
      opcionSeleccionada = false;
  
      if (!val) {
        inputCLIENTE_ID.value = "";
        inputPROYECTO.value = "";
        inputPROYECTO_ID.value = "";
        inputFECHA_INICIO.value = "";
        inputFECHA_FIN.value = "";
        inputDIAS_TOTALES.value = ""; // Limpiar el campo de días totales también
        return false;
      }
  
  
      fetch(`/api/buscar_proyecto/?query=${val}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
  
          proyectosDisponibles = data;
          var divItems = document.querySelector("#suggestions");
  
          if (divItems) {
            divItems.innerHTML = "";
            data.forEach((proyectoData) => {
              var proyecto = proyectoData.nombre_proyecto;
              var id = proyectoData.id;
              var fechainicio = proyectoData.fecha_inicio;
              var fechafin = proyectoData.fecha_fin;
              var totalSemanas = proyectoData.semanas;
              var id_cliente = proyectoData.id_cliente;
     
              var regex = new RegExp(`(${val})`, "gi");
              var item = document.createElement("div");
              item.classList.add("list-group-item");
  
              item.innerHTML = proyecto.replace(regex, "<strong style='font-size: 14px;font-family: arial;'>$1</strong>");
              item.innerHTML += `<input type='hidden' value='${proyecto}' data-cliente='${id_cliente}' data-id='${id}'  data-fecha-inicio='${fechainicio}' data-fecha-fin='${fechafin}'>`;
  
              item.addEventListener("click", function () {
               
                inputPROYECTO.value = this.querySelector("input").value;
                
                inputCLIENTE_ID.value = 
                  this.querySelector("input").getAttribute("data-cliente");
  
                inputPROYECTO_ID.value =
                  this.querySelector("input").getAttribute("data-id");
             
                inputFECHA_INICIO.value =
                  this.querySelector("input").getAttribute("data-fecha-inicio");
                inputFECHA_FIN.value =
                  this.querySelector("input").getAttribute("data-fecha-fin");
  
                
                inputDIAS_TOTALES.value = totalSemanas; // Asignar la diferencia de días al input correspondiente
  
                opcionSeleccionada = true;
                cerrarListaAutocompletado();
              });
  
              divItems.appendChild(item);
            });
          } else {
            
          }
        })
        .catch((error) => console.error("Error en la solicitud Fetch:", error));
    });
  
    inputPROYECTO.addEventListener("blur", function () {
      setTimeout(() => {
        if (!opcionSeleccionada) {
          inputPROYECTO.value = "";
          inputCLIENTE_ID.value = "";
          inputFECHA_INICIO.value = "";
          inputFECHA_FIN.value = "";
          inputDIAS_TOTALES.value = ""; // Limpiar el campo de días totales también
        }
      }, 200);
    });
  
    function cerrarListaAutocompletado() {
      var items = document.querySelectorAll("#suggestions .list-group-item");
      items.forEach((item) => item.remove());
    }
  
    document.addEventListener("click", function (e) {
      if (
        !e.target.matches("#PROYECTO") &&
        !e.target.matches("#suggestions") &&
        !e.target.closest("#suggestions")
      ) {
        cerrarListaAutocompletado();
      }
    });
  }

  function añadirConcepto() {
    
    var tabla = document.getElementById("DETALLE_PRESUPUESTO");
    var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
    var contador = cuerpoTabla.rows.length + 1;
    var newRow = cuerpoTabla.insertRow(); // Inserta la nueva fila al final
  
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);
    var cell7 = newRow.insertCell(6);
    var cell8 = newRow.insertCell(7);
    var cell9 = newRow.insertCell(8);
    
  
  
    cell1.innerHTML = `
    `;
  
    cell2.innerHTML = `
    <input type="text" class="form-control borderless text-center" style="display: none" id="ID_PARTIDA_${contador}" name="ID_PARTIDAS_NV[]" value="${contador}" readonly>
  
    <input type="text" class="form-control" id="INPUT_ESPECIALIDADES_${contador}" name="ESPECIALIDADES_NV[]" autocomplete="off" required>
    <input type="text" class="form-control" style="display: none" id="INPUT_ID_ESPECIALIDADES" name=ID_ESPECIALIDADES_NV[]>
    <div class="autocomplete-items"></div>
    <div class="invalid-feedback">
        SELECT A ESPECIALIDAD
    </div>`;
  
    cell3.innerHTML = `
      <div class="oculto" id="contenedor_boton_subpresupuesto_${contador}">
          <button type="button" class="btn botones" id="boto_modal_subpresupuesto${contador}" data-bs-toggle="modal" data-bs-target="#modalPresupuesto_${contador}">
            VER PRESUPUESTO BAUART
        </button>
      </div>
      <select class="form-control" id="INPUT_PROVEEDOR_${contador}" name="PROVEEDOR_NV[]" onchange="sub_presupuesto(this,${contador})">
          <option value="">SELECIONA UN PROVEEDOR</option>
          
      </select>
      <input type="text" class="form-control" style="display: none" id="INPUT_ID_PROVEEDOR" name="ID_PROVEDOR">
      <div class="invalid-feedback">
          Selecciona un proveedor
      </div>
      `;
  
    cell4.innerHTML = `
    <input type="text" class="form-control currency-input presupuesto-cliente" id="PRESUPUESTO_CLIENTE_${contador}" name="PRESUPUESTO_CLIENTE_NV[]" placeholder="$0.00" onchange="concular_diferecnia()">
  `;
  
    cell5.innerHTML = `
    <input type="text" class="form-control currency-input presupuesto-proveedor" id="PRESUPUESTO_PROVEEDOR_${contador}" name="PRESUPUESTO_PROVEEDOR_NV[]" placeholder="$0.00" onchange="concular_diferecnia()">
  `;
  
    cell6.innerHTML = `
      <input type="text" class="form-control currency-input presupuesto-diferencia" id="DIFERENCIA_${contador}" name="DIFERENCIA_NV[]" onchange="concular_diferencia()" placeholder="$0.00" readonly>
  `;
  
    cell7.innerHTML = `
  <select style="text-align: center;"  id="CONTRATO_FIRMADO_${contador}" name="CONTRATO_FIRMADO_NV[]" onchange="validarContratosPresupuesto()" class="form-control" >
      <option value=1>SÍ</option>
      <option value=0>NO</option>
  </select>
  <div class="invalid-feedback">
      Completa el banco
  </div>
  `;
  
    cell8.innerHTML = `
    <select name="STATUS_NV[]"  id="STATUS_${contador}" onchange="validarEstatusPresupuesto()" class="form-control">
        <option value="0">PRESUPUESTO CARGADO</option>
        <option value="1">APROBADO POR DIRECTOR</option>
    </select>
    `;
  
    cell9.innerHTML = `
  <div class="d-flex align-items-center justify-content-center">
    <button type="button" onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i></button>
  </div>
  `;
    
    
    configurar_autocompletado_especialida(newRow,contador);
    validarEstatusPresupuesto();
    actualizarNumeracion();

}




  
  
  // Añadir concepto nomina BAUART
  function añadir_concepto_sub(id,es_nomina) {
  
    var tabla = document.getElementById(`tablasub_${id}`);
    var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
    var contador = cuerpoTabla.rows.length + 1;
    var newRow = cuerpoTabla.insertRow(); // Inserta la nueva fila al final
  
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);
    var cell7 = newRow.insertCell(6);
    var cell8 = newRow.insertCell(7);


  
  
   
  
    //Si agrega una partida de nomina
    if (es_nomina) { 
      
      cell1.innerHTML = `
      `;
    
      cell2.innerHTML = `
      <input type="text" class="form-control" id="INPUT_ESPECIALIDADES_SUB_${id}-${contador}" name="ESPECIALIDADES_SUB-${id}[]" autocomplete="off" required>
      <input type="text" class="form-control" style="display: none" id="INPUT_ID_ESPECIALIDADES_SUB_${id}-${contador}" name="INPUT_ID_ESPECIALIDADES_SUB_${id}[]">
      <input type="text" class="form-control" style="display: none" id="IS_NOMINA_${contador}[]" name="IS_NOMINA_${id}[]" value='1'>
  
      <div class="autocomplete-items"></div>
      <div class="invalid-feedback">
          Selecciona una especialidad
      </div>`;
    
      cell3.innerHTML = `
        
        <select class="form-control" id="SELECT_PROVEEDOR_SUB_${id}-${contador}" name="" onchange="colocarSueldo(this,${contador},${id})">
            <option value="" style="text-align: center";>SELECCIONA UN PUESTO</option>
         
        </select>
        <input type="text" class="form-control" style="display: none" name="PROVEEDOR_SUB-${id}[]">
        <div class="invalid-feedback">
            Selecciona un proveedor
        </div>
        `;
    
      cell4.innerHTML = `
      <input type="text" class="form-control currency-input presupuesto-cliente"  id="SUB_PRESUPUESTO_CLIENTE-${id}-${contador}" name="SUB_PRESUPUESTO_CLIENTE-${id}[]" placeholder="$0.00" onchange="sub_cular_diferecnia(${id})">
    `;
      
    cell5.innerHTML = `
        <input type="text" class="form-control currency-input presupuesto-proveedor"  name="SUB_PRESUPUESTO_PROVEEDOR-${id}[]" placeholder="$0.00" onchange="sub_cular_diferecnia(${id})">
      `;
  
      cell6.innerHTML = `
          <input type="text" class="form-control currency-input presupuesto-diferencia" name="SUB_DIFERENCIA-${id}[]" placeholder="$0.00" readonly>
      `;
      
      cell7.innerHTML = `
      <select id="STATUS" name="SUB_STATUS-${id}[]" class="form-control">
                                    <option value="1">PRESUPUESTO CARGADO</option>
                                    <option value="2">APROBADO POR DIRECTOR</option>
                                </select>
      `;                      
  
      cell8.innerHTML = `
      <div class="d-flex align-items-center justify-content-center">
        <button type="button" onclick="sub_eliminarFila(this,${contador})" class="btn"><i class="bi bi-trash"></i></button>
      </div>
      `;
      
      configurar_autocompletado_especialida_sub(newRow,contador,id,true);
  
    } 
    else {
      cell2.innerHTML = `
      <input type="text" class="form-control" id="INPUT_ESPECIALIDADES_SUB_${id}-${contador}" name="ESPECIALIDADES_SUB-${id}[]" autocomplete="off" required>
      <input type="text" class="form-control" style="display: none" id="INPUT_ID_ESPECIALIDADES_SUB_${id}-${contador}" name="INPUT_ID_ESPECIALIDADES_SUB_${id}[]">
      <input type="text" class="form-control" style="display: none" id="IS_NOMINA_${id}-${contador}" value='0' name="IS_NOMINA_${id}[]" >
  
      <div class="autocomplete-items"></div>
      <div class="invalid-feedback">
          Selecciona una especialidad
      </div>`;
    
      cell3.innerHTML = `
        
        <select class="form-control" id="SELECT_PROVEEDOR_SUB_${id}-${contador}" name="">
            <option value="" style="text-align: center";>SELECIONA UN PROVEEDOR</option>
        </select>
        <input type="text" class="form-control" style="display: none" name="PROVEEDOR_SUB-${id}[]">
        <div class="invalid-feedback">
            SELECIONA UN PROVEEDOR
        </div>
        `;
    
      cell4.innerHTML = `
          <input type="text" class="form-control currency-input presupuesto-cliente"  name="SUB_PRESUPUESTO_CLIENTE-${id}[]" placeholder="$0.00" onchange="sub_cular_diferecnia(${id})">
        `;
  
      cell5.innerHTML = `
        <input type="text" class="form-control currency-input presupuesto-proveedor"  name="SUB_PRESUPUESTO_PROVEEDOR-${id}[]" placeholder="$0.00" onchange="sub_cular_diferecnia(${id})">
      `;
  
      cell6.innerHTML = `
          <input type="text" class="form-control currency-input presupuesto-diferencia" name="SUB_DIFERENCIA-${id}[]" placeholder="$0.00" readonly>
      `;
  
      cell7.innerHTML = `
      <select id="STATUS" name="SUB_STATUS-${id}[]" class="form-control">
                                    <option value="1">PRESUPUESTO CARGADO</option>
                                    <option value="2">APROBADO POR DIRECTOR</option>
                                </select>
      `;                      
  
      cell8.innerHTML = `
      <div class="d-flex align-items-center justify-content-center">
        <button type="button" onclick="sub_eliminarFila(this,${contador})" class="btn"><i class="bi bi-trash"></i></button>
      </div>
      `;
  
      configurar_autocompletado_especialida_sub(newRow,contador,id,false);
      
    }
    
    actualizarNumeracionsub(id);
  }
  
  
  function sub_presupuesto(select, id) {
   
    proveedorSeleccionado = select.value;
  
    // SI SE SELECIONA BAUART
    if (proveedorSeleccionado == 0) {
      const modalContainer = document.getElementById("subpresupuestos");
      const modalHTML = `
      <!-- Modal -->
      <div class="modal fade modal-xl" id="modalPresupuesto_${id}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"  data-bs-backdrop="static" data-bs-keyboard="false">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title" id="exampleModalLabel">PRESUPUESTO BAUART</h4>
            </div>
            <div class="modal-body">
              <div class="form-group row">
                  <!-- PROYECTO -->
                  <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
                      <strong><span id="PROYECTO_SUBPRESUPUESTO"> </span></strong> 
                       <input type="text"  class="form-control oculto" id="INPUT_NOMBRE_DIRECTOR_${id}" readonly>
                  </div>
              </div>
              <div class="form-group row">
                  <!--DIRECION DE OBRA-->
                  <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
                      <strong><span id="DIRECCION_${id}"> </span></strong> 
                      <input type="text"  class="form-control oculto" id="INPUT_DIRECCION_${id}" readonly>
                  </div> 
              </div>
              <div class="form-group row">
                  <!-- DIRECTOR -->
                  <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
                      <strong><span id="NOMBRE_DIRECTOR_${id}"> </span></strong> 
                      <input type="text"  class="form-control oculto" id="INPUT_NOMBRE_DIRECTOR_${id}" readonly>
                  </div>
              </div>
              <div class="form-group row">
                  <!-- PRESUPUESTO -->
                  <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
                       <strong><span id="NOMBRE_PRESUPUESTO_${id}"> </span></strong> 
                      <input type="text"  class="form-control oculto" id="INPUT_NOMBRE_PREPUSPUESTO_${id}" name="NOMBRE_SUB-${id}" readonly>
                  </div>
              </div>
              <div class="container-fluid">
                  <br>
                  <div class="d-grid gap-2 d-md-flex justify-content-start">
                    <button type="button" class="btn botones add-row-btn" onclick="añadir_concepto_sub(${id},false)">AGREGAR PARTIDA</button>
                    
                    <button type="button" class="btn boton-nomina add-row-btn" onclick="añadir_concepto_sub(${id},true)">AGREGAR NOMINA</button>
                    
                  </div>
                  
                  <br>
                  <div class="table-presupuesto_sub">
                      <table id="tablasub_${id}" class="table tabla-subpresupuesto table-hover table-borderless">
                          <colgroup>
                              <!-- Agrega más columnas según sea necesario -->
                              <col style="width: 40px;"> <!-- Primera columna -->
                              <col style="width: 400px;"> <!-- Segunda columna -->
                              <col style="width: 200px;"> <!-- Tercera columna -->
                              <col style="width: 130px;"> <!-- Cuarta columna -->
                              <col style="width: 130px;"> <!-- Quinta columna -->
                              <col style="width: 130px;"> <!-- Sexta columna -->
                              <col style="width: 200px;"> <!-- Novena columna -->
                              <col style="width: 50px;"> <!-- Decima columna -->
                              <!-- Añade más columnas si es necesario -->
                          </colgroup>
                          <thead class="thead-dark" style="text-align: center;">
                              <tr>
                                  <th style="white-space: normal;word-wrap: break-word;">NO</th>
                                  <th>PARTIDA PRESUPUESTAL</th>
                                  <th>CONTRATISTA / PROVEEDOR</th>
                                  <th  style="white-space: normal;word-wrap: break-word;">PRESUPUESTO CLIENTE COSTO DIRECTO IVA INC.</th>
                                  <th  style="white-space: normal;word-wrap: break-word;">PRESUPUESTO CONTRATISTAS IVA INC.</th>
                                  <th  style="white-space: normal;word-wrap: break-word;">DIFERENCIA PRESUPUESTOS</th>
                                  <th>ESTATUS</th>
                                  <th></th>
                                  <!-- Agrega más encabezados si es necesario -->
                              </tr>
                          </thead>
                          <tbody>
                              
                          </tbody>
                          <tfoot>
                              <!-- Pie de tabla -->
                              
                              <tr>
                                  <td colspan="2"></td>
                                  <td  class="text-end"><strong>SUBTOTAL:</strong></td>
                                  <td><input type="text" id="INPUT_PRESUPUESTO_CLIENTE_BAUART_${id}"  name="INPUT_PRESUPUESTO_CLIENTE_BAUART-${id}" class="form-control  currency-input" readonly></td>
                                  <td><input type="text" id="INPUT_PRESUPUESTO_CONTRATISTA_${id}"  name="INPUT_PRESUPUESTO_CONTRATISTA_BAUART-${id}" class="form-control  currency-input" readonly></td>
                                  <td><input type="text" id="INPUT_DIFERENCIA_PRESUPUESTOS_${id}" name="INPUT_DIFERENCIA_PRESUPUESTOS-${id}" class="form-control  currency-input" readonly></td>
                                  <td colspan="1"></td>
                              </tr>
              
                      </table>
                  </div>
              </div>
            </div>
           <div class="modal-footer">
              <div class="d-grid gap-2 d-md-flex justify-content-start">
                 <button type="button" class="btn botones"  data-bs-dismiss="modal" onclick="guardar_presuouesto(${id})" ><i class="bi bi-floppy"></i> CONFIRMAR</button
              </div>
            </div>
          </div>
        </div>
      </div>
      
      `;
  
       // Insertar el nuevo modal dinámicamente
       modalContainer.insertAdjacentHTML("beforeend", modalHTML);
      
      const contenedorBotones = document.getElementById(`contenedor_boton_subpresupuesto_${id}`)
      const inputPresupuestoCliente = document.getElementById(`PRESUPUESTO_CLIENTE_${id}`)
      const inputPresupuestoProveedor = document.getElementById(`PRESUPUESTO_PROVEEDOR_${id}`)
      const inputEspecialidad = document.getElementById(`INPUT_ESPECIALIDADES_${id}`)
      const tituloPresupuesto =  document.getElementById(`NOMBRE_PRESUPUESTO_${id}`) 
      const directorPrepupuesto = document.getElementById(`NOMBRE_DIRECTOR_${id}`)
      const direccionPrepupuesto = document.getElementById(`DIRECCION_${id}`)
      const inputNombreSub = document.getElementById(`INPUT_NOMBRE_PREPUSPUESTO_${id}`)
      const statuspartida = document.getElementById(`STATUS_${id}`)
     
      tituloPresupuesto.textContent  = "BAUART - " +inputEspecialidad.value 
      inputNombreSub.value =  "BAUART - " +inputEspecialidad.value 
      directorPrepupuesto.textContent = document.getElementById(`DIRECTOR`).value
      direccionPrepupuesto.textContent = document.getElementById(`DIRECCION`).value
  
      inputEspecialidad.setAttribute("readonly", true);
      inputPresupuestoCliente.setAttribute("readonly", true);
      inputPresupuestoProveedor.setAttribute("readonly", true)
      statuspartida.classList.add("readonly-select"); 
      contenedorBotones.classList.remove("oculto");
      select.classList.add("oculto")
  
      document.getElementById('PROYECTO_SUBPRESUPUESTO').value = document.getElementById('PROYECTO').value
      // Concatenamos correctamente el string del ID del modal
      const modalId = `modalPresupuesto_${id}`;
        
      $(`#${modalId}`).modal("show"); // Mostramos el modal correspondiente
    }
  }
  
  function guardar_presuouesto(id){
    const inputSubpresupuestoCliente = document.getElementById(`INPUT_PRESUPUESTO_CLIENTE_BAUART_${id}`)
    const inputSubpresuouestoContratista = document.getElementById(`INPUT_PRESUPUESTO_CONTRATISTA_${id}`)
    const inputSubpresupuestoDiferencia = document.getElementById(`INPUT_DIFERENCIA_PRESUPUESTOS_${id}`)
    const inputDetallePresupuestoCliente = document.getElementById(`PRESUPUESTO_CLIENTE_${id}`)
    const inputDetallePresupuestoContratista = document.getElementById(`PRESUPUESTO_PROVEEDOR_${id}`)
    
    console.log(inputDetallePresupuestoCliente.value)
    console.log(inputDetallePresupuestoContratista.value)


    inputDetallePresupuestoCliente.value = inputSubpresupuestoCliente.value
    inputDetallePresupuestoContratista.value  = inputSubpresuouestoContratista.value
    concular_diferecnia()
    //document.getElementById(`DIFERENCIA_${id}`).value = inputSubpresupuestoDiferencia.value


    //VERIFICAR QUE EL TODOS LOS ESTATUS ESTEN APROBADO

     // Selecciona la tabla por su ID
     var table = document.getElementById(`tablasub_${id}`);
    
     // Selecciona todas las filas del cuerpo de la tabla
     var rows = table.getElementsByTagName("tbody")[0].getElementsByTagName("tr");
    
    
    // Variable para verificar si todas las partidas están aprobadas
    let presupuesto_aprobado = true;

    // Recorrer todas las filas
    for (var i = 0; i < rows.length; i++) {
      // Obtener los selects de estatus
      var estatusSelect = rows[i].querySelector('select[name="STATUS_SUB_DB[]"]');
      var estatusSubPresupuesto = rows[i].querySelector(`select[name="SUB_STATUS-${id}[]"]`);

      // Verificar si ambos existen y si alguna fila no está aprobada
      if ((estatusSelect && estatusSelect.value !== "1") || 
          (estatusSubPresupuesto && estatusSubPresupuesto.value !== "1")) {
          presupuesto_aprobado = false;
          break;  // Si encontramos una fila no aprobada, salimos del bucle
      }
    }

    if(presupuesto_aprobado){
      // Si no se encontró ningún estatus "APROBADO POR DIRECTOR", muestra un mensaje de error
      selectEstatus = document.getElementById(`STATUS_${id}`)
      selectEstatus.value = 1
    }
    else{
      selectEstatus = document.getElementById(`STATUS_${id}`)
      selectEstatus.value = 0
    }
    
    validarEstatusPresupuesto()
  }
  
  function eliminarFila(button) {
    var row = button.closest("tr"); 
    row.parentNode.removeChild(row);
    actualizarNumeracion();
    concular_diferecnia();
  }
  
  function sub_eliminarFila(button,id) {
    var row = button.closest("tr"); 
    row.parentNode.removeChild(row);
    actualizarNumeracion();
    sub_cular_diferecnia(id)
  }
  
  
  function actualizarNumeracion() {
    var tabla = document.getElementById("DETALLE_PRESUPUESTO");
    var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
    var filas = cuerpoTabla.getElementsByTagName("tr");
  
    for (var i = 0; i < filas.length; i++) {
      var cell = filas[i].getElementsByTagName("td")[0];
      if (cell) {
        cell.textContent = i + 1;
      
      }
    }
  }
  
  function actualizarNumeracionsub(id) {
    var tabla = document.getElementById(`tablasub_${id}`);
    var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
    var filas = cuerpoTabla.getElementsByTagName("tr");
  
    for (var i = 0; i < filas.length; i++) {
      var cell = filas[i].getElementsByTagName("td")[0];
      if (cell) {
        var input = cell.querySelector("input");
        if (input) {
          input.value = i; // Asigna el número de fila (empezando en 1)
        }
        cell.textContent = i + 1;
      }
    }
  }
  
  function configurar_autocompletado_especialida_sub(row,contador,id,es_nomina) {
  
    var inputEspecialidad = row.querySelector(`#INPUT_ESPECIALIDADES_SUB_${id}-${contador}`);
    var inputIdEspecialidad = row.querySelector(`#INPUT_ID_ESPECIALIDADES_SUB_${id}-${contador}`);
    var selectProveedor = row.querySelector(`#SELECT_PROVEEDOR_SUB_${id}-${contador}`);
    var especialidadesDisponibles = [];
    var opcionSeleccionada = false;
  
    // Inicialmente deshabilitar el selectProveedor
    selectProveedor.disabled = true;
  
    if (es_nomina) {
      inputEspecialidad.addEventListener("input", function () {
        var val = this.value;
        cerrarListaAutocompletadoEspecialidad();
        opcionSeleccionada = false;
    
        if (!val) {
          inputIdEspecialidad.value = "";
          selectProveedor.innerHTML =
            '<option value="">SELECIONA UNA PUESTO</option';
          selectProveedor.disabled = true; // Deshabilitar el selectProveedor
          return false;
        }
    
    
        fetch(`/api/obtener_categorias/?query=${encodeURIComponent(val)}`)
          .then((response) => {
            if (!response.ok) {
              throw new Error("Network response was not ok");
            }
            return response.json();
          })
          .then((data) => {
            categoriasDisponibles = data;
            var divItems = row.querySelector(".autocomplete-items");
            data.forEach((categoria) => {
              var nombre = categoria.categoria;
              var id = categoria.id;
              var regex = new RegExp(`(${val})`, "gi");
              var item = document.createElement("div");
              item.classList.add("list-group-item");
              item.innerHTML = nombre.replace(regex, "<strong>$1</strong>");
              item.innerHTML += `<input type='hidden' value='${nombre}' data-id='${id}'>`;
    
              item.addEventListener("click", function () {
                inputEspecialidad.value = this.querySelector("input").value;
                inputIdEspecialidad.value =
                  this.querySelector("input").getAttribute("data-id");
                  cargarPuesto(inputIdEspecialidad.value, selectProveedor);
                opcionSeleccionada = true;
                cerrarListaAutocompletadoEspecialidad();
              });
    
              divItems.appendChild(item);
            });
          })
          .catch((error) => console.error("Error en la solicitud Fetch:", error));
      });
    
      inputEspecialidad.addEventListener("blur", function () {
        setTimeout(() => {
          if (!opcionSeleccionada) {
            inputEspecialidad.value = "";
            inputIdEspecialidad.value = "";
            selectProveedor.innerHTML =
              '<option value="" text-align: center;>SELECCIONA UN PUESTO</option>';
            selectProveedor.disabled = true; // Deshabilitar el selectProveedor
          }
        }, 200);
      });
    
    
      function cerrarListaAutocompletadoEspecialidad() {
        var items = row.querySelectorAll(".autocomplete-items div");
        items.forEach((item) => item.remove());
      }
    
      document.addEventListener("click", function (e) {
        if (!row.contains(e.target)) {
          cerrarListaAutocompletadoEspecialidad();
        }
      });
    }
  
    else {
      
      inputEspecialidad.addEventListener("input", function () {
        var val = this.value;
        cerrarListaAutocompletadoEspecialidad();
        opcionSeleccionada = false;
    
        if (!val) {
          inputIdEspecialidad.value = "";
          selectProveedor.innerHTML =
            '<option value="">SELECIONA UN PROVEEDOR</option';
          selectProveedor.disabled = true; // Deshabilitar el selectProveedor
          return false;
        }
    
    
        fetch(`/api/obtener_materiales/?query=${encodeURIComponent(val)}`)
          .then((response) => {
            if (!response.ok) {
              throw new Error("Network response was not ok");
            }
            return response.json();
          })
          .then((data) => {
            especialidadesDisponibles = data;
            var divItems = row.querySelector(".autocomplete-items");
            data.forEach((especialidad) => {
              var nombre = especialidad.nombre;
              var id = especialidad.id;
              var regex = new RegExp(`(${val})`, "gi");
              var item = document.createElement("div");
              item.classList.add("list-group-item");
              item.innerHTML = nombre.replace(regex, "<strong>$1</strong>");
              item.innerHTML += `<input type='hidden' value='${nombre}' data-id='${id}'>`;
    
              item.addEventListener("click", function () {
                inputEspecialidad.value = this.querySelector("input").value;
                inputIdEspecialidad.value =
                  this.querySelector("input").getAttribute("data-id");
                cargarProveedores(inputIdEspecialidad.value, selectProveedor);
                opcionSeleccionada = true;
                cerrarListaAutocompletadoEspecialidad();
              });
    
              divItems.appendChild(item);
            });
          })
          .catch((error) => console.error("Error en la solicitud Fetch:", error));
      });
    
      inputEspecialidad.addEventListener("blur", function () {
        setTimeout(() => {
          if (!opcionSeleccionada) {
            inputEspecialidad.value = "";
            inputIdEspecialidad.value = "";
            selectProveedor.innerHTML =
              '<option value="">SELECCIONA UN PROVEEDOR</option>';
            selectProveedor.disabled = true; // Deshabilitar el selectProveedor
          }
        }, 200);
      });
    
      function cargarProveedores(idEspecialidad, selectElement) {
        fetch(`/api/llenar_contratistas/?id_especialidad=${idEspecialidad}`)
          .then((response) => {
            if (!response.ok) {
              throw new Error("Network response was not ok");
            }
            return response.json();
          })
          .then((data) => {
            selectElement.innerHTML =
              '<option value="">SELECIONA UN PROVEDOR</option>';
            if (data.length > 0) {
              // Habilitar el selectProveedor solo si hay opciones disponibles
              selectElement.disabled = false;
            } else {
              selectElement.disabled = true; // Asegurarse de que esté deshabilitado si no hay opciones
            }
            data.forEach((proveedor) => {
              var option = document.createElement("option");
              option.value = proveedor.id_proveedor;
              option.textContent = proveedor.razon_social;
              selectElement.appendChild(option);
            });
          })
          .catch((error) => console.error("Error en la solicitud Fetch:", error));
      }
    
      function cerrarListaAutocompletadoEspecialidad() {
        var items = row.querySelectorAll(".autocomplete-items div");
        items.forEach((item) => item.remove());
      }
    
      document.addEventListener("click", function (e) {
        if (!row.contains(e.target)) {
          cerrarListaAutocompletadoEspecialidad();
        }
      });
    }
      
  
      
  }
  
  function configurar_autocompletado_especialida(row,contador) {
    var inputEspecialidad = row.querySelector("#INPUT_ESPECIALIDADES_" + contador);
    var inputIdEspecialidad = row.querySelector("#INPUT_ID_ESPECIALIDADES");
    var selectProveedor = row.querySelector("#INPUT_PROVEEDOR_" + contador);
    var especialidadesDisponibles = [];
    var opcionSeleccionada = false;
  
    // Inicialmente deshabilitar el selectProveedor
    selectProveedor.disabled = true;
  
    inputEspecialidad.addEventListener("input", function () {
      var val = this.value;
      cerrarListaAutocompletadoEspecialidad();
      opcionSeleccionada = false;
  
      if (!val) {
        inputIdEspecialidad.value = "";
        selectProveedor.innerHTML =
          '<option value="">SELECCIONA UN PROVEEDOR</option>';
        selectProveedor.disabled = true; // Deshabilitar el selectProveedor
        return false;
      }
  
  
      fetch(`/api/obtener_especialidades/?query=${encodeURIComponent(val)}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          especialidadesDisponibles = data;
          var divItems = row.querySelector(".autocomplete-items");
          data.forEach((especialidad) => {
            var nombre = especialidad.nombre;
            var id = especialidad.id;
            var regex = new RegExp(`(${val})`, "gi");
            var item = document.createElement("div");
            item.classList.add("list-group-item");
            item.innerHTML = nombre.replace(regex, "<strong>$1</strong>");
            item.innerHTML += `<input type='hidden' value='${nombre}' data-id='${id}'>`;
  
            item.addEventListener("click", function () {
              inputEspecialidad.value = this.querySelector("input").value;
              inputIdEspecialidad.value =
                this.querySelector("input").getAttribute("data-id");
              cargarProveedores(inputIdEspecialidad.value, selectProveedor);
              opcionSeleccionada = true;
              cerrarListaAutocompletadoEspecialidad();
            });
  
            divItems.appendChild(item);
          });
        })
        .catch((error) => console.error("Error en la solicitud Fetch:", error));
    });
  
    inputEspecialidad.addEventListener("blur", function () {
      setTimeout(() => {
        if (!opcionSeleccionada) {
          inputEspecialidad.value = "";
          inputIdEspecialidad.value = "";
          selectProveedor.innerHTML =
            '<option value="">SELECIONA UN PROVEEDOR</option>';
          selectProveedor.disabled = true; // Deshabilitar el selectProveedor
        }
      }, 200);
    });
  
    function cargarProveedores(idEspecialidad, selectElement) {
      fetch(`/api/llenar_contratistas/?id_especialidad=${idEspecialidad}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          selectElement.innerHTML =
            '<option value="">SELECIONA UN PROVEEDOR</option>';
          selectElement.innerHTML += '<option value="0">BAUART</option>';
          if (data.length > 0) {
            // Habilitar el selectProveedor solo si hay opciones disponibles
            selectElement.disabled = false;
          } else {
            selectElement.disabled = true; // Asegurarse de que esté deshabilitado si no hay opciones
          }
          data.forEach((proveedor) => {
            var option = document.createElement("option");
            option.value = proveedor.id_proveedor;
            option.textContent = proveedor.razon_social;
            selectElement.appendChild(option);
          });
        })
        .catch((error) => console.error("Error en la solicitud Fetch:", error));
    }
  
    function cerrarListaAutocompletadoEspecialidad() {
      var items = row.querySelectorAll(".autocomplete-items div");
      items.forEach((item) => item.remove());
    }
  
    document.addEventListener("click", function (e) {
      if (!row.contains(e.target)) {
        cerrarListaAutocompletadoEspecialidad();
      }
    });
  }
  
  function formatearMoneda(valor) {
    // Elimina cualquier carácter no numérico y formatea como número
    valor = parseFloat(valor.replace(/[^0-9.]/g, ""));
    if (isNaN(valor)) {
      valor = 0;
    }
    return valor.toLocaleString("es-MX", { style: "currency", currency: "MXN" });
  }
  
  function formatearMoneda(valor) {
    // Elimina cualquier carácter no numérico y formatea como número
    valor = parseFloat(valor.replace(/[^0-9.-]/g, "")); // Incluye '-' para diferencias negativas
    if (isNaN(valor)) {
      valor = 0;
    }
    return valor.toLocaleString("es-MX", { style: "currency", currency: "MXN" });
  }
  
  /**
   * FUNCION PARA CALCULAR LA DIFERENCIA EN EL SUBPRESUPUESTO
   *
   * @param {Tipo} idDetallePresupuesto  - Id de partida presupuestal
   * @param {Tipo} idSubDetallePresupuesto - Id de partida Subpresupuesto
  */

  function sub_cular_diferecnia(idDetallePresuouesto,idSubDetallePresupuesto) {


    var tabla = document.getElementById(`tablasub_${idDetallePresuouesto}`);
    var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
    var filas = cuerpoTabla.getElementsByTagName("tr");
  
    var totalCliente = 0;
    var totalProveedor = 0;
    var totalDiferencia = 0;
  
    for (var i = 0; i < filas.length; i++) {
      var cellPresupuestoCliente = filas[i].getElementsByTagName("td")[3];
      var cellPresupuestoProveedor = filas[i].getElementsByTagName("td")[4];
      var cellDiferencia = filas[i].getElementsByTagName("td")[5];
  
      if (cellPresupuestoCliente && cellPresupuestoProveedor && cellDiferencia) {
        // Obtener valores de los inputs
        var presupuesto_cliente_input =
          cellPresupuestoCliente.querySelector("input");
        var presupuesto_proveedor_input =
          cellPresupuestoProveedor.querySelector("input");
        var diferencia_input = cellDiferencia.querySelector("input");
  
        var presupuesto_cliente = presupuesto_cliente_input.value || "0";
        var presupuesto_proveedor = presupuesto_proveedor_input.value || "0";
  
        // Convertir los valores a números
        presupuesto_cliente =
          parseFloat(presupuesto_cliente.replace(/[^0-9.-]/g, "")) || 0;
        presupuesto_proveedor =
          parseFloat(presupuesto_proveedor.replace(/[^0-9.-]/g, "")) || 0;
  
        // Calcular la diferencia
        var diferencia = presupuesto_cliente - presupuesto_proveedor;
  
        // Formatear los valores como moneda
        presupuesto_cliente_input.value = formatearMoneda(
          presupuesto_cliente.toString()
        );
        presupuesto_proveedor_input.value = formatearMoneda(
          presupuesto_proveedor.toString()
        );
        diferencia_input.value = formatearMoneda(diferencia.toString());
  
        // Cambiar el color del input si la diferencia es negativa
        if (diferencia < 0) {
          diferencia_input.style.backgroundColor = "red";
          diferencia_input.style.color = "white"; // Cambia el texto a blanco para mayor visibilidad
        } else {
          diferencia_input.style.backgroundColor = ""; // Restaurar color de fondo original
          diferencia_input.style.color = ""; // Restaurar color de texto original
        }
  
        totalCliente += presupuesto_cliente;
        totalProveedor += presupuesto_proveedor;
        totalDiferencia += diferencia;
  
      }
    }
  
  


    inputPresupuestoClienteBauart = document.getElementById(`INPUT_PRESUPUESTO_CLIENTE_BAUART_${idDetallePresuouesto}`)
    inputPresupuestoProveedor = document.getElementById(`INPUT_PRESUPUESTO_CONTRATISTA_${idDetallePresuouesto}`)
    inputDiferencia = document.getElementById(`INPUT_DIFERENCIA_PRESUPUESTOS_${idDetallePresuouesto}`)


    if (totalDiferencia<0){
      inputDiferencia.style.backgroundColor = "red";
      inputDiferencia.style.color = "white";
  
    }
    else{
      inputDiferencia.style.backgroundColor = "";
      inputDiferencia.style.color = "";
    }

    inputPresupuestoClienteBauart.value = formatearMoneda(totalCliente.toString());
    inputPresupuestoProveedor.value = formatearMoneda(totalProveedor.toString());
    inputDiferencia.value = formatearMoneda(totalDiferencia.toString());

    

  
  }
  
  function concular_diferecnia() {
    var tabla = document.getElementById("DETALLE_PRESUPUESTO");
    var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
    var filas = cuerpoTabla.getElementsByTagName("tr");
  
    var totalCliente = 0;
    var totalProveedor = 0;
    var totalDiferencia = 0;
  
    for (var i = 0; i < filas.length; i++) {
      var cellPresupuestoCliente = filas[i].getElementsByTagName("td")[3];
      var cellPresupuestoProveedor = filas[i].getElementsByTagName("td")[4];
      var cellDiferencia = filas[i].getElementsByTagName("td")[5];
  
      if (cellPresupuestoCliente && cellPresupuestoProveedor && cellDiferencia) {
        // Obtener valores de los inputs
        var presupuesto_cliente_input =
          cellPresupuestoCliente.querySelector("input");
        var presupuesto_proveedor_input =
          cellPresupuestoProveedor.querySelector("input");
        var diferencia_input = cellDiferencia.querySelector("input");
  
        var presupuesto_cliente = presupuesto_cliente_input.value || "0";
        var presupuesto_proveedor = presupuesto_proveedor_input.value || "0";
  
        // Convertir los valores a números
        presupuesto_cliente =
          parseFloat(presupuesto_cliente.replace(/[^0-9.-]/g, "")) || 0;
        presupuesto_proveedor =
          parseFloat(presupuesto_proveedor.replace(/[^0-9.-]/g, "")) || 0;
  
        // Calcular la diferencia
        var diferencia = presupuesto_cliente - presupuesto_proveedor;
  
        // Formatear los valores como moneda
        presupuesto_cliente_input.value = formatearMoneda(
          presupuesto_cliente.toString()
        );
        presupuesto_proveedor_input.value = formatearMoneda(
          presupuesto_proveedor.toString()
        );
        diferencia_input.value = formatearMoneda(diferencia.toString());
  
        // Cambiar el color del input si la diferencia es negativa
        if (diferencia < 0) {
          diferencia_input.style.backgroundColor = "red";
          diferencia_input.style.color = "white"; // Cambia el texto a blanco para mayor visibilidad
        } else {
          diferencia_input.style.backgroundColor = ""; // Restaurar color de fondo original
          diferencia_input.style.color = ""; // Restaurar color de texto original
        }
  
        totalCliente += presupuesto_cliente;
        totalProveedor += presupuesto_proveedor;
        totalDiferencia += diferencia;
  
       
      }
    }
  
    // Actualizar los totales en la tabla
    document.getElementById("subtotalCliente").value = formatearMoneda(
      totalCliente.toString()
    );
    document.getElementById("subtotalContratista").value = formatearMoneda(
      totalProveedor.toString()
    );

    document.getElementById("totalContratista").value = formatearMoneda(
      totalProveedor.toString()
    );

    if(totalDiferencia<0){
      document.getElementById("subtotalDiferencia").style.backgroundColor = "red";
      document.getElementById("subtotalDiferencia").style.color = "white"
    }
    else{
      document.getElementById("subtotalDiferencia").style.backgroundColor = "";
      document.getElementById("subtotalDiferencia").style.color = ""
    }
    document.getElementById("subtotalDiferencia").value = formatearMoneda(
      totalDiferencia.toString()
    );
    
    /*
      document.getElementById("PRESUPUESTO_CLIENTE").value = formatearMoneda(
      totalCliente.toString()
      );
    */
    
    document.getElementById("totalContratista").value = formatearMoneda(
      totalProveedor.toString()
    );
  
  
  }
  
  function calcularTotalConIndirecto() {
    // Obtener el subtotal
    var subtotalCliente =
      parseFloat(
        document.getElementById("subtotalCliente").value.replace(/[^0-9.-]/g, "")
      ) || 0;
  
    // Obtener el porcentaje directo ingresado por el usuario
    var porcentajeIndirecto =
      parseFloat(document.getElementById("porcentajeIndirecto").value) || 0;
  
    // Calcular el valor adicional basado en el porcentaje directo
    var valorAdicionalCliente = subtotalCliente * (porcentajeIndirecto / 100);
  
    // Calcular los totales sumando el subtotal y el valor adicional
    var totalCliente = subtotalCliente + valorAdicionalCliente;
  
    // Mostrar los totales en los campos correspondientes
    document.getElementById("totalCliente").value = formatearMoneda(
      totalCliente.toString()
    );

    document.getElementById("PRESUPUESTO_CLIENTE").value = formatearMoneda(
      totalCliente.toString()
    )

    document.getElementById("totalIndirectoCliente").value = formatearMoneda(
      valorAdicionalCliente.toString()
    );


    calcularTotalDiferencia();
  }
  
  function calcularTotalDiferencia() {
    // Obtener Total CLiente
    var totalCliente =
      parseFloat(
        document.getElementById("totalCliente").value.replace(/[^0-9.-]/g, "")
      ) || 0;
  
    // Obtener el totalContratista
    var totalContratista =
      parseFloat(
        document.getElementById("totalContratista").value.replace(/[^0-9.-]/g, "")
      ) || 0;
  
    // Calcular el valor adicional basado en el porcentaje directo
    var valorDiferencia = totalCliente - totalContratista;
    var diferencia_input = document.getElementById("totalDiferencia");
    // Cambiar el color del input si la diferencia es negativa
    if (valorDiferencia < 0) {
      diferencia_input.style.backgroundColor = "red";
      diferencia_input.style.color = "white"; // Cambia el texto a blanco para mayor visibilidad
    } else {
      diferencia_input.style.backgroundColor = ""; // Restaurar color de fondo original
      diferencia_input.style.color = ""; // Restaurar color de texto original
    }
  
    // Mostrar los totales en los campos correspondientes
    document.getElementById("totalDiferencia").value = formatearMoneda(
      valorDiferencia.toString()
    );
  }
  

  
  function cargarProveedores(idEspecialidad, selectElement) {
    fetch(`/api/llenar_contratistas/?id_especialidad=${idEspecialidad}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        selectElement.innerHTML =
          '<option value="">Selecciona un proveedor</option>';
        selectElement.innerHTML += '<option value="0">BAUART</option>';
        if (data.length > 0) {
          // Habilitar el selectProveedor solo si hay opciones disponibles
          selectElement.disabled = false;
        } else {
          selectElement.disabled = true; // Asegurarse de que esté deshabilitado si no hay opciones
        }
        data.forEach((proveedor) => {
          var option = document.createElement("option");
          option.value = proveedor.id_proveedor;
          option.textContent = proveedor.razon_social;
          selectElement.appendChild(option);
        });
      })
      .catch((error) => console.error("Error en la solicitud Fetch:", error));
  }
  
 
  
  function colocarSueldo(select, contador,id) {
    const id_puesto = select.value; // Asegurarse de obtener el valor del select
    const inputPresupuestoCliente = document.getElementById(`SUB_PRESUPUESTO_CLIENTE-${id}-${contador}`);
  
    // Validar que el elemento existe
    if (!inputPresupuestoCliente) {
      console.error("El elemento de input no se encontró.");
      return;
    }
  
    fetch(`/api/obtener_puesto/?id_puesto=${id_puesto}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Error en la solicitud: ${response.status} ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => {
        if (data && data.sueldo_base !== undefined) {
          // Actualizar el valor del input con el sueldo_base
          inputPresupuestoCliente.value = data.sueldo_base;
          sub_cular_diferecnia(`${id}`)
        } else {
          console.error("No se recibió el sueldo_base en la respuesta.");
          inputPresupuestoCliente.value = ""; // Vaciar el input en caso de error
        }
      })
      .catch((error) => {
        console.error("Error en la solicitud Fetch:", error);
      });
  }
  
    // Función que recibirá un argumento
    function autocompleta_concepto_sub_modificar(input,idDetallePresuouesto, contadorConcepto,is_nomina) {
        // Funcion para configurar autocompletado de especialidades

        // OBTENER LOS ARGUMENTOS O VALORES DE LA BUSQUEDA
        const args = input.value
        console.log(args)
        const inputIdEspecialidadSub = document.getElementById(`INPUT_ID_ESPECIALIDADES_SUB_${idDetallePresuouesto}-${contadorConcepto}`)
        console.log(inputIdEspecialidadSub)
        const selectProvedoresSub = document.getElementById(`SELECT_PROVEEDOR_SUB_${idDetallePresuouesto}-${contadorConcepto}`)
        cerrarListaAutocompletadoConceptoSub(idDetallePresuouesto,contadorConcepto);
        opcionSeleccionada = false;

        if (is_nomina){
            //ES UNA PARTIDA DE NOMINA
            if (!args) {
                inputIdEspecialidadSub.value = "";
                selectProvedoresSub.innerHTML =
                '<option value="" style="text-align: center;">SELECIONA UN PUESTO</option>';
                selectProvedoresSub.disabled = true; // Deshabilitar el selectProveedor
              return false;
            }

            fetch(`/api/obtener_categorias/?query=${encodeURIComponent(args)}`)
            .then((response) => {
                if (!response.ok) {
                throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => {
                categoriasDisponibles = data;
                var divItems = document.getElementById(`DIV_LISTA_RESULTADOS_${idDetallePresuouesto}-${contadorConcepto}`)
                data.forEach((especialidad) => {
                var nombre = especialidad.categoria;
                var id = especialidad.id;
                var regex = new RegExp(`(${args})`, "gi");
                var item = document.createElement("div");
                item.classList.add("list-group-item");
                item.innerHTML = nombre.replace(regex, "<strong>$1</strong>");
                item.innerHTML += `<input type='hidden' value='${nombre}' data-id='${id}'>`;

                item.addEventListener("click", function () {
                    input.value = this.querySelector("input").value;
                    inputIdEspecialidadSub.value = 
                        this.querySelector("input").getAttribute("data-id");
                    cargarPuesto(inputIdEspecialidadSub.value, selectProvedoresSub);
                    opcionSeleccionada = true;
                    cerrarListaAutocompletadoConceptoSub(idDetallePresuouesto,contadorConcepto);
                });

                divItems.appendChild(item);
                });

                
            })
            .catch((error) => console.error("Error en la solicitud Fetch:", error));
        }
        else{
            //ES UNA PARTIDA DE MATERIALES
            if (!args) {
                inputIdEspecialidadSub.value = "";
                selectProvedoresSub.innerHTML =
                '<option value="" style="text-align: center;">SIN PROVEEDOR</option>';
                selectProvedoresSub.disabled = true; // Deshabilitar el selectProveedor
              return false;
            }
            fetch(`/api/obtener_especialidades/?query=${encodeURIComponent(args)}`)
            .then((response) => {
                if (!response.ok) {
                throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => {
                especialidadesDisponibles = data;
                console.log(especialidadesDisponibles)
                var divItems = document.getElementById(`DIV_LISTA_RESULTADOS_${idDetallePresuouesto}-${contadorConcepto}`)
                data.forEach((especialidad) => {
                var nombre = especialidad.nombre;
                var id = especialidad.id;
                var regex = new RegExp(`(${args})`, "gi");
                var item = document.createElement("div");
                item.classList.add("list-group-item");
                item.innerHTML = nombre.replace(regex, "<strong>$1</strong>");
                item.innerHTML += `<input type='hidden' value='${nombre}' data-id='${id}'>`;

                item.addEventListener("click", function () {
                    input.value = this.querySelector("input").value;
                    inputIdEspecialidadSub.value = 
                        this.querySelector("input").getAttribute("data-id");
                    opcionSeleccionada = true;
                    cerrarListaAutocompletadoConceptoSub(idDetallePresuouesto,contadorConcepto);
                });

                divItems.appendChild(item);
                });

                
            })
            .catch((error) => console.error("Error en la solicitud Fetch:", error));
        }
    
        
    

        

    }

    function cerrarListaAutocompletadoConceptoSub(idDetallePresuouesto,contadorConcepto) {
        var div = document.getElementById(`DIV_LISTA_RESULTADOS_${idDetallePresuouesto}-${contadorConcepto}`)
        var  items = div.querySelectorAll(".autocomplete-items div");
        items.forEach((item) => item.remove());
      }

      function cargarPuesto(idEspecialidad, selectElement) {
        fetch(`/api/llenar_puestos/?id_categoria=${idEspecialidad}`)
          .then((response) => {
            if (!response.ok) {
              throw new Error("Network response was not ok");
            }
            return response.json();
          })
          .then((data) => {
            selectElement.innerHTML =
              '<option value="" >SELECIONA UN PUESTO</option>';
            if (data.length > 0) {
              // Habilitar el selectProveedor solo si hay opciones disponibles
              selectElement.disabled = false;
            } else {
              selectElement.disabled = true; // Asegurarse de que esté deshabilitado si no hay opciones
            }
            data.forEach((puesto) => {
              var option = document.createElement("option");
              option.value = puesto.id;
              option.textContent = puesto.puesto;
              selectElement.appendChild(option);
            });
          })
          .catch((error) => console.error("Error en la solicitud Fetch:", error));
      }

      document.addEventListener("DOMContentLoaded", function () {
    // Obtener todos los inputs con la clase 'currency-input'
    const currencyInputs = document.querySelectorAll(".currency-input");

    // Recorrer cada input
    currencyInputs.forEach(input => {
        // Obtener el valor del input
        const rawValue = input.value;

        // Eliminar símbolos como '$' y ',' para convertirlo a un número
        const numericValue = parseFloat(rawValue.replace(/[\$,]/g, ''));

        // Verificar si el valor es negativo
        if (!isNaN(numericValue) && numericValue < 0) {
            // Aplicar estilo al input
            input.style.backgroundColor = "red";
            input.style.color = "white";
        }
    });
});



function validarEstatusPresupuesto() {
  // Obtener la tabla
  var table = document.getElementById("DETALLE_PRESUPUESTO");
  if (!table) {
      console.error("No se encontró la tabla con ID DETALLE_PRESUPUESTO.");
      return;
  }

  // Obtener todas las filas del tbody
  let rows = table.getElementsByTagName("tbody")[0].getElementsByTagName("tr");

  // Variable para verificar si todas las partidas están aprobadas
  var estatus_presupuesto = true;

  // Recorrer todas las filas de la tabla
  for (var i = 0; i < rows.length; i++) {
      // Buscar los selects de estatus
      var estatusPartidasDb = rows[i].querySelector('select[name="STATUS_DB[]"]');
      var estatusPartidasNv = rows[i].querySelector('select[name="STATUS_NV[]"]');

      // Verificar si existen los selects y si alguna fila no está aprobada
      if ((estatusPartidasDb && estatusPartidasDb.value !== "1") || 
          (estatusPartidasNv && estatusPartidasNv.value !== "1")) {
          estatus_presupuesto = false;
          break; // Si encontramos una fila no aprobada, salimos del bucle
      }
  }

  // Obtener el campo de status_presupuesto
  let inputstatusPresupuesto = document.getElementById("status_presupuesto");

  if (!inputstatusPresupuesto) {
      console.error("No se encontró el campo con ID status_presupuesto.");
      return;
  }

  // Asignar el valor al input
  inputstatusPresupuesto.value = estatus_presupuesto ? "true" : "false";

  console.log("Estado del presupuesto:", inputstatusPresupuesto.value);
}


function validarContratosPresupuesto(){
   // Obtener la tabla
   var table = document.getElementById("DETALLE_PRESUPUESTO");
   if (!table) {
       console.error("No se encontró la tabla con ID DETALLE_PRESUPUESTO.");
       return;
   }
 
   // Obtener todas las filas del tbody
   let rows = table.getElementsByTagName("tbody")[0].getElementsByTagName("tr");
 
   // Variable para verificar si todas las partidas están aprobadas
   var contratos_firmados = true;
 
   // Recorrer todas las filas de la tabla
  for (var i = 0; i < rows.length; i++) {
      // Buscar los selects de estatus
      var contatroFirmadoDb = rows[i].querySelector('select[name="CONTRATO_FIRMADO_DB[]"]');
      var contatroFirmadoNv = rows[i].querySelector('select[name="CONTRATO_FIRMADO_NV[]"]');
 
      // Verificar si existen los selects y si alguna fila no está aprobada
      if ((contatroFirmadoDb && contatroFirmadoDb.value !== "1") || 
          (contatroFirmadoNv && contatroFirmadoNv.value !== "1")) {
          contratos_firmados = false;
          break; // Si encontramos una fila no aprobada, salimos del bucle
      }
  }

  
  // Obtener el campo de status_presupuesto
  let inputStatusContratos = document.getElementById("status_contratos");

  if (!inputStatusContratos) {
      console.error("No se encontró el campo con ID status_presupuesto.");
      return;
  }

  // Asignar el valor al input
  inputStatusContratos.value = contratos_firmados ? "true" : "false";

  console.log("Estado del presupuesto:", inputstatusPresupuesto.value);

}