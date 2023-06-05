from flask import request, redirect, session  # Importa las clases request, redirect y session de Flask
from models.usuarios import Usuario  # Importa la clase Usuario desde el módulo usuarios del paquete models
from app import db  # Importa el objeto db desde el módulo app

def registrar_usuario():  # Define la función registrar_usuario()
    try:
        nombreCompleto = request.form['nombre']  # Obtiene el valor del campo 'nombre' del formulario enviado
        telefono = request.form['telefono']  # Obtiene el valor del campo 'telefono' del formulario enviado
        correo = request.form['correo']  # Obtiene el valor del campo 'correo' del formulario enviado
        password = request.form['password']  # Obtiene el valor del campo 'password' del formulario enviado

        nuevoUsuario = Usuario(nombreCompleto, telefono, correo, password)  # Crea un nuevo objeto Usuario con los datos proporcionados

        db.session.add(nuevoUsuario)  # Agrega el nuevoUsuario a la sesión de la base de datos
        db.session.commit()  # Confirma los cambios en la base de datos

        return redirect('/registro_usuario')  # Redirige al punto de acceso '/registro_usuario'
    except Exception as e:  # Captura cualquier excepción que ocurra
        return redirect('/registro_usuario')  # En caso de excepción, redirige al punto de acceso '/registro_usuario'

def validar_usuario():  # Define la función validar_usuario()
    try:
        correo = request.form['correo']  # Obtiene el valor del campo 'correo' del formulario enviado
        password = request.form['password']  # Obtiene el valor del campo 'password' del formulario enviado

        usuario = Usuario.query.filter_by(correo=correo).first()  # Realiza una consulta a la base de datos para obtener el usuario con el correo proporcionado

        if usuario and usuario.comparar_contraseña(password):  # Verifica si el usuario existe y la contraseña es correcta
            session['id_usuario'] = usuario.id  # Almacena el ID del usuario en la sesión
            return redirect('/prediccion_felinos')  # Redirige al punto de acceso '/prediccion_felinos'

        return redirect('/')  # Si no se cumple la condición anterior, redirige al punto de acceso '/'
    except Exception as e:  # Captura cualquier excepción que ocurra
        return redirect('/')  # En caso de excepción, redirige al punto de acceso '/'

def salir():  # Define la función salir()
    session.pop('id_usuario', None)  # Elimina la clave 'id_usuario' de la sesión, si existe
    return redirect('/')  # Redirige al punto de acceso '/'