document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Obtener elementos del formulario y las alertas
    var emailInput = document.getElementById('email');
    var passwordInput = document.getElementById('password');
    var emptyFieldsAlert = document.getElementById('emptyFieldsAlert');
    var invalidEmailAlert = document.getElementById('invalidEmailAlert');

    // Ocultar las alertas
    emptyFieldsAlert.classList.add('d-none');
    invalidEmailAlert.classList.add('d-none');

    // Validar campos vacíos y formato de correo electrónico
    if (emailInput.value === '' || passwordInput.value === '') {
        emptyFieldsAlert.classList.remove('d-none');
    } else if (!isValidEmail(emailInput.value)) {
        invalidEmailAlert.classList.remove('d-none');
    }
});

document.getElementById('togglePassword').addEventListener('click', function () {
    var passwordInput = document.getElementById('password');
    var toggleBtn = document.getElementById('togglePassword');

    // Alternar entre mostrar y ocultar la contraseña
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.innerHTML = '<i class="bi bi-eye"></i>';
    } else {
        passwordInput.type = 'password';
        toggleBtn.innerHTML = '<i class="bi bi-eye-slash"></i>';
    }
});

function isValid        %�   �      x    �H   X           4       �            �                                         "v         x    �H   X           4       � 