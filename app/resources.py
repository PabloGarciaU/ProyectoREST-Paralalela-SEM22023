from flask_restx import Resource, Namespace
from .api_models import salas_model, salas_input_model
from .extensions import db
from .models import Salas

ns = Namespace("api")

@ns.route("/salas")  # Operación GET para obtener la lista de salas y POST para crear una sala
class SalasResource(Resource):
    @ns.marshal_list_with(salas_model)
    def get(self):
        salas = Salas.query.all()
        return salas

    @ns.expect(salas_input_model)
    @ns.marshal_with(salas_model)
    def post(self):
        sala = Salas(
            codigo=ns.payload["codigo"],
            nombre=ns.payload["nombre"],
            capacidad=ns.payload["capacidad"]
        )
        db.session.add(sala)
        db.session.commit()
        return sala, 201

@ns.route("/salas/<int:id>")  # Operación GET para obtener una sala específica, PUT para actualizar y DELETE para eliminar
class SalaResource(Resource):
    @ns.marshal_with(salas_model)
    def get(self, id):
        sala = Salas.query.get_or_404(id)
        return sala

    @ns.expect(salas_input_model)
    @ns.marshal_with(salas_model)
    def put(self, id):
        sala = Salas.query.get_or_404(id)
        sala.codigo = ns.payload["codigo"]
        sala.nombre = ns.payload["nombre"]
        sala.capacidad = ns.payload["capacidad"]
        db.session.commit()
        return sala

    def delete(self, id):
        sala = Salas.query.get_or_404(id)
        db.session.delete(sala)
        db.session.commit()
        return "", 204
