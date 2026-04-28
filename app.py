"""
Punto de entrada principal de la aplicación.

Inicializa el servidor Flask y registra los Blueprints (rutas)
para seguir la arquitectura MVC.
"""

from flask import Flask
from routes.calculadora_routes import calculadora_bp

# Instanciación de la aplicación Flask
app = Flask(__name__)

# Registro del módulo de rutas de la calculadora
app.register_blueprint(calculadora_bp)

if __name__ == "__main__":
    # Inicia el servidor de desarrollo en modo debug
    app.run(debug=True)