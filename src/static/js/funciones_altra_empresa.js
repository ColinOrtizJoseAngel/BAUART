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

        var tabla = document.getElementById("Registros_Patronales");
        var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
        var numFilas = cuerpoTabla.rows.length;
        console.log("NUMERO FILAS" + numFilas);
        
        if (numFilas === 0) {
          Swal.fire({
            title: "Falta Registro Patronal",
            text: "Por favor, añade al menos un registro patronal antes de continuar.",
            icon: "warning",
            customClass: {
              confirmButton: "btn btn-warning",
            },
          });
        }
        var tablaBancos = document.getElementById("Cuentas_Bancarias");
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


// FUNCION PARA VALIDAR RFC
function validar_rfc(input_rfc){
  rfc = input_rfc.value
  fetch(`/api/validar_rfc_empresas/?rfc=${rfc}`)
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
          title: "Este RFC le pertenece a otra empresa",
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



// FUNCION PARA AÑADIR UN REGISTRO PATRONAL
function añadirRegistro() {
  var tabla = document.getElementById("Registros_Patronales");
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
  var newRow = cuerpoTabla.insertRow(0);

  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2); // Celda para el botón de eliminar

  cell1.innerHTML =`
      <input type="text"  class="form-control" name="noRegistro[]" placeholder="NÚMERO DE REGISTRO PATRONAL" required>
      <div class="invalid-feedback">
        COMPLETA NO REGISTRO PATRONAL
      </div>
  `;
  cell2.innerHTML =`
        <select id="selectEstados" class="form-control" name="estado[]" required>
          <option id="selectEstados" value="" style="text-align: center;">SELECIONA UN ESTADO</option>
          <option value="AGUASCALIENTES">AGUASCALIENTES</option>
          <option value="BAJA CALIFORNIA">BAJA CALIFORNIA</option>
          <option value="BAJA CALIFORNIA SUR">BAJA CALIFORNIA SUR</option>
          <option value="CHIAPAS">CHIAPAS</option>
          <option value="CHIHUAHUA">CHIHUAHUA</option>
          <option value="CIUDAD DE MÉXICO">CIUDAD DE MÉXICO</option>
          <option value="COAHUILA">COAHUILA</option>
          <option value="COLIMA">COLIMA</option>
          <option value="DURANGO">DURANGO</option>
          <option value="ESTADO DE MÉXICO">ESTADO DE MÉXICO</option>
          <option value="GUANAJUATO">GUANAJUATO</option>
          <option value="GUERRERO">GUERRERO</option>
          <option value="HIDALGO">HIDALGO</option>
          <option value="JALISCO">JALISCO</option>
          <option value="MICHOACÁN">MICHOACÁN</option>
          <option value="MORELOS">MORELOS</option>
          <option value="NAYARIT">NAYARIT</option>
          <option value="NUEVO LEÓN">NUEVO LEÓN</option>
          <option value="OAXACA">OAXACA</option>
          <option value="PUEBLA">PUEBLA</option>
          <option value="QUERÉTARO">QUERÉTARO</option>
          <option value="QUINTANA ROO">QUINTANA ROO</option>
          <option value="SAN LUIS POTOSÍ">SAN LUIS POTOSÍ</option>
          <option value="SIN LOCALIDAD">SIN LOCALIDAD</option>
          <option value="SINALOA">SINALOA</option>
          <option value="SONORA">SONORA</option>
          <option value="TABASCO">TABASCO</option>
          <option value="TAMAULIPAS">TAMAULIPAS</option>
          <option value="TLAXCALA">TLAXCALA</option>
          <option value="VERACRUZ">VERACRUZ</option>
          <option value="YUCATÁN">YUCATÁN</option>
          <option value="ZACATECAS">ZACATECAS</option>
          <option value="SIN LOCALIDAD">SIN LOCALIDAD</option>

        </select>

        <div class="invalid-feedback">
          SELECIONA UN ESTADO
        </div>`;
  cell3.innerHTML =
    '<div class="d-flex align-items-center justify-content-center">' +
    '<button onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i></button>' +
    "</div>";
}

// FUNCION PARA ELIMINAR UNA FILA DE LA TABLA
function eliminarFila(btn) {
  var row = btn.parentNode.parentNode.parentNode;
  row.parentNode.removeChild(row); 
}

// FUNCION PARA AÑADIR CUENTAS BANCARIAS
function añadirCuentasBancarias() {
  var tabla = document.getElementById("Cuentas_Bancarias");
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
  var newRow = cuerpoTabla.insertRow(0);

  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2); // Celda para el botón de eliminar
  var cell4 = newRow.insertCell(3);

  cell1.innerHTML = `
      <select id="SELECT_BANCO" name="BANCO[]" class="form-control" style="text-align: center;" required>
        <option value="">Selecciona un banco</option>
      </select>
      <div class="invalid-feedback">
        SELECIONA UN BANCO
      </div>
    `;

  cell2.innerHTML = `
      <input type="text" class="form-control" name="NO_CUENTA[]" maxlength="19" oninput="formatearCLABE(this)" required>
      <div class="invalid-feedback">
      "COMPLETA NO CUENTA"
      </div>
    `;

  cell3.innerHTML = `
      <input type="text" class="form-control" name="CLABE[]" maxlength="23" oninput="formatearCLABE(this)" required>
      <div class="invalid-feedback">
      "COMPLETA CLABE"
      </div>
    `;
  cell4.innerHTML = `
    <div class="d-flex align-items-center justify-content-center" style="height: 100%;">
      <button onclick="eliminarFila(this)" class="btn"><i class="bi bi-trash"></i></button>
    </div>
    `;

  cargaBancos(newRow);
}

// FORMATO CUENTA BANCARIA
function formatearCuenta(input) {
  // Remover todos los caracteres que no sean dígitos
  let value = input.value.replace(/\D/g, "");

  // Limitar a 16 dígitos
  value = value.substring(0, 16);

  // Añadir guion cada 4 dígitos
  input.value = value.replace(/(\d{4})(?=\d)/g, "$1-");
}

// FORMMATO CLABE
function formatearCLABE(input) {
  // Remover todos los caracteres que no sean dígitos
  let value = input.value.replace(/\D/g, "");

  // Limitar a 18 dígitos
  value = value.substring(0, 18);

  // Añadir guion cada 3 dígitos
  input.value = value.replace(/(\d{3})(?=\d)/g, "$1-");
}

//FUNCION PARA CONSULTAR BANCOS
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

