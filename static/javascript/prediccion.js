// Datos de cada span
const porcentajeLeon = document.getElementById('leon').textContent;
const porcentajeGato = document.getElementById('gato').textContent;
const porcentajeTigre = document.getElementById('tigre').textContent;
const porcentajePantera = document.getElementById('pantera').textContent;

// Span para la barra de progreso de predicción
document.getElementById('barraLeon').style.width = porcentajeLeon;
document.getElementById('barraGato').style.width = porcentajeGato;
document.getElementById('barraTigre').style.width = porcentajeTigre;
document.getElementById('barraPantera').style.width = porcentajePantera;

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