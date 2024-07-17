function añadirRegistro() {
  var tabla = document.getElementById("Registros_Patronales");
  var cuerpoTabla = tabla.getElementsByTagName("tbody")[0];
  var newRow = cuerpoTabla.insertRow(0);

  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2); // Celda para el botón de eliminar

  cell1.innerHTML =
    '<label class="form-label">No Registro Patronal</label>' +
    '<input type="text"  class="form-control" name="noRegistro[]" required>' +
    '<div class="invalid-feedback">' +
    "Completa No de registro patronal" +
    "</div>";
  cell2.innerHTML =
    '<label class="form-label">Estado</label>' +
    '<input type="text" class="form-control" name="estado[]" required>' +
    '<div class="invalid-feedback">' +
    "Completa Estado de resgistro patronal" +
    "</div>";
  cell3.innerHTML =
    '<div class="d-flex align-items-center justify-content-center" style="height: 100%;margin-top: 30px;">' +
    '<button onclick="eliminarFila(this)" class="btn btn-danger"><i class="bi bi-trash"></i> Eliminar</button>' +
    "</div>";
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
  var cell5 = newRow.insertCell(4);

  cell1.innerHTML = "<div>"+
    '<label for="banco-select">Seleccione un banco:</label>' +
    '<select id="banco-select" name="banco-select[]" class="form-control">' +
    '<option value="">Seleccione un banco</option>' +
    "</select>";
  '<div class="invalid-feedback">' + "Completa el banco" + "</div>" + "<div>";

  cell2.innerHTML =
    '<label class="form-label">No. cuenta</label>' +
    '<input type="text" class="form-control" name="noCuenta[]" required>' +
    '<div class="invalid-feedback">' +
    "Completa Estado de resgistro patronal" +
    "</div>";

  cell3.innerHTML =
    '<label class="form-label">CABE</label>' +
    '<input type="text" class="form-control" name="cabe[]" required>' +
    '<div class="invalid-feedback">' +
    "Completa Estado de resgistro patronal" +
    "</div>";

  cell4.innerHTML =
    '<div class="d-flex align-items-center justify-content-center" style="height: 100%;margin-top: 30px;">' +
    '<button onclick="eliminarFila(this)" class="btn btn-danger"><i class="bi bi-trash"></i> Eliminar</button>' +
    "</div>";

  cargaBancos(newRow);
}

function cargaBancos(row) {
  fetch("/api/data")
      .then((response) => {
          if (!response.ok) {
              throw new Error("Network response was not ok");
          }
          return response.json();
      })
      .then((data) => {
          console.log(data);
          const select = row.querySelector("#banco-select");
          data.forEach((banco) => {
              const option = document.createElement("option");
              option.value = banco.id;
              option.textContent = banco.banco;
              select.appendChild(option);
          });
      })
      .catch((error) => console.error("Error:", error));
}


