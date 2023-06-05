from app import db  # Importa el objeto 'db' desde el módulo 'main'

class Prediccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Define una columna 'id' como entero y clave primaria
    id_usuario_fk = db.Column(db.Integer, db.ForeignKey('usuario.id'))  # Define una columna 'id_usuario_fk' como entero y clave foránea que referencia a la columna 'id' de la tabla 'usuario'
    porcentajeGato = db.Column(db.String(20))  # Define una columna 'porcentajeGato' como una cadena de máximo 20 caracteres
    porcentajeLeon = db.Column(db.String(20))  # Define una columna 'porcentajeLeon' como una cadena de máximo 20 caracteres
    porcentajeTigre = db.Column(db.String(20))  # Define una columna 'porcentajeTigre' como una cadena de máximo 20 caracteres
    porcentajePantera = db.Column(db.String(20))  # Define una columna 'porcentajePantera' como una cadena de máximo 20 caracteres
    imagen = db.Column(db.String(500))  # Define una columna 'imagen' como una cadena de máximo 500 caracteres

    def _init_(self, id_usuario_fk, porcentajeGato, porcentajeLeon, porcentajeTigre, porcentajePantera, imagen):
        self.id_usuario_fk = id_usuario_fk  # Inicializa el atributo 'id_usuario_fk' con el valor recibido como parámetro
        self.porcentajeGato = porcentajeGato  # Inicializa el atributo 'porcentajeGato' con el valor recibido como parámetro
        self.porcentajeLeon = porcentajeLeon  # Inicializa el atributo 'porcentajeLeon' con el valor recibido como parámetro
        self.porcentajeTigre = porcentajeTigre  # Inicializa el atributo 'porcentajeTigre' con el valor recibido como parámetro
        self.porcentajePantera = porcentajePantera  # Inicializa el atributo 'porcentajePantera' con el valor recibido como parámetro
        self.imagen = imagen  # Inicializa el atributo 'imagen' con el valor recibido como parámetro