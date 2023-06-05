from flask import Blueprint, render_template  # Importa la clase Blueprint y la función render_template de Flask
from controllers.usuarios_controller import registrar_usuario  # Importa la función registrar_usuario desde el módulo usuario_controller del paquete controllers
from controllers.usuarios_controller import validar_usuario  # Importa la función validar_usuario desde el módulo usuario_controller del paquete controllers
from controllers.usuarios_controller import salir  # Importa la función salir desde el módulo usuario_controller del paquete controllers

rutasUsuario = Blueprint('usuario', __name__)  # Crea un objeto Blueprint llamado 'rutasUsuario' con el nombre de módulo 'usuario'

@rutasUsuario.route('/')  # Define una ruta para el punto de acceso '/'
def root():  # Define la función asociada a la ruta '/'
    return render_template('iniciar_sesion.html')  # Renderiza la plantilla 'iniciar_sesion.html'

@rutasUsuario.route('/validar_usuario', methods=['POST'])  # Define una ruta para '/validar_usuario' con el método POST
def validar_login():  # Define la función asociada a la ruta '/validar_usuario'
    return validar_usuario()  # Llama a la función validar_usuario

@rutasUsuario.route('/registro_usuario')  # Define una ruta para '/registro_usuario'
def vista_registro():  # Define la función asociada a la ruta '/registro_usuario'
    return render_template('registrarse.html')  # Renderiza la plantilla 'registrarse.html'

@rutasUsuario.route('/nuevo_usuario', methods=['POST'])  # Define una ruta para '/nuevo_usuario' con el método POST
def nuevo_registro():  # Define la función asociada a la ruta '/nuevo_usuario'
    return registrar_usuario()  # Llama a la función registrar_usuario

@rutasUsuario.route('/cerrar_sesión')  # Define una ruta para '/cerrar_sesión'
def cerrar_sesion():  # Define la función asociada a la ruta '/cerrar_sesión'
    return salir()  # Llama a la función salir