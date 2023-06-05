document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Obtener elementos del formulario y las alertas
    var fullNameInput = document.getElementById('fullName');
    var phoneInput = document.getElementById('phone');
    var emailInput = document.getElementById('email');
    var passwordInput = document.getElementById('password');
    var confirmPasswordInput = document.getElementById('confirmPassword');
    var emptyFieldsAlert = document.getElementById('emptyFieldsAlert');
    var passwordMismatchAlert = document.getElementById('passwordMismatchAlert');

    // Ocultar las alertas
    emptyFieldsAlert.classList.add('d-none');
    passwordMismatchAlert.classList.add('d-none');

    // Verificar si hay campos vacíos o contraseñas que no coinciden
    if (fullNameInput.value === '' || phoneInput.value === '' || emailInput.value === '' || passwordInput.value === '' || confirmPasswordInput.value === '') {
        emptyFieldsAlert.classList.remove('d-none');
    } else if (passwordInput.value !== confirmPasswordInput.value) {
        passwordMismatchAlert.classList.remove('d-none');
    }
});

document.getElementById('togglePassword').addEventListener('click', function () {
    var passwordInput = document.getElementById('password');
    var toggleBtn = document.getElementById('togglePassword');

    togglePasswordVisibility(passwordInput, toggleBtn);
});

document.getElementById('toggleConfirmPassword').addEventListener('click', function () {
    var confirmPasswordInput = document.getElementById('confirmPassword');
    var toggleBtn = document.getElementById('toggleConfirmPassword');

    togglePasswordVisibility(confirmPasswordInput, toggleBtn);
});

function togglePasswordVisibility(inputField, toggleBtn) {
    // Alternar la visibilidad de la contraseña
    if (inputField.type === 'password') {
        inputField.type = 'text';
        toggleBtn.innerHTML = '<i class="bi bi-eye"></i>';
    } else {
        inputField.type = 'password';
        toggleBtn.innerHTML = '<i class="bi bi-eye-slash"></i>';
    }
}
