from .extensions import db

#clases de prueba

class Salas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(50), unique=True)
    capacidad = db.Column(db.Integer, unique=True)

class Reservas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), unique=True)
    usuario = db.Column(db.String(50), unique=True)
    sala = db.Column(db.String(50), unique=True)
    inicio_fecha = db.Column(db.String(50), unique=True)
    termino_fecha = db.Column(db.String(50), unique=True)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    apellido = db.Column(db.String(50), unique=True)
    correo = db.Column(db.String(50), unique=True)
    contrasena = db.Column(db.String(50), unique=True)
    rol = db.Column(db.String(50), unique=True)
