from .extensions import db

#clases de prueba

class Salas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(50), unique=True)
    capacidad = db.Column(db.Integer)
