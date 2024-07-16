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
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();

          Swal.fire({
            title: "Faltan campos",
            text: "Por favor, complete todos los campos requeridos.",
            icon: "warning", // Cambié el icono a 'warning' para que coincida mejor con el mensaje.
            customClass: {
              confirmButton: "custom-button",
            },
          });
        }
        // Comprobación del número de filas en la tabla de registros patronales

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

        form.classList.add("was-validated");
      },
      false
    );
  });
})();
