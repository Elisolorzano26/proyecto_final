from flask import Blueprint, render_template  # Importa la clase Blueprint y la función render_template del módulo flask
from controllers.predicciones_controller import procesar_imagen  # Importa la función procesar_imagen del controlador predicciones_controller
from controllers.predicciones_controller import historial_predicciones  # Importa la función historial_predicciones del controlador predicciones_controller

rutasPrediccion = Blueprint('prediccion', __name__)  # Crea una instancia de la clase Blueprint con el nombre 'prediccion'

@rutasPrediccion.route('/prediccion_felinos')  # Define una ruta '/prediccion_felinos' para el punto de acceso vista_predecir()
def vista_predecir():
    return render_template('prediccion.html')  # Renderiza la plantilla 'prediccion.html'

@rutasPrediccion.route('/nueva_prediccion', methods=['POST'])  # Define una ruta '/nueva_prediccion' para el punto de acceso nueva_prediccion()
def nueva_prediccion():
    return procesar_imagen()  # Llama a la función procesar_imagen() del controlador para procesar la imagen

@rutasPrediccion.route('/historial_predicciones')  # Define una ruta '/historial_predicciones' para el punto de acceso datos_predicciones()
def datos_predicciones():
    return historial_predicciones()  # Llama a la función historial_predicciones() del controlador para obtener el historial de predicciones