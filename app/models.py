from .extensions import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contrasena = db.Column(db.String(200))
    public_id = db.Column(db.String(200))
    google_id = db.Column(db.String(200))

class Salas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    capacidad = db.Column(db.Integer)

class Reservas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50))
    usuario = db.Column(db.String(50))
    sala = db.Column(db.String(50))
    inicio_fecha = db.Column(db.String(50))
    termino_fecha = db.Column(db.String(50))
