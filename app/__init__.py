from flask import Flask
from .extensions import api, db, jwt
from .resources import ns
from datetime import timedelta  

def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)

    # Configuración de la clave secreta para sesiones
    app.secret_key = 'supersecretkey'
    
    # Configuración del nombre de la cookie de sesión
    app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
    
    # Configuración de la duración de las sesiones
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=1)

    # Configuración de la clave secreta de la aplicación
    app.config['SECRET_KEY'] = 'supersecret'
    
    # Configuración de la URI de la base de datos SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Inicialización de la extensión API (Flask-RESTx) en la aplicación
    api.init_app(app)
    
    # Inicialización de la extensión SQLAlchemy en la aplicación
    db.init_app(app)

    # Inicialización de la extensión JWT en la aplicación
    jwt.init_app(app)

    # Agregar un espacio de nombres (namespace) a la API
    api.add_namespace(ns)

    # Devuelve la instancia configurada de la aplicación Flask
    return app