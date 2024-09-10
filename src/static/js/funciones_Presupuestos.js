document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM completamente cargado y analizado");
  var inputPROYECTO = document.querySelector("#PROYECTO");
  var inputCLIENTE = document.querySelector("#CLIENTE");
  var inputEMPRESA = document.querySelector("#EMPRESA");
  var inputPROYECTO_ID = document.querySelector("#PROYECTO_ID");
  var inputCLIENTE_ID = document.querySelector("#CLIENTE_ID");
  var inputEMPRESA_ID = document.querySelector("#EMPRESA_ID");
  var inputFECHA_INICIO = document.querySelector("#FECHA_INICIO");
  var inputFECHA_FIN = document.querySelector("#FECHA_FIN");
  var inputDIAS_TOTALES = document.querySelector("#DIAS_TOTALES"); // Nuevo input para mostrar los días totales

  console.log("Input inputPROYECTO:", inputPROYECTO);
  console.log("Input inputCLIENTE:", inputCLIENTE);
  console.log("Input inputEMPRESA:", inputEMPRESA);
  console.log("Input inputPROYECTO_ID:", inputPROYECTO_ID);

  if (inputPROYECTO) {
    configurar_autocompletado(
      inputPROYECTO,
      inputCLIENTE,
      inputEMPRESA,
      inputPROYECTO_ID,
      inputCLIENTE_ID,
      inputEMPRESA_ID,
      inputFECHA_INICIO,
      inputFECHA_FIN,
      inputDIAS_TOTALES
    );
  }
});

function configurar_autocompletado(
  inputPROYECTO,
  inputCLIENTE,
  inputEMPRESA,
  inputPROYECTO_ID,
  inputCLIENTE_ID,
  inputEMPRESA_ID,
  inputFECHA_INICIO,
  inputFECHA_FIN,
  inputDIAS_TOTALES
) {
  var proyectosDisponibles = [];
  var opcionSeleccionada = false;

  inputPROYECTO.addEventListener("input", function () {
    var val = this.value;
    console.log(`Valor del input: ${val}`);

    cerrarListaAutocompletado();
    opcionSeleccionada = false;

    if (!val) {
      inputPROYECTO.value = "";
      inputCLIENTE.value = "";
      inputEMPRESA.value = "";
      inputPROYECTO_ID.value = "";
      inputCLIENTE_ID.value = "";
      inputEMPRESA_ID.value = "";
      inputFECHA_INICIO.value = "";
      inputFECHA_FIN.value = "";
      inputDIAS_TOTALES.value = ""; // Limpiar el campo de días totales también
      console.log("Valor vacío, limpiando inputs");
      return false;
    }

    console.log(`Buscando clientes con el valor: ${val}`);

    fetch(`/api/llenar_proyecto/?query=${val}`)
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
            var clienteRazonSocial = proyectoData.razon_social_cliente;
            var empresaRazonSocial = proyectoData.razon_social_empresa;
            var id = proyectoData.id;
            var idcliente = proyectoData.id_cliente;
            var idempresa = proyectoData.id_empresa;
            var fechainicio = proyectoData.fecha_inicio;
            var fechafin = proyectoData.fecha_fin;
            var regex = new RegExp(`(${val})`, "gi");
            var item = document.createElement("div");
            item.classList.add("list-group-item");

            item.innerHTML = proyecto.replace(regex, "<strong>$1</strong>");
            item.innerHTML += `<input type='hidden' value='${proyecto}' data-id='${id}' data-cliente='${clienteRazonSocial}' data-empresa='${empresaRazonSocial}' data-id-cliente='${idcliente}' data-id-empresa='${idempresa}' data-fecha-inicio='${fechainicio}' data-fecha-fin='${fechafin}'>`;

            item.addEventListener("click", function () {
              console.log(
                "Elemento seleccionado:",
                this.querySelector("input").value
              );
              inputPROYECTO.value = this.querySelector("input").value;
              inputCLIENTE.value =
                this.querySelector("input").getAttribute("data-cliente");
              inputEMPRESA.value =
                this.querySelector("input").getAttribute("data-empresa");
              inputPROYECTO_ID.value =
                this.querySelector("input").getAttribute("data-id");
              inputCLIENTE_ID.value =
                this.querySelector("input").getAttribute("data-id-cliente");
              inputEMPRESA_ID.value =
                this.querySelector("input").getAttribute("data-id-empresa");
              inputFECHA_INICIO.value =
                this.querySelector("input").getAttribute("data-fecha-inicio");
              inputFECHA_FIN.value =
                this.querySelector("input").getAttribute("data-fecha-fin");

              // Calcular los días totales
              var fechaInicio = new Date(inputFECHA_INICIO.value);
              var fechaFin = new Date(inputFECHA_FIN.value);
              var diferenciaTiempo = fechaFin - fechaInicio;
              var diasTotales = Math.ceil(
                diferenciaTiempo / (1000 * 60 * 60 * 24)
              );
              inputDIAS_TOTALES.value = diasTotales; // Asignar la diferencia de días al input correspondiente

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
        inputCLIENTE.value = "";
        inputEMPRESA.value = "";
        inputPROYECTO_ID.value = "";
        inputCLIENTE_ID.value = "";
        inputEMPRESA_ID.value = "";
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

function añadirConcepto() {
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
    <input type="number" class="form-control borderless" id="ID_DETALLE[]" name="ID_DETALLE[]" readonly>
`;

  cell2.innerHTML = `
  <input type="text" class="form-control" style="text-align: left" id="INPUT_ESPECIALIDADES" name="ESPECIALIDADES[]" autocomplete="off" required>
  <input type="text" class="form-control" style="display: none" id="INPUT_ID_ESPECIALIDADES">
  <div class="autocomplete-items"></div>
  <div class="invalid-feedback">
      Selecciona una especialidad
  </div>`;

  cell3.innerHTML = `
    <select class="form-control" id="INPUT_PROVEEDOR" name="PROVEEDOR[]">
        <option value="">Selecciona un proveedor</option>
        
    </select>
    <input type="text" class="form-control" style="display: none" id="INPUT_ID_PROVEEDOR" name="ID_PROVEDOR">
    <div class="invalid-feedback">
        Selecciona un proveedor
    </div>
    `;

  cell4.innerHTML = `
  <input type="text" class="form-control currency-input presupuesto-cliente" name="PRESUPUESTO_CLIENTE[]" placeholder="$0.00" onblur="concular_diferecnia()">
`;

  cell5.innerHTML = `
  <input type="text" class="form-control currency-input presupuesto-proveedor"  name="PRESUPUESTO_PROVEEDOR[]" placeholder="$0.00" onblur="concular_diferecnia()">
`;

  cell6.innerHTML = `
    <input type="text" class="form-control currency-input presupuesto-diferencia" name="DIFERENCIA[]" placeholder="$0.00" readonly>
`;

  cell7.innerHTML = `
<select style="text-align: center;"  id="CONTRATO_FIRMADO" name="CONTRATO_FIRMADO[]" class="form-control">
    <option value="1">No</option>
    <option value="2">Sí</option>
</select>
<div class="invalid-feedback">
    Completa el banco
</div>
`;

  cell8.innerHTML = `
<select id="STATUS" name="STATUS[]" class="form-control">
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
  
  configurar_autocompletado_especialida(newRow);
  actualizarNumeracion();
}

function eliminarFila(button) {
  var row = button.closest("tr");
  row.parentNode.removeChild(row);
  actualizarNumeracion();
  concular_diferecnia()
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
      
      cell.textContent = i+1
    }
  }
}

function configurar_autocompletado_especialida(row) {
    var inputEspecialidad = row.querySelector("#INPUT_ESPECIALIDADES");
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
            inputIdEspecialidad.value = ''; 
            selectProveedor.innerHTML = '<option value="">Selecciona un proveedor</option'; 
            selectProveedor.disabled = true; // Deshabilitar el selectProveedor
            return false;
        }

        console.log(`Buscando especialidades con el valor: ${val}`);

        fetch(`/api/obtener_especialidades/?query=${encodeURIComponent(val)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then(data => {
                console.log("Datos recibidos de la API de especialidades:", data); 
                especialidadesDisponibles = data; 
                var divItems = row.querySelector(".autocomplete-items");
                data.forEach(especialidad => {
                    var nombre = especialidad.nombre;
                    var id = especialidad.id;
                    var regex = new RegExp(`(${val})`, 'gi');
                    var item = document.createElement("div");
                    item.classList.add("list-group-item"); 
                    item.innerHTML = nombre.replace(regex, "<strong>$1</strong>");
                    item.innerHTML += `<input type='hidden' value='${nombre}' data-id='${id}'>`;

                    item.addEventListener("click", function () {
                        inputEspecialidad.value = this.querySelector("input").value;
                        inputIdEspecialidad.value = this.querySelector("input").getAttribute("data-id");
                        cargarProveedores(inputIdEspecialidad.value, selectProveedor);
                        opcionSeleccionada = true;
                        cerrarListaAutocompletadoEspecialidad();
                    });

                    divItems.appendChild(item);
                });
            })
            .catch(error => console.error("Error en la solicitud Fetch:", error));
    });

    inputEspecialidad.addEventListener("blur", function () {
        setTimeout(() => {
            if (!opcionSeleccionada) {
                inputEspecialidad.value = '';
                inputIdEspecialidad.value = '';
                selectProveedor.innerHTML = '<option value="">Seleciona un proveedor</option>'; 
                selectProveedor.disabled = true; // Deshabilitar el selectProveedor
            }
        }, 200);
    });

    function cargarProveedores(idEspecialidad, selectElement) {
        fetch(`/api/llenar_contratistas/?id_especialidad=${idEspecialidad}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then(data => {
                selectElement.innerHTML = '<option value="">Seleciona un proveedor</option>'; 
                selectElement.innerHTML += '<option value="0">BAUART</option>';
                if (data.length > 0) {
                    // Habilitar el selectProveedor solo si hay opciones disponibles
                    selectElement.disabled = false;
                } else {
                    selectElement.disabled = true; // Asegurarse de que esté deshabilitado si no hay opciones
                }
                data.forEach(proveedor => {
                    var option = document.createElement("option");
                    option.value = proveedor.id_proveedor;
                    option.textContent = proveedor.razon_social;
                    selectElement.appendChild(option);
                });
            })
            .catch(error => console.error("Error en la solicitud Fetch:", error));
    }

    function cerrarListaAutocompletadoEspecialidad() {
        var items = row.querySelectorAll(".autocomplete-items div");
        items.forEach(item => item.remove());
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
    valor = parseFloat(valor.replace(/[^0-9.]/g, ''));
    if (isNaN(valor)) {
        valor = 0;
    }
    return valor.toLocaleString('es-MX', { style: 'currency', currency: 'MXN' });
}

function formatearMoneda(valor) {
    // Elimina cualquier carácter no numérico y formatea como número
    valor = parseFloat(valor.replace(/[^0-9.-]/g, '')); // Incluye '-' para diferencias negativas
    if (isNaN(valor)) {
        valor = 0;
    }
    return valor.toLocaleString('es-MX', { style: 'currency', currency: 'MXN' });
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
            var presupuesto_cliente_input = cellPresupuestoCliente.querySelector('input');
            var presupuesto_proveedor_input = cellPresupuestoProveedor.querySelector('input');
            var diferencia_input = cellDiferencia.querySelector('input');

            var presupuesto_cliente = presupuesto_cliente_input.value || '0';
            var presupuesto_proveedor = presupuesto_proveedor_input.value || '0';

            // Convertir los valores a números
            presupuesto_cliente = parseFloat(presupuesto_cliente.replace(/[^0-9.-]/g, '')) || 0;
            presupuesto_proveedor = parseFloat(presupuesto_proveedor.replace(/[^0-9.-]/g, '')) || 0;

            // Calcular la diferencia
            var diferencia = presupuesto_cliente - presupuesto_proveedor;

            // Formatear los valores como moneda
            presupuesto_cliente_input.value = formatearMoneda(presupuesto_cliente.toString());
            presupuesto_proveedor_input.value = formatearMoneda(presupuesto_proveedor.toString());
            diferencia_input.value = formatearMoneda(diferencia.toString());

            // Cambiar el color del input si la diferencia es negativa
            if (diferencia < 0) {
                diferencia_input.style.backgroundColor = 'red';
                diferencia_input.style.color = 'white'; // Cambia el texto a blanco para mayor visibilidad
            } else {
                diferencia_input.style.backgroundColor = ''; // Restaurar color de fondo original
                diferencia_input.style.color = ''; // Restaurar color de texto original
            }

            totalCliente += presupuesto_cliente;
            totalProveedor += presupuesto_proveedor;
            totalDiferencia += diferencia;

            console.log('Cliente:', presupuesto_cliente_input.value);
            console.log('Proveedor:', presupuesto_proveedor_input.value);
            console.log('Diferencia:', diferencia_input.value);
        }
    }

     // Actualizar los totales en la tabla
     document.getElementById('subtotalCliente').value = formatearMoneda(totalCliente.toString());
     document.getElementById('subtotalContratista').value = formatearMoneda(totalProveedor.toString());
     document.getElementById('subtotalDiferencia').value = formatearMoneda(totalDiferencia.toString());
     document.getElementById('PRESUPUESTO_CLIENTE').value = formatearMoneda(totalCliente.toString());
    document.getElementById('totalContratista').value = formatearMoneda(totalProveedor.toString());
 
    console.log('Total Cliente:', totalCliente);
    console.log('Total Proveedor:', totalProveedor);
    console.log('Total Diferencia:', totalDiferencia);
}

function calcularTotalConIndirecto() {
    // Obtener el subtotal
    var subtotalCliente = parseFloat(document.getElementById('subtotalCliente').value.replace(/[^0-9.-]/g, '')) || 0;

     // Obtener el porcentaje directo ingresado por el usuario
     var porcentajeIndirecto = parseFloat(document.getElementById('porcentajeIndirecto').value) || 0;

     // Calcular el valor adicional basado en el porcentaje directo
    var valorAdicionalCliente = subtotalCliente * (porcentajeIndirecto / 100);

    // Calcular los totales sumando el subtotal y el valor adicional
    var totalCliente = subtotalCliente + valorAdicionalCliente;

    // Mostrar los totales en los campos correspondientes
    document.getElementById('totalCliente').value = formatearMoneda(totalCliente.toString());
    document.getElementById('totalIndirectoCliente').value = formatearMoneda(valorAdicionalCliente.toString());
    calcularTotalDiferencia()
}

function calcularTotalDiferencia() {
    // Obtener Total CLiente
    var totalCliente = parseFloat(document.getElementById('totalCliente').value.replace(/[^0-9.-]/g, '')) || 0;

     // Obtener el totalContratista
     var totalContratista = parseFloat(document.getElementById('totalContratista').value.replace(/[^0-9.-]/g, '')) || 0;

     // Calcular el valor adicional basado en el porcentaje directo
    var valorDiferencia = totalCliente - totalContratista 
    var diferencia_input = document.getElementById('totalDiferencia')
    // Cambiar el color del input si la diferencia es negativa
    if (valorDiferencia < 0) {
        diferencia_input.style.backgroundColor = 'red';
        diferencia_input.style.color = 'white'; // Cambia el texto a blanco para mayor visibilidad
    } else {
        diferencia_input.style.backgroundColor = ''; // Restaurar color de fondo original
        diferencia_input.style.color = ''; // Restaurar color de texto original
    }

    // Mostrar los totales en los campos correspondientes
    document.getElementById('totalDiferencia').value = formatearMoneda(valorDiferencia.toString());
}


inputEspecialidad.addEventListener("blur", function () {
    setTimeout(() => {
        if (!opcionSeleccionada) {
            inputEspecialidad.value = '';
            inputIdEspecialidad.value = '';
            selectProveedor.innerHTML = '<option value="">Selecciona un proveedor</option>'; 
            selectProveedor.disabled = true; // Deshabilitar el selectProveedor
        }
    }, 200);
});

function cargarProveedores(idEspecialidad, selectElement) {
    fetch(`/api/llenar_contratistas/?id_especialidad=${idEspecialidad}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            selectElement.innerHTML = '<option value="">Selecciona un proveedor</option>'; 
            if (data.length > 0) {
                // Habilitar el selectProveedor solo si hay opciones disponibles
                selectElement.disabled = false;
            } else {
                selectElement.disabled = true; // Asegurarse de que esté deshabilitado si no hay opciones
            }
            data.forEach(proveedor => {
                var option = document.createElement("option");
                option.value = proveedor.id_proveedor;
                option.textContent = proveedor.razon_social;
                selectElement.appendChild(option);
            });
        })
        .catch(error => console.error("Error en la solicitud Fetch:", error));
}

document.addEventListener('DOMContentLoaded', function() {
  const table = document.querySelector('#DETALLE_PRESUPUESTO');
  const thElements = table.querySelectorAll('th');

  thElements.forEach((th, index) => {
      const resizer = document.createElement('div');
      resizer.classList.add('resizer');

      // Añadir el resizer a la cabecera de la columna
      th.appendChild(resizer);

      let startX, startWidth;

      resizer.addEventListener('mousedown', function(e) {
          startX = e.pageX;
          startWidth = th.offsetWidth;

          document.addEventListener('mousemove', mouseMoveHandler);
          document.addEventListener('mouseup', mouseUpHandler);
      });

      const mouseMoveHandler = function(e) {
          const width = startWidth + (e.pageX - startX);
          th.style.width = `${width}px`;
          const col = table.querySelectorAll('col')[index];
          col.style.width = `${width}px`;
      };

      const mouseUpHandler = function() {
          document.removeEventListener('mousemove', mouseMoveHandler);
          document.removeEventListener('mouseup', mouseUpHandler);
      };
  });
});