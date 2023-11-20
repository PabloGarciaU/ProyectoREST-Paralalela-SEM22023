from flask_restx import fields

from .extensions import api

# modelos de la api salas

salas_model = api.model("Salas", {
    "codigo": fields.String,
    "nombre": fields.String,
    "capacidad": fields.Integer,
})

salas_input_model = api.model("SalasInput", {
    "codigo": fields.String(required=True),
    "nombre": fields.String(required=True),
    "capacidad": fields.Integer(required=True),
})

reservas_model = api.model("Reservas", {
    "token": fields.String,
    "usuario": fields.String,
    "sala": fields.String,
    "inicio_fecha": fields.String,
    "termino_fecha": fields.String,
})

reservas_input_model = api.model("ReservasInput", {
    "token": fields.String(required=True),
    "usuario": fields.String(required=True),
    "sala": fields.String(required=True),
    "inicio_fecha": fields.String(required=True),
    "termino_fecha": fields.String(required=True),
})

usuarios_model = api.model("Usuarios", {
    "nombre": fields.String,
    "correo": fields.String,
    "contrasena": fields.String,
    "public_id": fields.String,
    "google_id": fields.String,

})

usuarios_input_model = api.model("UsuariosInput", {
    "nombre": fields.String(required=True),
    "correo": fields.String(required=True),
    "contrasena": fields.String(required=True),
    "public_id": fields.String(required=True),
    "google_id": fields.String(required=True),
})