const ModalEditFamilia = document.getElementById('ModalEditFamilia');
 console.log("Este es el modal "+ ModalEditFamilia)
 ModalEditFamilia.addEventListener('show.bs.modal', event => {
      const button = event.relatedTarget;
      const id = button.getAttribute('data-id');
      const familia = button.getAttribute('data-familia');

      var inputFamiliaEdit = ModalEditFamilia.querySelector("#inputFamiliaEdit");

      inputFamiliaEdit.value = familia;

      const form = ModalEditFamilia.querySelector('form');
      console.log(form)
      form.action = `/edit_familia/${id}`;
  });
