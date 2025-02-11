document.addEventListener("DOMContentLoaded", function () {

  function cargaCFDI() {
      fetch("/api/obtener_cfdi/")
          .then((response) => {
              if (!response.ok) {
                  console.error(`Error: ${response.status} - ${response.statusText}`);
                  throw new Error("Network response was not ok");
              }
              return response.json();
          })
          .then((data) => {
              console.log(data);
              const select = document.querySelector("#USO_CFDI");

              // Asegúrate de que el elemento select exista antes de intentar manipularlo
              if (select) {
                  data.forEach((cfdi) => {
                      const option = document.createElement("option");
                      cfdis = `${cfdi.nombre} - ${cfdi.decripcion}`;
                      option.value = cfdi.id;
                      option.textContent = cfdis  // Corregí la concatenación de clave y descripción
                      select.appendChild(option);
                  });
              } else {
                  console.error("No se encontró el elemento select con el ID #USO_CFDI.");
              }
          })
          .catch((error) => console.error("Error:", error));
  }

  cargaCFDI();
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
      <input type="text"  class="form-control" style="text-align: center;" placeholder="NOMBRE" name="NOMBRE_CONTACTO[]" required>
      <div class="invalid-feedback">
        COMPLETA NOMBRE
      </div>`;

  cell2.innerHTML = `
      <input type="text"  class="form-control"  style="text-align: center;" placeholder="APELLIDO" name="APELLIDO_CONTACTO[]" required>
      <div class="invalid-feedback">
        COMPLETA APELLIDO 
      </div>`;

  cell3.innerHTML = `
      <input type="tel"  class="form-control" style="text-align: center;" placeholder="TELEFONO" maxlength="10" name="TELEFONO_CONTACTO[]" required>
      <div class="invalid-feedback">
        COMPLETA TELEFONO
      </div>`;

  cell4.innerHTML = `
      <input type="text"  class="form-control" style="text-align: center;" placeholder="CORREO DE CONTACTO" name="CORREO_CONTACTO[]" required>
      <div class="invalid-feedback">
        COMPLETA CORREO 
      </div>`;

  cell5.innerHTML = `
      <input type="text"  class="form-control" style="text-align:center;" placeholder="PESTO DE CONTACTO" name="PUESTO_CONTACTO[]" required>
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
      <input type="text" class="form-control" style="text-align:center;" placeholder="NUMERO DE CUENTA" name="NUM_CUENTA[]" maxlength="19" required oninput="formatearCuenta(this)">
      <div class="invalid-feedback">
        COMPLETA NO CUENTA
      </div>`;

  cell3.innerHTML = `
      <input type="text" class="form-control" style="text-align:center;" placeholder="CLABE" name="CLABE[]" maxlength="23" required oninput="formatearCLABE(this)">
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

function initMap() {
  // Obtener el campo de entrada para autocompletar
  const input = document.getElementById('inputDirecionObra');
  if (!input) {
      console.error("Campo 'autocomplete' no encontrado");
      return;
  }

  // Inicializa el mapa
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 19.432608, lng: -99.133209 }, // Coordenadas de Ciudad de México (por defecto)
    zoom: 14,
  });

  // Agrega un marcador inicial
  marker = new google.maps.Marker({
    map: map,
    draggable: false,
  });

  // Configurar el autocompletado, restringido solo a direcciones
  const autocomplete = new google.maps.places.Autocomplete(input, {
    types: ["address"],
    componentRestrictions: { country: "mx" },
  });

  // Añadir listener para cuando el usuario selecciona una ubicación
  autocomplete.addListener('place_changed', function () {
      const place = autocomplete.getPlace();
      if (!place.geometry) {
          console.error("No se encontró información de ubicación para la dirección");
          return;
      }

      // Obtener latitud y longitud de la ubicación seleccionada
      const lat = place.geometry.location.lat();
      console.log("Esta es la lat" + lat)
      const lng = place.geometry.location.lng();
      console.log("Esta es la lat" + lng)


      // Asignar latitud y longitud a los campos correspondientes
      inputLat = document.getElementById('id_latitud')
      console.log(inputLat)
      inputLat.value = lat
      

      inputlng =document.getElementById('id_longitud')
      inputlng.value = lng

      // Extraer componentes de la dirección y asignarlos a los campos correspondientes
      const addressComponents = place.address_components;
      let street = '', streetNumber = '', neighborhood = '', postalCode = '', state = '', city = '';

      addressComponents.forEach(component => {
          const types = component.types;
          if (types.includes("route")) {
              street = component.long_name; // Calle
          }
          if (types.includes("street_number")) {
              streetNumber = component.long_name; // Número exterior
          }
          if (types.includes("sublocality") || types.includes("neighborhood")) {
              neighborhood = component.long_name; // Colonia
          }
          if (types.includes("postal_code")) {
              postalCode = component.long_name; // Código postal
          }
          if (types.includes("administrative_area_level_1")) {
              state = component.long_name; // Estado
          }
          if (types.includes("locality")) {
              city = component.long_name; // Ciudad
          }
      });

      // Asignar los valores a los campos individuales
      document.getElementById('inputCalle').value = street;
      document.getElementById('inputNumeroExterior').value = streetNumber;
      document.getElementById('inputColonia').value = neighborhood;
      document.getElementById('inputCp').value = postalCode;
      document.getElementById('inputEstado').value = state;
      document.getElementById('inputCiudad').value = city;

      // Centrar el mapa en la ubicación seleccionada
      const map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: lat, lng: lng },
          zoom: 15,
      });

       // Centrar el mapa y mover el marcador
       const location = place.geometry.location;
       map.setCenter(location);
       marker.setPosition(location);

       // Colocar un marcador en la ubicación seleccionada
      new google.maps.Marker({
        position: { lat: lat, lng: lng },
        map: map,
      });
  });
}

// Asegurarse de que initMap se ejecute cuando la ventana esté cargada
window.addEventListener('load', initMap);
