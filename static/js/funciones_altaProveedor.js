   // Example starter JavaScript for disabling form submissions if there are invalid fields
   (() => {
    "use strict";
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll(".needs-validation");
  
    // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        let isFormValid = true; // Variable para determinar si el formulario es válido

        // Verificar si el formulario es válido utilizando la validación de Bootstrap
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
          isFormValid = false; // El formulario no es válido
          
          Swal.fire({
            title: "Faltan campos",
            text: "Por favor, complete todos los campos requeridos.",
            icon: "warning", 
            customClass: {
              confirmButton: "custom-button",
            },
          });
        }

        // Comprobación del número de filas en la tabla de Especialidades
        const tablaEspecialidades = document.getElementById("Especialidades");
        const cuerpoTablaEspecialidades = tablaEspecialidades.getElementsByTagName("tbody")[0];
        const numFilasEspecialidades = cuerpoTablaEspecialidades.rows.length;

        if (numFilasEspecialidades === 0) {
          event.preventDefault(); // Evitar el envío del formulario
          event.stopPropagation();
          isFormValid = false; // El formulario no es válido
          
          Swal.fire({
            title: "FALTA ESPECIALIDAD",
            text: "Por favor, agrega al menos una ESPECIALIDAD antes de continuar.",
            icon: "warning",
            customClass: {
              confirmButton: "btn btn-warning",
            },
          });
        }

        // Comprobación del número de filas en la tabla de Contactos
        const tablaContactos = document.getElementById("Contactos");
        const cuerpoTablaContactos = tablaContactos.getElementsByTagName("tbody")[0];
        const numFilasContactos = cuerpoTablaContactos.rows.length;

        if (numFilasContactos === 0) {
          event.preventDefault(); // Evitar el envío del formulario
          event.stopPropagation();
          isFormValid = false; // El formulario no es válido
          
          Swal.fire({
            title: "FALTA CONTACTO",
            text: "Por favor, agrega al menos un CONTACTO antes de continuar.",
            icon: "warning",
            customClass: {
              confirmButton: "btn btn-warning",
            },
          });
        }

        // Comprobación del número de filas en la tabla de Contactos
        const tablaCuentasBancarias = document.getElementById("Cuentas_Bancarias");
        const cuerpoTablaCuentasBancarias = tablaCuentasBancarias.getElementsByTagName("tbody")[0];
        const numFilasCunetas = cuerpoTablaCuentasBancarias.rows.length;

        if (numFilasCunetas === 0) {
          event.preventDefault(); // Evitar el envío del formulario
          event.stopPropagation();
          isFormValid = false; // El formulario no es válido
          
          Swal.fire({
            title: "FALTA CUENTA BANCARIA",
            text: "Por favor, agrega al menos una CUENTA antes de continuar.",
            icon: "warning",
            customClass: {
              confirmButton: "btn btn-warning",
            },
          });
        }

  
          form.classList.add("was-validated");
        },
        false
      );
    });
  })();


function añadirContacto() {
  var tabla = document.getElementById("Contactos");
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
  var newRow = cuerpoTabla.insertRow(0);

  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2);
  var cell4 = newRow.insertCell(3);
  var cell5 = newRow.insertCell(4);
  var cell6 = newRow.insertCell(5); // Celda para el botón de eliminar

  cell1.innerHTML = `
        <input type="text"  class="form-control" name="NOMBRE_CONTACTO[]" required>
        <div class="invalid-feedback">
          COMPLETA NOMBRE
        </div>
      `;

  cell2.innerHTML = `
      <input type="text" class="form-control" name="APELLIDO_CONTACTO[]" required>
      <div class="invalid-feedback">
        COMPLETA APELLIDO
      </div>
    `;

  cell3.innerHTML = `
    <input type="tel" class="form-control" name="TELEFONO_CONTACTO[]" required>
    <div class="invalid-feedback">
      COMPLETA TELEFONO DE CONTACTO
    </div>
  `;

  cell4.innerHTML = `
    <input type="email" class="form-control" name="CORREO_CONTACTO[]" required>
    <div class="invalid-feedback">
      COMPLETA CORRECO
    </div>
  `;

  cell5.innerHTML = `
    <input type="text" class="form-control" name="PUESTO_CONTACTO[]" required>
    <div class="invalid-feedback">
      COMPLETA PUESTO 
    </div>
  `;

  cell6.innerHTML = `
    <div class="d-flex align-items-center justify-content-center" style="height: 100%;">
    <button onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i> </button>
    </div>
  `;

}

function eliminarFila(btn) {
  var row = btn.parentNode.parentNode.parentNode; // Navegar del botón a la celda, de la celda a la fila
  row.parentNode.removeChild(row); // Eliminar la fila del DOM
}

function añadirCuentasBancarias() {
  var tabla = document.getElementById("Cuentas_Bancarias");
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
  var newRow = cuerpoTabla.insertRow(0);

  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2); // Celda para el botón de eliminar
  var cell4 = newRow.insertCell(3);

  cell1.innerHTML = `
        <select id="SELECT_BANCO" name="BANCO[]" style="text-align: center" class="form-control" required >
          <option value="" style="text-align: center;">SELECIONA UN BANCO</option>
        </select>
        <div class="invalid-feedback">
          SELECIONA UN BANCO
        </div>
      `;

  cell2.innerHTML = `
        <input type="text" class="form-control" name="NO_CUENTA[]" maxlength="19" oninput="formatearCLABE(this)" required>
        <div class="invalid-feedback">
          COMPLETA NUMERO DE CUENTA
        </div>
      `;

  cell3.innerHTML = `
        <input type="text" class="form-control" name="CLABE[]" maxlength="23" oninput="formatearCLABE(this)" required>
        <div class="invalid-feedback">
          COMPLETA CLABE
        </div>
      `;
  cell4.innerHTML = `
      <div class="d-flex align-items-center justify-content-center" style="height: 100%;">
        <button onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i></button>
      </div>
      `;

  cargaBancos(newRow);
}

function formatearCuenta(input) {
  // Remover todos los caracteres que no sean dígitos
  let value = input.value.replace(/\D/g, "");

  // Limitar a 16 dígitos
  value = value.substring(0, 16);

  // Añadir guion cada 4 dígitos
  input.value = value.replace(/(\d{4})(?=\d)/g, "$1-");
}

function formatearCLABE(input) {
  // Remover todos los caracteres que no sean dígitos
  let value = input.value.replace(/\D/g, "");

  // Limitar a 18 dígitos
  value = value.substring(0, 18);

  // Añadir guion cada 3 dígitos
  input.value = value.replace(/(\d{3})(?=\d)/g, "$1-");
}

function cargaBancos(row) {
  fetch("/api/obtener_bancos/")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      const select = row.querySelector("#SELECT_BANCO");
      data.forEach((banco) => {
        const option = document.createElement("option");
        option.value = banco.id;
        option.textContent = banco.nombre;
        select.appendChild(option);
      });
    })
    .catch((error) => console.error("Error:", error));
}

function añadirEspecialidad() {
  var tabla = document.getElementById("Especialidades");
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
  var newRow = cuerpoTabla.insertRow(0);

  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1); // Celda para el botón de eliminar

  cell1.innerHTML = `
      <input type="text" placeholder="BUSCAR" class="form-control" style="text-align: center" id="INPUT_ESPECIALIDADES" name="ESPECIALIDADES[]" autocomplete="off" required>
      <input type="hidden" class="form-control" id="INPUT_ID_ESPECIALIDADES" name="ID_ESPECIALIDADES[]">
      <div class="autocomplete-items" ></div>
      <div class="invalid-feedback">
          Selecciona una especialidad
      </div>`;

  cell2.innerHTML =
      '<div class="d-flex align-items-center justify-content-center" style="height: 100%;">' +
      '<button onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i></button>' +
      "</div>";

  configurar_autocompletado(newRow);
}


function configurar_autocompletado(row) {
  var inputEspecialidad = row.querySelector("#INPUT_ESPECIALIDADES");
  var inputIdEspecialidad = row.querySelector("#INPUT_ID_ESPECIALIDADES");
  var especialidadesDisponibles = [];
  var opcionSeleccionada = false; // Variable para verificar si se seleccionó una opción

  inputEspecialidad.addEventListener("input", function () {
      var val = this.value;
      cerrarListaAutocompletado();
      opcionSeleccionada = false; // Resetear la selección en cada input

      if (!val) {
          inputIdEspecialidad.value = ''; // Limpiar ID si se borra el texto
          return false;
      }

      fetch(`/api/obtener_especialidades/?query=${encodeURIComponent(val)}`)
          .then(response => {
              if (!response.ok) {
                  throw new Error("Network response was not ok");
              }
              return response.json();
          })
          .then(data => {
              especialidadesDisponibles = data; // Guardar especialidades disponibles
              var divItems = row.querySelector(".autocomplete-items");
              data.forEach(especialidad => {
                  var nombre = especialidad.nombre;
                  var id = especialidad.id;
                  var regex = new RegExp(`(${val})`, 'gi');
                  var item = document.createElement("div");

                  // Resaltar coincidencias en el nombre
                  item.innerHTML = nombre.replace(regex, "<strong>$1</strong>");
                  item.innerHTML += `<input type='hidden' value='${nombre}' data-id='${id}'>`;

                  item.addEventListener("click", function () {
                      // Asignar el nombre seleccionado al input de especialidad
                      inputEspecialidad.value = this.querySelector("input").value;

                      // Asignar el ID correspondiente al input de ID
                      inputIdEspecialidad.value = this.querySelector("input").getAttribute("data-id");

                      opcionSeleccionada = true; // Marcar como seleccionada una opción
                      cerrarListaAutocompletado();
                  });

                  divItems.appendChild(item);
              });
          })
          .catch(error => console.error("Error:", error));
  });

  inputEspecialidad.addEventListener("blur", function () {
      setTimeout(() => {
          if (!opcionSeleccionada) {
              // Si no se seleccionó una opción, limpiar ambos inputs
              inputEspecialidad.value = '';
              inputIdEspecialidad.value = '';
          }
      }, 200); // Un pequeño retraso para manejar la selección correcta
  });

  function cerrarListaAutocompletado() {
      var items = row.querySelectorAll(".autocomplete-items div");
      items.forEach(item => item.remove());
  }

  document.addEventListener("click", function (e) {
      if (!row.contains(e.target)) {
          cerrarListaAutocompletado();
      }
  });
}

function configurar_autocompletado_especialidad() { 
  var tabla  = document.querySelector("#Especialidades");
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];

  for (let i = 0, row; row = cuerpoTabla.rows[i]; i++) {
    var inputEspecialidad = document.getElementById('INPUT_ESPECIALIDADES_' + (i + 1));
    console.log("ESTE ES EL INPUT DE ESPECIALIDAD: " + inputEspecialidad.value);

    
    var inputIdEspecialidad = document.getElementById('INPUT_ID_ESPECIALIDADES_' + (i + 1));
    console.log("ESTE ES EL INPUT DEL ID DE LA ESPECIALIDAD: " + inputIdEspecialidad.value);
    
    var especialidadesDisponibles = [];
    var opcionSeleccionada = false; // Variable para verificar si se seleccionó una opción

    inputEspecialidad.addEventListener("input", function () {
      var val = this.value;
      cerrarListaAutocompletado();
      opcionSeleccionada = false; // Resetear la selección en cada input

      if (!val) {
          inputIdEspecialidad.value = ''; // Limpiar ID si se borra el texto
          return false;
      }

      fetch(`/api/obtener_especialidades/?query=${encodeURIComponent(val)}`)
        .then(response => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then(data => {
          especialidadesDisponibles = data; // Guardar especialidades disponibles
          var divItems = row.querySelector(".autocomplete-items");

          data.forEach(especialidad => {
            var nombre = especialidad.nombre;
            var id = especialidad.id;
            var regex = new RegExp(`(${val})`, 'gi');
            var item = document.createElement("div");

            // Resaltar coincidencias en el nombre
            item.innerHTML = nombre.replace(regex, "<strong>$1</strong>");
            item.innerHTML += `<input type='hidden' value='${nombre}' data-id='${id}'>`;

            item.addEventListener("click", function () {
              // Asignar el valor seleccionado al input de especialidad
              inputEspecialidad = document.getElementById('INPUT_ESPECIALIDADES_' + (i + 1));
              inputEspecialidad.value = this.querySelector("input").value;

              // Asignar el ID correspondiente al input de ID
              inputIdEspecialidad = document.getElementById('INPUT_ID_ESPECIALIDADES_' + (i + 1));
              inputIdEspecialidad.value = this.querySelector("input").getAttribute("data-id");

              opcionSeleccionada = true; // Marcar como seleccionada una opción
              cerrarListaAutocompletado();
            });

            divItems.appendChild(item);
          });
        })
        .catch(error => console.error("Error:", error));
    });

    inputEspecialidad.addEventListener("blur", function () {
      setTimeout(() => {
        if (!opcionSeleccionada) {
          inputEspecialidad = document.getElementById('INPUT_ESPECIALIDADES_' + (i + 1));
          inputIdEspecialidad = document.getElementById('INPUT_ID_ESPECIALIDADES_' + (i + 1));


          // Si no se seleccionó una opción, limpiar ambos inputs
          inputEspecialidad.value = '';
          inputIdEspecialidad.value = '';
        }
      }, 200); // Un pequeño retraso para manejar la selección correcta
    });

    function cerrarListaAutocompletado() {
      var items = row.querySelectorAll(".autocomplete-items div");
      items.forEach(item => item.remove());
    }

    document.addEventListener("click", function (e) {
      if (!row.contains(e.target)) {
        cerrarListaAutocompletado();
      }
    });
  }
}

document.addEventListener("DOMContentLoaded", function () {
  configurar_autocompletado_especialidad();
});



function validar_rfc(input_rfc){
  rfc = input_rfc.value
  fetch(`/api/validar_rfc_proveedores/?rfc=${rfc}`)
  .then((response) => {
      console.log("Respuesta del servidor:", response);
      if (!response.ok) {
      throw new Error("Network response was not ok");
      }
      return response.json();
  }).then((data) => {
      existeRFC = data

      if (existeRFC) {
          Swal.fire({
          title: "Este RFC le pertenece a otro proveedor",
          text: "Por favor, valide la información.",
          icon: "warning", 
          customClass: {
          confirmButton: "custom-button",
              },
          });
          input_rfc.value = ""    
      }


      
  }).catch((error) => console.error("Error en la solicitud Fetch:", error));


}