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

  document.getElementById("NO_REGISTRO_PATRONAL").value = "";
  document.getElementById("ESTADO_REPRESENTANTE").value = "";
}

function eliminarFila(btn) {
  var row = btn.parentNode.parentNode.parentNode; // Navegar del botón a la celda, de la celda a la fila
  row.parentNode.removeChild(row); // Eliminar la fila del DOM
}
