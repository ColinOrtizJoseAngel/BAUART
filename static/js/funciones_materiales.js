document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM completamente cargado y analizado");
  var FamiliaFiltro = document.querySelector("#FamiliaFiltro");
  var FamiliaID = document.querySelector("#FamiliaID"); // Obtener el campo para el ID

  if (FamiliaFiltro) {
    console.log("Input FamiliaFiltro encontrado:", FamiliaFiltro);
    configurar_autocompletado(FamiliaFiltro, FamiliaID); // Pasar también el campo ID
  } else {
    console.error("No se encontró el elemento con id #FamiliaFiltro");
  }
});

function configurar_autocompletado(FamiliaFiltro, FamiliaID) {
  console.log("Configurando autocompletado para el campo:", FamiliaFiltro);
  var opcionSeleccionada = false;

  // Evento que se activa cada vez que se escribe algo en el campo
  FamiliaFiltro.addEventListener("input", function () {
    var val = this.value;

    // Imprime lo que se va escribiendo en el campo
    console.log("Texto que se está escribiendo:", val);

    cerrarListaAutocompletado(); // Cerrar lista de autocompletado previa
    opcionSeleccionada = false;

    if (!val) {
      console.log("Input vacío, se limpia el valor.");
      cerrarListaAutocompletado();
      return false;
    }

    console.log(`Buscando familias con el valor: ${val}`);

    // Realizar la solicitud al servidor con el valor ingresado
    fetch(`/api/llenar_familia/?query=${val}`)
      .then((response) => {
        if (!response.ok) {
          console.error("Error en la respuesta del servidor:", response);
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Datos recibidos de la API:", data);

        var divItems = document.querySelector("#suggestions");

        if (divItems) {
          divItems.innerHTML = ""; // Limpiar sugerencias previas
          console.log("Sugerencias limpias, procesando nuevas opciones...");

          if (data.length > 0) {
            data.forEach((familiaData) => {
              var familia = familiaData.familia; // El nombre de la familia
              var idFamilia = familiaData.id; // ID de la familia
              var regex = new RegExp(`(${val})`, "gi");
              var item = document.createElement("div");
              item.classList.add("list-group-item");

              // Resaltamos el texto coincidente
              item.innerHTML = familia.replace(regex, "<strong>$1</strong>");
              item.innerHTML += `<input type='hidden' value='${familia}' data-id='${idFamilia}'>`; // Guardar ID en un input oculto

              // Agregar evento click a cada sugerencia
              item.addEventListener("click", function () {
                console.log("Elemento seleccionado:", this.querySelector("input").value);
                FamiliaFiltro.value = this.querySelector("input").value; // Establecer el nombre de la familia
                FamiliaID.value = idFamilia; // Establecer el ID de la familia
                console.log("ID de Familia seleccionada:", idFamilia);

                opcionSeleccionada = true;
                cerrarListaAutocompletado();
              });

              divItems.appendChild(item);
            });

            divItems.style.display = "block"; // Mostrar el contenedor de sugerencias
            console.log("Sugerencias visibles.");

          } else {
            console.log("No se encontraron resultados para la búsqueda.");
            divItems.style.display = "none"; // Ocultar si no hay resultados
          }
        } else {
          console.error("No se encontró el contenedor de sugerencias con id #suggestions.");
        }
      })
      .catch((error) => console.error("Error en la solicitud Fetch:", error));
  });

  FamiliaFiltro.addEventListener("blur", function () {
    setTimeout(() => {
      if (!opcionSeleccionada) {
        FamiliaFiltro.value = "";
        FamiliaID.value = ""; // Limpiar el ID si no se seleccionó nada
        console.log("Ninguna opción seleccionada, limpiando los campos.");
      }
    }, 200);
  });



  

  // Función para cerrar el autocompletado
  function cerrarListaAutocompletado() {
    var items = document.querySelectorAll("#suggestions .list-group-item");
    items.forEach((item) => item.remove());
    var divItems = document.querySelector("#suggestions");
    divItems.style.display = "none"; // Ocultar el contenedor de sugerencias
    console.log("Lista de autocompletado cerrada.");
  }

  // Cerrar autocompletado si se hace clic fuera del input o de la lista de sugerencias
  document.addEventListener("click", function (e) {
    if (
      !e.target.matches("#FamiliaFiltro") &&
      !e.target.matches("#suggestions") &&
      !e.target.closest("#suggestions")
    ) {
      cerrarListaAutocompletado();
      console.log("Hizo clic fuera del campo de entrada o lista de sugerencias, cerrando autocompletado.");
    }
  });
}

 const editMaterialesModal = document.getElementById('modalEditarMaterial');
 console.log("Este es el modal "+ editMaterialesModal)
 editMaterialesModal.addEventListener('show.bs.modal', event => {
      const button = event.relatedTarget;
      console.log("hola mundo soy el button"+button)
      const id = button.getAttribute('data-material-id');
      console.log(id)
      const material = button.getAttribute('data-material');
      const familia = button.getAttribute('data-material-familia');
      const uom = button.getAttribute('data-material-uom');

      var inputFamiliaEdit = editMaterialesModal.querySelector("#inputFamiliaEdit");
      var inputIdFamiliaEdit = editMaterialesModal.querySelector("#inputIdFamiliaEdit"); // Obtener el campo para el ID



   
      inputFamiliaEdit.value = familia;

      const inputDecripcion = editMaterialesModal.querySelector('#inputDecripcion');
      inputDecripcion.value = material;

      const inputUOM  = editMaterialesModal.querySelector('#inputUOMEdit');
      inputUOM.value = uom;


      configurar_autocompletado_edit(inputFamiliaEdit,inputIdFamiliaEdit)


      const form = editMaterialesModal.querySelector('form');
      console.log(form)
      form.action = `/edit_materiales/${id}`;
  });

  function configurar_autocompletado_edit(FamiliaFiltro, FamiliaID) {
    console.log("Configurando autocompletado para el campo:", FamiliaFiltro);
    var opcionSeleccionada = false;
  
    // Evento que se activa cada vez que se escribe algo en el campo
    FamiliaFiltro.addEventListener("input", function () {
      var val = this.value;
  
      // Imprime lo que se va escribiendo en el campo
      console.log("Texto que se está escribiendo:", val);
  
      cerrarListaAutocompletado(); // Cerrar lista de autocompletado previa
      opcionSeleccionada = false;
  
      if (!val) {
        console.log("Input vacío, se limpia el valor.");
        cerrarListaAutocompletado();
        return false;
      }
  
      console.log(`Buscando familias con el valor: ${val}`);
  
      // Realizar la solicitud al servidor con el valor ingresado
      fetch(`/api/llenar_familia/?query=${val}`)
        .then((response) => {
          if (!response.ok) {
            console.error("Error en la respuesta del servidor:", response);
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          console.log("Datos recibidos de la API:", data);
  
          var divItems = document.querySelector("#suggestions-editar");
  
          if (divItems) {
            divItems.innerHTML = ""; // Limpiar sugerencias previas
            console.log("Sugerencias limpias, procesando nuevas opciones...");
  
            if (data.length > 0) {
              data.forEach((familiaData) => {
                var familia = familiaData.familia; // El nombre de la familia
                var idFamilia = familiaData.id; // ID de la familia
                var regex = new RegExp(`(${val})`, "gi");
                var item = document.createElement("div");
                item.classList.add("list-group-item");
  
                // Resaltamos el texto coincidente
                item.innerHTML = familia.replace(regex, "<strong>$1</strong>");
                item.innerHTML += `<input type='hidden' value='${familia}' data-id='${idFamilia}'>`; // Guardar ID en un input oculto
  
                // Agregar evento click a cada sugerencia
                item.addEventListener("click", function () {
                  console.log("Elemento seleccionado:", this.querySelector("input").value);
                  FamiliaFiltro.value = this.querySelector("input").value; // Establecer el nombre de la familia
                  FamiliaID.value = idFamilia; // Establecer el ID de la familia
                  console.log("ID de Familia seleccionada:", idFamilia);
  
                  opcionSeleccionada = true;
                  cerrarListaAutocompletado();
                });
  
                divItems.appendChild(item);
              });
  
              divItems.style.display = "block"; // Mostrar el contenedor de sugerencias
              console.log("Sugerencias visibles.");
  
            } else {
              console.log("No se encontraron resultados para la búsqueda.");
              divItems.style.display = "none"; // Ocultar si no hay resultados
            }
          } else {
            console.error("No se encontró el contenedor de sugerencias con id #suggestions.");
          }
        })
        .catch((error) => console.error("Error en la solicitud Fetch:", error));
    });
  
    FamiliaFiltro.addEventListener("blur", function () {
      setTimeout(() => {
        if (!opcionSeleccionada) {
          FamiliaFiltro.value = "";
          FamiliaID.value = ""; // Limpiar el ID si no se seleccionó nada
          console.log("Ninguna opción seleccionada, limpiando los campos.");
        }
      }, 200);
    });
  
  
  
    
  
    // Función para cerrar el autocompletado
    function cerrarListaAutocompletado() {
      var items = document.querySelectorAll("#suggestions-editar .list-group-item");
      items.forEach((item) => item.remove());
      var divItems = document.querySelector("#suggestions-editar");
      divItems.style.display = "none"; // Ocultar el contenedor de sugerencias
      console.log("Lista de autocompletado cerrada.");
    }
  
    // Cerrar autocompletado si se hace clic fuera del input o de la lista de sugerencias
    document.addEventListener("click", function (e) {
      if (
        !e.target.matches("#inputFamiliaEdit") &&
        !e.target.matches("#suggestions-editar") &&
        !e.target.closest("#suggestions-editar")
      ) {
        cerrarListaAutocompletado();
        console.log("Hizo clic fuera del campo de entrada o lista de sugerencias, cerrando autocompletado.");
      }
    });
  }
  