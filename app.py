from flask import Flask  # Importa la clase Flask del módulo flask
from flask_sqlalchemy import SQLAlchemy  # Importa la clase SQLAlchemy del módulo flask_sqlalchemy
from config import urlConexion, claveSecreta  # Importa las variables urlConexion y claveSecreta del archivo config.py
from routes.rutas_usuarios import rutasUsuario  # Importa el blueprint rutas_usuario del módulo routes.rutas_usuarios
from routes.rutas_prediccion import rutasPrediccion  # Importa el blueprint rutas_prediccion del módulo routes.rutas_prediccion

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

app.secret_key = claveSecreta  # Establece la clave secreta de la aplicación para las sesiones

app.config['SQLALCHEMY_DATABASE_URI'] = urlConexion  # Configura la URI de la base de datos en la aplicación
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva el seguimiento de modificaciones en la base de datos

db = SQLAlchemy(app)  # Crea una instancia de la base de datos SQLAlchemy asociada a la aplicación

app.register_blueprint(rutasUsuario)  # Registra el blueprint rutas_usuario en la aplicación
app.register_blueprint(rutasPrediccion)  # Registra el blueprint rutas_prediccion en la aplicación

with app.app_context():  # Crea un contexto de aplicación para ejecutar comandos dentro de la aplicación
    db.create_all()  # Crea todas las tablas en la base de datos según los modelos definidos

if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración (debug) si se ejecuta directamente como script principal