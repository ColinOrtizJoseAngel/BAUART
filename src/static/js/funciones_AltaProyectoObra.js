document.addEventListener("DOMContentLoaded", function () {

    console.log("DOM completamente cargado y analizado"); // Verificar si el DOM está cargado
    // Encuentra el input de cliente y empresa en el DOM
    var inputCliente = document.querySelector("#cliente");
    var inputEmpresa = document.querySelector("#empresa");
    var inputClienteId = document.querySelector("#cliente_id");
    var nombre_empresa = document.querySelector("#nombre_empresa")
  
    console.log("Input Cliente:", inputCliente); // Verificar si el elemento se encuentra
    console.log("Input Empresa:", inputEmpresa); // Verificar si el elemento se encuentra
    console.log("Input cliente_id:", inputClienteId); // Verificar si el elemento se encuentra
  
    if (inputCliente) {
        configurar_autocompletado(inputCliente, inputEmpresa, inputClienteId,nombre_empresa);
    }

    
  });
  



  function configurar_autocompletado(inputCliente, inputEmpresa, inputClienteId,inputNombreEmpresa) {
    var clientesDisponibles = [];
    var opcionSeleccionada = false;
  
    inputCliente.addEventListener("input", function () {
        var val = this.value;
        console.log(`Valor del input: ${val}`); // Verificar el valor del input
  
        cerrarListaAutocompletado();
        opcionSeleccionada = false;
  
        if (!val) {
            inputEmpresa.value = ''; // Limpiar empresa si se borra el texto
            inputClienteId.value = ''; // Limpiar cliente_id si se borra el texto
            console.log("Valor vacío, limpiando inputEmpresa y inputClienteId");
            return false;
        }
  
        // Depuración: Log para verificar la solicitud
        console.log(`Buscando clientes con el valor: ${val}`);
  
        fetch(`/api/obtener_Cliente/?query=${val}`)
            .then(response => {
                console.log("Respuesta del servidor:", response); // Verificar la respuesta del servidor
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then(data => {
                // Depuración: Log para verificar los datos recibidos
                console.log("Datos recibidos de la API:", data);
  
                clientesDisponibles = data;
                var divItems = document.querySelector("#suggestions");
  
                if (divItems) {
                    divItems.innerHTML = ''; // Limpiar elementos anteriores
                    data.forEach(cliente => {
                        var razonSocial = cliente.razon_social;
                        var idEmpresa = cliente.id_empresa;
                        var nombre_empresa = cliente.nombre_empresa;
                        var id = cliente.id;
                        var regex = new RegExp(`(${val})`, 'gi');
                        var item = document.createElement("div");
                        item.classList.add("list-group-item"); // Añadir una clase para estilo, si es necesario
  
                        // Resaltar coincidencias en la razón social
                        item.innerHTML = razonSocial.replace(regex, "<strong>$1</strong>");
                        item.innerHTML += `<input type='hidden' value='${razonSocial}' data-id-empresa='${idEmpresa}' data-id='${id}' data-nombre_empres='${nombre_empresa}'>
                        
                        `;
  
                        item.addEventListener("click", function () {
                            console.log("Elemento seleccionado:", this.querySelector("input").value); // Verificar el valor del elemento seleccionado
                            inputCliente.value = this.querySelector("input").value;
                            inputEmpresa.value = this.querySelector("input").getAttribute("data-id-empresa");
                            inputClienteId.value = this.querySelector("input").getAttribute("data-id"); // Cambiado aquí
                            inputNombreEmpresa.value = this.querySelector("input").getAttribute("data-nombre_empres")
  
                            opcionSeleccionada = true;
                            cerrarListaAutocompletado();
                        });
  
                        divItems.appendChild(item);
                    });
                } else {
                    console.log("No se encontró el contenedor de sugerencias.");
                }
            })
            .catch(error => console.error("Error en la solicitud Fetch:", error));
    });
  
    inputCliente.addEventListener("blur", function () {
        setTimeout(() => {
            if (!opcionSeleccionada) {
                inputCliente.value = '';
                inputEmpresa.value = '';
                inputClienteId.value = ''; // Limpiar inputClienteId cuando se borra el texto
                console.log("No se seleccionó ninguna opción, limpiando los inputs.");
            }
        }, 200);
    });
  
    function cerrarListaAutocompletado() {
        var items = document.querySelectorAll("#suggestions .list-group-item");
        items.forEach(item => item.remove());
        console.log("Lista de autocompletado cerrada.");
    }
  
    document.addEventListener("click", function (e) {
        // Cerrar lista si se hace clic fuera del campo de entrada y sugerencias
        if (!e.target.matches('#cliente') && !e.target.matches('#suggestions') && !e.target.closest('#suggestions')) {
            cerrarListaAutocompletado();
            console.log("Hizo clic fuera del campo de entrada y sugerencias.");
        }
    });
  }
  


  function initMap() {
    // Obtener el campo de entrada para autocompletar
    const input = document.getElementById('inputDirecionObra');
    if (!input) {
        console.error("Campo 'autocomplete' no encontrado");
        return;
    }
  
    // Configurar el autocompletado, restringido solo a direcciones
    const autocomplete = new google.maps.places.Autocomplete(input, { types: ['address'] });
  
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
  
        // Colocar un marcador en la ubicación seleccionada
        new google.maps.Marker({
            position: { lat: lat, lng: lng },
            map: map,
        });
    });
  }
  
  // Asegurarse de que initMap se ejecute cuando la ventana esté cargada
  window.addEventListener('load', initMap);
  
  
    // Función que muestra/oculta el div en función del switch
    document.getElementById('checkLugarEntrega').addEventListener('change', function () {
      const cotenedorLugarEntrega = document.getElementById('contendorLugarEntrega');
      const inputDirecionObra = document.getElementById("inputDirecionObra");
     
  
      if (this.checked) {
          cotenedorLugarEntrega.classList.remove("oculto");  // Mostrar el formulario
          
          inputDirecionObra.setAttribute('required', true);
     
      } else {
          cotenedorLugarEntrega.classList.add("oculto") // Ocultar el formulario
          inputDirecionObra.removeAttribute('required');
          
      
      }
  });