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