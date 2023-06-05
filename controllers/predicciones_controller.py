from flask import request, render_template, session, url_for, current_app  # Importa funciones y objetos necesarios de Flask
import os  # Importa el módulo 'os' para interactuar con el sistema operativo
import random  # Importa el módulo 'random' para generar valores aleatorios
import string  # Importa el módulo 'string' para trabajar con cadenas de caracteres
import numpy as np  # Importa el módulo 'numpy' para operaciones numéricas
from werkzeug.utils import secure_filename  # Importa una función para asegurar el nombre de archivo
from scipy.special import softmax  # Importa la función softmax del módulo 'scipy.special'
from tensorflow.keras.preprocessing.image import load_img, img_to_array  # Importa funciones para cargar y transformar imágenes
from keras.models import load_model  # Importa la función para cargar un modelo de Keras
from models.predicciones import Prediccion  # Importa la clase 'Prediccion' desde el módulo 'models.prediccion'
from app import db  # Importa el objeto 'db' desde el módulo 'app'

def predict(image_path):
    longitud, altura = 150, 150  # Define las dimensiones deseadas para la imagen

    rutaActual = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ruta actual del archivo
    rutaModelo = os.path.join(rutaActual, '../modelo_ia/modelo.h5')  # Construye la ruta al modelo de IA

    modelo = load_model(rutaModelo)  # Carga el modelo de IA
    classes = ['Gato', 'León', 'Pantera', 'Tigre']  # Define las clases de predicción posibles

    imagen = load_img(image_path, target_size=(altura, longitud))  # Carga la imagen y la redimensiona
    imagenArray = img_to_array(imagen)  # Convierte la imagen a un array
    imagenArray = np.expand_dims(imagenArray, axis=0)  # Añade una dimensión adicional al array

    prediccionPrediccion = modelo.predict(imagenArray)  # Realiza la predicción de la imagen
    probabilidades = softmax(prediccionPrediccion)[0]  # Aplica la función softmax a las probabilidades

    listaPredicciones = []  # Crea una lista para almacenar las predicciones

    for i in enumerate(classes):  # Recorre las clases enumeradas
        porcentaje = round(probabilidades[i] * 100, 2)  # Calcula el porcentaje de predicción
        listaPredicciones.append(porcentaje)  # Agrega el porcentaje a la lista de predicciones

    return listaPredicciones  # Devuelve la lista de predicciones

def procesar_imagen():
    imagen = request.files['imagen']  # Obtiene el archivo de imagen enviado en la solicitud
    nombre = secure_filename(imagen.filename)  # Asegura el nombre del archivo

    chars = string.ascii_letters + string.digits  # Define los caracteres permitidos en el nombre aleatorio
    nombreIMG = ''.join(random.choice(chars) for _ in range(8))  # Genera un nombre aleatorio para la imagen
    extensionIMG = os.path.splitext(nombre)[1]  # Obtiene la extensión del archivo original
    nombreCompleto = nombreIMG + extensionIMG  # Construye el nombre completo del archivo
    ruta_img = os.path.join(current_app.root_path, 'static', 'img', nombreCompleto)  # Construye la ruta donde se guardará la imagen

    imagen.save(ruta_img)  # Guarda la imagen en la ruta especificada
    predicted_label = predict(ruta_img)  # Realiza la predicción de la imagen

    porcentajeGato = predicted_label[0]  # Obtiene el porcentaje de predicción para la clase 'Gato'
    porcentajeLeon = predicted_label[1]  # Obtiene el porcentaje de predicción para la clase 'León'
    porcentajeTigre = predicted_label[3]  # Obtiene el porcentaje de predicción para la clase 'Tigre'
    porcentajePantera = predicted_label[2]  # Obtiene el porcentaje de predicción para la clase 'Pantera'

    id_usuario_fk = session['id_usuario'] #ID del usuario en la sesión de flask
    prediccion = Prediccion(id_usuario_fk, porcentajeGato, porcentajeLeon, porcentajeTigre, porcentajePantera, ruta_img)  # Instancia para el nuevo registro
    db.session.add(prediccion)     # Se guarda el registro 
    db.session.commit() # Se finaliza la sesión

    print('La imagen se predice como:', predicted_label)  # Imprime la etiqueta de predicción de la imagen

    imagen_ruta = url_for('static', filename='img/' + nombreCompleto)  # Genera la ruta a la imagen para mostrar en el resultado

    return render_template('resultado_prediccion.html', 
                        porcentajeGato=porcentajeGato,
                        porcentajeLeon=porcentajeLeon,
                        porcentajeTigre=porcentajeTigre,
                        porcentajePantera=porcentajePantera, 
                        image_path=imagen_ruta)  # Renderiza la plantilla 'resultado_prediccion.html' con los resultados de la predicción