document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM completamente cargado y analizado");
  var inputPROYECTO = document.querySelector("#PROYECTO");
  var inputPROYECTO_ID = document.querySelector("#PROYECTO_ID");
  var inputCLIENTE_ID = document.querySelector("#CLIENTE_ID")
  var inputFECHA_INICIO = document.querySelector("#FECHA_INICIO");
  var inputFECHA_FIN = document.querySelector("#FECHA_FIN");
  var inputDIAS_TOTALES = document.querySelector("#DIAS_TOTALES"); // Nuevo input para mostrar los días totales


  if (inputPROYECTO) {
    configurar_autocompletado(
      inputPROYECTO,
      inputPROYECTO_ID,
      inputFECHA_INICIO,
      inputFECHA_FIN,
      inputDIAS_TOTALES,
      inputCLIENTE_ID
    );
  }
});

function configurar_autocompletado(inputPROYECTO,inputPROYECTO_ID, inputFECHA_INICIO,inputFECHA_FIN,inputDIAS_TOTALES,inputCLIENTE_ID) {
  var proyectosDisponibles = [];
  var opcionSeleccionada = false;

  inputPROYECTO.addEventListener("input", function () {
    var val = this.value;
    console.log(`Valor del input: ${val}`);

    cerrarListaAutocompletado();
    opcionSeleccionada = false;

    if (!val) {
      inputCLIENTE_ID.value = "";
      inputPROYECTO.value = "";
      inputPROYECTO_ID.value = "";
      inputFECHA_INICIO.value = "";
      inputFECHA_FIN.value = "";
      inputDIAS_TOTALES.value = ""; // Limpiar el campo de días totales también
      console.log("Valor vacío, limpiando inputs");
      return false;
    }

    console.log(`Buscando clientes con el valor: ${val}`);

    fetch(`/api/buscar_proyecto/?query=${val}`)
      .then((response) => {
        console.log("Respuesta del servidor:", response);
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Datos recibidos de la API:", data);

        proyectosDisponibles = data;
        var divItems = document.querySelector("#suggestions");

        if (divItems) {
          divItems.innerHTML = "";
          data.forEach((proyectoData) => {
            var proyecto = proyectoData.nombre_proyecto;
            var id = proyectoData.id;
            
            var id_cliente = proyectoData.id_cliente;
            console.log(id_cliente)
            var fechainicio = proyectoData.fecha_inicio;
            var fechafin = proyectoData.fecha_fin;
            var totalSemanas = proyectoData.semanas
            var regex = new RegExp(`(${val})`, "gi");
            var item = document.createElement("div");
            item.classList.add("list-group-item");

            item.innerHTML = proyecto.replace(regex, "<strong>$1</strong>");
            item.innerHTML += `<input type='hidden' value='${proyecto}' data-id='${id}' data-id-cliente='${id_cliente}'  data-fecha-inicio='${fechainicio}' data-fecha-fin='${fechafin}'>`;

            item.addEventListener("click", function () {
              console.log(
                "Elemento seleccionado:",
                this.querySelector("input").value
              );

              

              inputPROYECTO.value = this.querySelector("input").value;
              console.log(inputPROYECTO_ID)
              inputPROYECTO_ID.value = this.querySelector("input").getAttribute("data-id");

              
                
              inputCLIENTE_ID.value = this.querySelector("input").getAttribute("data-id-cliente");
              
              inputFECHA_INICIO.value = this.querySelector("input").getAttribute("data-fecha-inicio");
              
              inputFECHA_FIN.value = this.querySelector("input").getAttribute("data-fecha-fin");

              
              inputDIAS_TOTALES.value = totalSemanas; // Asignar la diferencia de días al input correspondiente

              opcionSeleccionada = true;
              cerrarListaAutocompletado();
            });

            divItems.appendChild(item);
          });
        } else {
          console.log("No se encontró el contenedor de sugerencias.");
        }
      })
      .catch((error) => console.error("Error en la solicitud Fetch:", error));
  });

  inputPROYECTO.addEventListener("blur", function () {
    setTimeout(() => {
      if (!opcionSeleccionada) {
        inputPROYECTO.value = "";
        inputCLIENTE_ID.value = ""
        inputFECHA_INICIO.value = "";
        inputFECHA_FIN.value = "";
        inputDIAS_TOTALES.value = ""; // Limpiar el campo de días totales también
      }
    }, 200);
  });

  function cerrarListaAutocompletado() {
    var items = document.querySelectorAll("#suggestions .list-group-item");
    items.forEach((item) => item.remove());
    console.log("Lista de autocompletado cerrada.");
  }

  document.addEventListener("click", function (e) {
    if (
      !e.target.matches("#PROYECTO") &&
      !e.target.matches("#suggestions") &&
      !e.target.closest("#suggestions")
    ) {
      cerrarListaAutocompletado();
      console.log("Hizo clic fuera del campo de entrada y sugerencias.");
    }
  });
}
contador = 0;
function añadirConcepto() {
  contador++;
  var tabla = document.getElementById("DETALLE_PRESUPUESTO");
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
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
    <input type="number" class="form-control borderless" id="ID_DETALLE_${contador}" name="ID_DETALLE[]" readonly>
`;

  cell2.innerHTML = `
  <input type="text" class="form-control" id="INPUT_ESPECIALIDADES_${contador}" name="ESPECIALIDADES[]" autocomplete="off" required>
  <input type="text" class="form-control" style="display: none" id="INPUT_ID_ESPECIALIDADES">
  <div class="autocomplete-items"></div>
  <div class="invalid-feedback">
      Selecciona una especialidad
  </div>`;

  cell3.innerHTML = `
    <div class="oculto" id="contenedor_boton_subpresupuesto_${contador}">
        <button type="button" class="btn botones" id="boto_modal_subpresupuesto${contador}" data-bs-toggle="modal" data-bs-target="#modalPresupuesto_${contador}">
          VER PRESUPUESTO BAUART
      </button>
    </div>
    <select class="form-control" id="INPUT_PROVEEDOR" name="PROVEEDOR[]" onchange="sub_presupuesto(this,${contador})">
        <option value="">Selecciona un proveedor</option>
        
    </select>
    <input type="text" class="form-control" style="display: none" id="INPUT_ID_PROVEEDOR" name="ID_PROVEDOR">
    <div class="invalid-feedback">
        Selecciona un proveedor
    </div>
    `;

  cell4.innerHTML = `
  <input type="text" class="form-control currency-input presupuesto-cliente" id="PRESUPUESTO_CLIENTE_${contador}" name="PRESUPUESTO_CLIENTE[]" placeholder="$0.00" onchange="concular_diferecnia()">
`;

  cell5.innerHTML = `
  <input type="text" class="form-control currency-input presupuesto-proveedor" id="PRESUPUESTO_PROVEEDOR_${contador}" name="PRESUPUESTO_PROVEEDOR[]" placeholder="$0.00" onchange="concular_diferecnia()">
`;

  cell6.innerHTML = `
    <input type="text" class="form-control currency-input presupuesto-diferencia" id="DIFERENCIA_${contador}" name="DIFERENCIA[]" onchange="concular_diferencia()" placeholder="$0.00" readonly>
`;

  cell7.innerHTML = `
<select style="text-align: center;"  id="CONTRATO_FIRMADO" name="CONTRATO_FIRMADO[]" class="form-control" >
    <option value="1">No</option>
    <option value="2">Sí</option>
</select>
<div class="invalid-feedback">
    Completa el banco
</div>
`;

  cell8.innerHTML = `
<select id="STATUS" name="STATUS[]" class="form-control" style="text-align: center;">
    <option value="1">Carga presupuesto</option>
    <option value="2">Aprobación director</option>
    <option value="3">Primera modificación de presupuesto</option> 
</select>
`;

  cell9.innerHTML = `
<div class="d-flex align-items-center justify-content-center">
  <button onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i></button>
</div>
`;



  configurar_autocompletado_especialida(newRow,contador);
  actualizarNumeracion();
}



function añadir_concepto_sub(id) {

  var tabla = document.getElementById(`tablasub_${id}`);
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
  var newRow = cuerpoTabla.insertRow(); // Inserta la nueva fila al final

  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2);
  var cell4 = newRow.insertCell(3);
  var cell5 = newRow.insertCell(4);
  var cell6 = newRow.insertCell(5);
  var cell7 = newRow.insertCell(6);


  cell1.innerHTML = `
    <input type="number" class="form-control borderless" id="ID_DETALLE_SUB${contador}" name="ID_DETALLE[]" readonly>
`;

  cell2.innerHTML = `
  <input type="text" class="form-control" id="INPUT_ESPECIALIDADES_SUB_${contador}" name="ESPECIALIDADES[]" autocomplete="off" required>
  <input type="text" class="form-control" style="display: none" id="INPUT_ID_ESPECIALIDADES_SUB_${contador}">
  <div class="autocomplete-items"></div>
  <div class="invalid-feedback">
      Selecciona una especialidad
  </div>`;

  cell3.innerHTML = `
    
    <select class="form-control" id="SELECT_PROVEEDOR_SUB_${contador}" name="PROVEEDOR[]" onchange="sub_presupuesto(this,${contador})">
        <option value="">Selecciona un proveedor</option>
        
    </select>
    <input type="text" class="form-control" style="display: none" id="INPUT_ID_PROVEEDOR_SUB${contador}" name="ID_PROVEDOR">
    <div class="invalid-feedback">
        Selecciona un proveedor
    </div>
    `;

  cell4.innerHTML = `
  <input type="text" class="form-control currency-input presupuesto-cliente"  name="PRESUPUESTO_CLIENTE[]" placeholder="$0.00" onchange="sub_cular_diferecnia(${contador})">
`;

  cell5.innerHTML = `
  <input type="text" class="form-control currency-input presupuesto-proveedor"  name="PRESUPUESTO_PROVEEDOR[]" placeholder="$0.00" onchange="sub_cular_diferecnia(${contador})">
`;

  cell6.innerHTML = `
    <input type="text" class="form-control currency-input presupuesto-diferencia" name="DIFERENCIA[]" placeholder="$0.00" readonly>
`;


  cell7.innerHTML = `
<div class="d-flex align-items-center justify-content-center">
  <button onclick="sub_eliminarFila(this,${contador})" class="btn"><i class="bi bi-trash"></i></button>
</div>
`;

  configurar_autocompletado_especialida_sub(newRow,contador);
  actualizarNumeracionsub(contador);
}


function sub_presupuesto(select, id) {
 
  proveedorSeleccionado = select.value;

  // SI SE SELECIONA BAUART
  if (proveedorSeleccionado == 0) {
    const modalContainer = document.getElementById("subpresupuestos");
    const modalHTML = `
    <!-- Modal -->
    <div class="modal fade modal-xl" id="modalPresupuesto_${id}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title" id="exampleModalLabel">PRESUPUESTO BAUART</h4>
            <button type="button" style="background-color: white;" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="form-group row">
                <!-- PROYECTO -->
                <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
                    <strong><span id="PROYECTO_SUBPRESUPUESTO"> </span></strong> 
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
                    <input type="text"  class="form-control oculto" id="INPUT_NOMBRE_PREPUSPUESTO_${id}" name="PREPUSPUESTO_[]" readonly>
                </div>
            </div>
            <div class="container-fluid">
                <br>
                <div class="form-group row">
                    <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
                        <button class="btn botones add-row-btn" onclick="añadir_concepto_sub(${id})">AGREGAR PARTIDA</button>
                    </div>
                </div>
                <br>
                <div class="table-presupuesto_sub">
                    <table id="tablasub_${id}" class="table tabla-subpresupuesto table-hover table-borderless">
                        <colgroup>
                            <!-- Agrega más columnas según sea necesario -->
                            <col style="width: 40px;"> <!-- Primera columna -->
                            <col style="width: 500px;"> <!-- Segunda columna -->
                            <col style="width: 500px;"> <!-- Tercera columna -->
                            <col style="width: 130px;"> <!-- Cuarta columna -->
                            <col style="width: 130px;"> <!-- Quinta columna -->
                            <col style="width: 130px;"> <!-- Sexta columna -->
                            <col style="width: 50px;"> <!-- Novena columna -->
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
                                <td><input type="text" id="INPUT_PRESUPUESTO_CLIENTE_BAUART_${id}"  name="INPUT_PRESUPUESTO_CLIENTE_BAUART_[]" class="form-control  currency-input" readonly></td>
                                <td><input type="text" id="INPUT_PRESUPUESTO_CONTRATISTA_${id}"  name="INPUT_PRESUPUESTO_CONTRATISTA_BAUART_[]" class="form-control  currency-input" readonly></td>
                                <td><input type="text" id="INPUT_DIFERENCIA_PRESUPUESTOS_${id}" name="INPUT_DIFERENCIA_PRESUPUESTOS[]" class="form-control  currency-input" readonly></td>
                                <td colspan="1"></td>
                            </tr>
            
                    </table>
                </div>
            </div>
          </div>
         <div class="modal-footer">
            <div class="d-grid gap-2 d-md-flex justify-content-start">
              <button type="button" class="btn botones" data-bs-dismiss="modal"><i class="bi bi-x-lg"></i> CERRAR</button>
              <button type="submit" class="btn botones"  data-bs-dismiss="modal" onclick="guardar_presuouesto(${id})" ><i class="bi bi-floppy"></i> CONFIRMAR</button
            </div>
          </div>
        </div>
      </div>
    </div>
    
    `;

     // Insertar el nuevo modal dinámicamente
     modalContainer.insertAdjacentHTML("beforeend", modalHTML);
    
    const contenedorBotones = document.getElementById(`contenedor_boton_subpresupuesto_${id}`)
    const inputPresupuestoCliente = document.getElementById(`PRESUPUESTO_CLIENTE_${contador}`)
    const inputPresupuestoProveedor = document.getElementById(`PRESUPUESTO_PROVEEDOR_${contador}`)
    const inputEspecialidad = document.getElementById(`INPUT_ESPECIALIDADES_${contador}`)
    const tituloPresupuesto =  document.getElementById(`NOMBRE_PRESUPUESTO_${id}`) 
    const directorPrepupuesto = document.getElementById(`NOMBRE_DIRECTOR_${id}`)
    const direccionPrepupuesto = document.getElementById(`DIRECCION_${id}`)

    //console.log("HOLAS SOY LA DIRECION" + DI)
    tituloPresupuesto.textContent  = "BAUART - " +inputEspecialidad.value 
    directorPrepupuesto.textContent = document.getElementById(`DIRECTOR`).value
    direccionPrepupuesto.textContent = document.getElementById(`DIRECCION`).value

    console.log("ESTA ES LA EQUETA"+ tituloPresupuesto)
    inputEspecialidad.setAttribute("readonly", true);
    inputPresupuestoCliente.setAttribute("readonly", true);
    inputPresupuestoProveedor.setAttribute("readonly", true)
    contenedorBotones.classList.remove("oculto");
    select.classList.add("oculto")


   
    
    
    document.getElementById('PROYECTO_SUBPRESUPUESTO').value = document.getElementById('PROYECTO').value
    // Concatenamos correctamente el string del ID del modal
    const modalId = `modalPresupuesto_${id}`;
      
    $(`#${modalId}`).modal("show"); // Mostramos el modal correspondiente
  }
}

function guardar_presuouesto(id){
  // OBTENER SUBTOTALES DE PRESUPUESTO
  const inputSubpresupuestoCliente = document.getElementById(`INPUT_PRESUPUESTO_CLIENTE_BAUART_${id}`)
  const inputSubpresuouestoContratista = document.getElementById(`INPUT_PRESUPUESTO_CONTRATISTA_${id}`)
  const inputSubpresupuestoDiferencia = document.getElementById(`INPUT_DIFERENCIA_PRESUPUESTOS_${id}`)


  document.getElementById(`PRESUPUESTO_CLIENTE_${id}`).value = inputSubpresupuestoCliente.value
  document.getElementById(`PRESUPUESTO_PROVEEDOR_${id}`).value  = inputSubpresuouestoContratista.value
  concular_diferecnia()
  //document.getElementById(`DIFERENCIA_${id}`).value = inputSubpresupuestoDiferencia.value

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
      var input = cell.querySelector("input");
      if (input) {
        input.value = i; // Asigna el número de fila (empezando en 1)
      }

      cell.textContent = i + 1;
    }
  }
}

function actualizarNumeracionsub(id) {
  var tabla = document.getElementById(`tablasub_${id}`);
  console.log(tabla)
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

function configurar_autocompletado_especialida_sub(row,contador) {
  var inputEspecialidad = row.querySelector(`#INPUT_ESPECIALIDADES_SUB_${contador}`);
  console.log(inputEspecialidad)
  var inputIdEspecialidad = row.querySelector(`#INPUT_ID_ESPECIALIDADES_SUB_${contador}`);
  var selectProveedor = row.querySelector(`#SELECT_PROVEEDOR_SUB_${contador}`);
  var especialidadesDisponibles = [];
  var opcionSeleccionada = false;

  // Inicialmente deshabilitar el selectProveedor
  selectProveedor.disabled = true;

  inputEspecialidad.addEventListener("input", function () {
    var val = this.value;
    console.log(`Valor del input de especialidad: ${val}`);
    cerrarListaAutocompletadoEspecialidad();
    opcionSeleccionada = false;

    if (!val) {
      inputIdEspecialidad.value = "";
      selectProveedor.innerHTML =
        '<option value="">Selecciona un proveedor</option';
      selectProveedor.disabled = true; // Deshabilitar el selectProveedor
      return false;
    }

    console.log(`Buscando especialidades con el valor: ${val}`);

    fetch(`/api/obtener_materiales/?query=${encodeURIComponent(val)}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Datos recibidos de la API de especialidades:", data);
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
          '<option value="">Seleciona un proveedor</option>';
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
          '<option value="">Seleciona un proveedor</option>';
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
    console.log("Lista de autocompletado de especialidades cerrada.");
  }

  document.addEventListener("click", function (e) {
    if (!row.contains(e.target)) {
      cerrarListaAutocompletadoEspecialidad();
    }
  });
}

function configurar_autocompletado_especialida(row,contador) {
  var inputEspecialidad = row.querySelector("#INPUT_ESPECIALIDADES_" + contador);
  var inputIdEspecialidad = row.querySelector("#INPUT_ID_ESPECIALIDADES");
  var selectProveedor = row.querySelector("#INPUT_PROVEEDOR");
  var especialidadesDisponibles = [];
  var opcionSeleccionada = false;

  // Inicialmente deshabilitar el selectProveedor
  selectProveedor.disabled = true;

  inputEspecialidad.addEventListener("input", function () {
    var val = this.value;
    console.log(`Valor del input de especialidad: ${val}`);
    cerrarListaAutocompletadoEspecialidad();
    opcionSeleccionada = false;

    if (!val) {
      inputIdEspecialidad.value = "";
      selectProveedor.innerHTML =
        '<option value="">Selecciona un proveedor</option';
      selectProveedor.disabled = true; // Deshabilitar el selectProveedor
      return false;
    }

    console.log(`Buscando especialidades con el valor: ${val}`);

    fetch(`/api/obtener_especialidades/?query=${encodeURIComponent(val)}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Datos recibidos de la API de especialidades:", data);
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
          '<option value="">Seleciona un proveedor</option>';
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
          '<option value="">Seleciona un proveedor</option>';
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
    console.log("Lista de autocompletado de especialidades cerrada.");
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

function sub_cular_diferecnia(id) {
  var tabla = document.getElementById(`tablasub_${id}`);
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

      console.log("Cliente:", presupuesto_cliente_input.value);
      console.log("Proveedor:", presupuesto_proveedor_input.value);
      console.log("Diferencia:", diferencia_input.value);
    }
  }

  // Actualizar los totales en la tabla
  document.getElementById(`INPUT_PRESUPUESTO_CLIENTE_BAUART_${id}`).value = formatearMoneda(
    totalCliente.toString()
  );
  document.getElementById(`INPUT_PRESUPUESTO_CONTRATISTA_${id}`).value = formatearMoneda(
    totalProveedor.toString()
  );
  document.getElementById(`INPUT_DIFERENCIA_PRESUPUESTOS_${id}`).value = formatearMoneda(
    totalDiferencia.toString()
  );
  

  console.log("PRESUPUESTO BAUART Total Cliente:", totalCliente);
  console.log("PRESUPUESTO BAUART Total Proveedor:", totalProveedor);
  console.log("PRESUPUESTO BAUART Total Diferencia:", totalDiferencia);
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

      console.log("Cliente:", presupuesto_cliente_input.value);
      console.log("Proveedor:", presupuesto_proveedor_input.value);
      console.log("Diferencia:", diferencia_input.value);
    }
  }

  // Actualizar los totales en la tabla
  document.getElementById("subtotalCliente").value = formatearMoneda(
    totalCliente.toString()
  );
  document.getElementById("subtotalContratista").value = formatearMoneda(
    totalProveedor.toString()
  );
  document.getElementById("subtotalDiferencia").value = formatearMoneda(
    totalDiferencia.toString()
  );
  
  document.getElementById("PRESUPUESTO_CLIENTE").value = formatearMoneda(
    totalCliente.toString()
  );
  document.getElementById("totalContratista").value = formatearMoneda(
    totalProveedor.toString()
  );

  console.log("Total Cliente:", totalCliente);
  console.log("Total Proveedor:", totalProveedor);
  console.log("Total Diferencia:", totalDiferencia);
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

  console.log("hola" + valorDiferencia)
  // Mostrar los totales en los campos correspondientes
  document.getElementById("totalDiferencia").value = formatearMoneda(
    valorDiferencia.toString()
  );
}

inputEspecialidad.addEventListener("blur", function () {
  setTimeout(() => {
    if (!opcionSeleccionada) {
      inputEspecialidad.value = "";
      inputIdEspecialidad.value = "";
      selectProveedor.innerHTML =
        '<option value="">Selecciona un proveedor</option>';
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

document.addEventListener("DOMContentLoaded", function () {
  const table = document.querySelector("#DETALLE_PRESUPUESTO");
  const thElements = table.querySelectorAll("th");

  thElements.forEach((th, index) => {
    const resizer = document.createElement("div");
    resizer.classList.add("resizer");

    // Añadir el resizer a la cabecera de la columna
    th.appendChild(resizer);

    let startX, startWidth;

    resizer.addEventListener("mousedown", function (e) {
      startX = e.pageX;
      startWidth = th.offsetWidth;

      document.addEventListener("mousemove", mouseMoveHandler);
      document.addEventListener("mouseup", mouseUpHandler);
    });

    const mouseMoveHandler = function (e) {
      const width = startWidth + (e.pageX - startX);
      th.style.width = `${width}px`;
      const col = table.querySelectorAll("col")[index];
      col.style.width = `${width}px`;
    };

    const mouseUpHandler = function () {
      document.removeEventListener("mousemove", mouseMoveHandler);
      document.removeEventListener("mouseup", mouseUpHandler);
    };
  });
});
