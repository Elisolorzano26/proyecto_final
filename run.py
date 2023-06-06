from app import db, agregar_rutas

app = agregar_rutas()

with app.app_context():  # Crea un contexto de aplicación para ejecutar comandos dentro de la aplicación
    db.create_all()  # Crea todas las tablas en la base de datos según los modelos definidos

if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración (debug) si se ejecuta directamente como script principal