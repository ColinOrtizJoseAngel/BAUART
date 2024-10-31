document.querySelectorAll('input[type="text"]').forEach(function(input) {
    input.addEventListener('input', function() {
        this.value = this.value.toUpperCase();
    });
  });