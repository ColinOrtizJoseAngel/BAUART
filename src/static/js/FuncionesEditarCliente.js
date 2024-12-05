document.addEventListener("DOMContentLoaded", function () {

  console.log("HOLA MUNDO DE FUNCIONES CLIENTES")
  });
  
  // VALIDAR FORMULARIO 
  (() => {
    "use strict";
  
    const forms = document.querySelectorAll(".needs-validation");
  
    Array.from(forms).forEach((form) => {
      form.addEventListener(
        "submit",
        (event) => {
          if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
  
            Swal.fire({
              title: "Faltan campos",
              text: "Por favor, complete todos los campos requeridos.",
              icon: "warning", 
              customClass: {
                confirmButton: "custom-button",
              },
            });
          }
  
          var tabla = document.getElementById("Contactos");
          var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
          var numFilas = cuerpoTabla.rows.length;
          console.log("NUMERO FILAS" + numFilas);
          
          if (numFilas === 0) {
            Swal.fire({
              title: "Falta Contacto",
              text: "Por favor, añade al menos un contacto antes de continuar.",
              icon: "warning",
              customClass: {
                confirmButton: "btn btn-warning",
              },
            });
          }
          var tablaBancos = document.getElementById("Cuentas");
          var cuerpoTablaBancos = tablaBancos.getElementsByTagName("tbody")[0];
          var numFilasBancos = cuerpoTablaBancos.rows.length;
          console.log("NUMERO FILAS" + numFilasBancos);
  
          if (numFilasBancos === 0) {
  
            Swal.fire({
              title: "Falta Cuenta Bancaria",
              text: "No has añadido ninguna cuenta bancaria. Puedes continuar sin agregarla.",
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
  
  
  
  // FUNCION PARA AÑADIR CONTACTOS
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
        <input type="text"  class="form-control" placeholder="NOMBRE" name="NOMBRE_CONTACTO[]" required>
        <div class="invalid-feedback">
          COMPLETA NOMBRE
        </div>`;
  
    cell2.innerHTML = `
        <input type="text"  class="form-control" placeholder="APELLIDO" name="APELLIDO_CONTACTO[]" required>
        <div class="invalid-feedback">
          COMPLETA APELLIDO 
        </div>`;
  
    cell3.innerHTML = `
        <input type="tel"  class="form-control" placeholder="TELEFONO" name="TELEFONO_CONTACTO[]" required>
        <div class="invalid-feedback">
          COMPLETA TELEFONO
        </div>`;
  
    cell4.innerHTML = `
        <input type="text"  class="form-control" placeholder="CORREO DE CONTACTO" name="CORREO_CONTACTO[]" required>
        <div class="invalid-feedback">
          COMPLETA CORREO 
        </div>`;
  
    cell5.innerHTML = `
        <input type="text"  class="form-control" placeholder="PUESTO DE CONTACTO" name="PUESTO_CONTACTO[]" required>
        <div class="invalid-feedback">
          COMPLETA PUESTO
        </div>`;
  
    cell6.innerHTML =
      '<div class="d-flex align-items-center justify-content-center" style="height: 100%;">' +
      '<button onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i></button>' +
      "</div>";
  }
  
  //FUNCION PARA ELIMINAR FILA
  function eliminarFila(btn) {
    var row = btn.parentNode.parentNode.parentNode; // Navegar del botón a la celda, de la celda a la fila
    row.parentNode.removeChild(row); // Eliminar la fila del DOM
  }
  
  //FUNCIONES PARA AÑADIR CUENTA BANCARIA
  function añadirCuenta() {
    var tabla = document.getElementById("Cuentas");
    var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
    var newRow = cuerpoTabla.insertRow(0);
  
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3); // Celda para el botón de eliminar
  
    cell1.innerHTML = `
        <select id="SELECT_BANCO" class="form-control" name="ID_BANCO[]" required>
          <option value="" style="text-align: center;">SELECCIONA</option>
        </select>
        <div class="invalid-feedback">
          SELECCIONE UN BANCO
        </div>`;
  
    cell2.innerHTML = `
        <input type="text" class="form-control" name="NUM_CUENTA[]" placeholder="NUMERO DE CUENTA" maxlength="19" required oninput="formatearCuenta(this)">
        <div class="invalid-feedback">
          COMPLETA NO CUENTA
        </div>`;
  
    cell3.innerHTML = `
        <input type="text" class="form-control" name="CLABE[]" maxlength="23" placeholder="CLABE" required oninput="formatearCLABE(this)">
        <div class="invalid-feedback">
          COMPLETA CLABE
        </div>`;
  
    cell4.innerHTML = `
        <div class="d-flex align-items-center justify-content-center" style="height: 100%;">
          <button onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i> </button>
        </div>`;
  
    cargaBancos(newRow);
  }
  
  //FORMATEAR CUENTA
  function formatearCuenta(input) {
    // Remover todos los caracteres que no sean dígitos
    let value = input.value.replace(/\D/g, "");
  
    // Limitar a 16 dígitos
    value = value.substring(0, 16);
  
    // Añadir guion cada 4 dígitos
    input.value = value.replace(/(\d{4})(?=\d)/g, "$1-");
  }
  
  //FORAMATERA CLABE
  function formatearCLABE(input) {
    // Remover todos los caracteres que no sean dígitos
    let value = input.value.replace(/\D/g, "");
  
    // Limitar a 18 dígitos
    value = value.substring(0, 18);
  
    // Añadir guion cada 3 dígitos
    input.value = value.replace(/(\d{3})(?=\d)/g, "$1-");
  }
  
  // FUNCION PARA CONSULTAR LOS BANCOS ACTIVOS
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
  
  
  function validar_rfc(input_rfc){
    rfc = input_rfc.value
    fetch(`/api/validar_rfc_clientes/?rfc=${rfc}`)
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
            title: "Este RFC le pertenece a otro cliente",
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
  