from app import db  # Importa el objeto 'db' desde el módulo 'app'

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Define una columna 'id' como entero y clave primaria
    nombreCompleto = db.Column(db.String(50))  # Define una columna 'nombreCompleto' como una cadena de máximo 50 caracteres
    telefono = db.Column(db.String(30))  # Define una columna 'telefono' como una cadena de máximo 30 caracteres
    correo = db.Column(db.String(30), unique=True)  # Define una columna 'correo' como una cadena de máximo 30 caracteres y única (no repetida)
    password = db.Column(db.String(50))  # Define una columna 'password' como una cadena de máximo 50 caracteres

    def _init_(self, nombreCompleto, telefono, correo, password):
        self.nombreCompleto = nombreCompleto  # Inicializa el atributo 'nombreCompleto' con el valor recibido como parámetro
        self.telefono = telefono  # Inicializa el atributo 'telefono' con el valor recibido como parámetro
        self.correo = correo  # Inicializa el atributo 'correo' con el valor recibido como parámetro
        self.password = password  # Inicializa el atributo 'password' con el valor recibido como parámetro

    def comparar_contraseña(self, password):
        return self.password == password # Validamos si ambas contraseñas coinciden
