document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Obtener el elemento de carga de imágenes y la alerta de imagen no válida
    var imageInput = document.getElementById('imageUpload');
    var invalidImageAlert = document.getElementById('invalidImageAlert');

    // Ocultar la alerta de imagen no válida
    invalidImageAlert.classList.add('d-none');

    // Verificar si no se seleccionó ninguna imagen
    if (imageInput.files.length === 0) {
        invalidImageAlert.classList.remove('d-none');
    }
});
