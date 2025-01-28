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
  
  // FUNCION PARA VALIDAR FECHAS DE INICIO Y FIN DE PROYECTO
  function validarFechas(){
    console.log("SE EJECUTA VALIDAR FECHAS")
    const fechaInicio = document.getElementById('fecha_inicio');
    const fechaFin = document.getElementById('fecha_fin');

    const inicio = new Date(fechaInicio.value);
    const fin = new Date(fechaFin.value);

        if (inicio && fin) {
            if (fin < inicio) {
                // Mostrar alerta
                alert("La fecha de fin no puede ser menor que la fecha de inicio. Por favor, corrige las fechas.");
                
                // Vaciar los campos
                fechaInicio.value = '';
                fechaFin.value = '';
            }
        }
    }
  

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
  
