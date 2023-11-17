from flask import redirect, url_for
from flask_restx import Resource, Namespace
from .api_models import salas_model, salas_input_model, reservas_model, reservas_input_model, usuarios_model, usuarios_input_model
from .extensions import db
from .models import Salas
from .models import Salas, Reservas
from app.models import Usuarios
from .auth import login_required

ns = Namespace("api")

@ns.route("/")  # Nueva ruta para redirigir al index
class IndexResource(Resource):
    def get(self):
        # Puedes redirigir a la ruta que prefieras, en este caso, "index"
        return redirect(url_for("index"))

# Inicio endpoints de las salas

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

# Fin endpoints de las salas

# Inicio endpoints de las reservas

@ns.route("/reservas")  # Operación GET para obtener la lista de reservas y POST para crear una reserva
class ReservasResource(Resource):
    @ns.marshal_list_with(reservas_model)
    def get(self):
        reservas = Reservas.query.all()
        return reservas

    @ns.expect(reservas_input_model)
    @ns.marshal_with(reservas_model)
    def post(self):
        reserva = Reservas(
            token=ns.payload["token"],
            usuario=ns.payload["usuario"],
            sala=ns.payload["sala"],
            inicio_fecha=ns.payload["inicio_fecha"],
            termino_fecha=ns.payload["termino_fecha"]
        )
        db.session.add(reserva)
        db.session.commit()
        return reserva, 201

@ns.route("/reservas/<int:id>")  # Operación GET para obtener una reserva específica, PUT para actualizar y DELETE para eliminar
class ReservaResource(Resource):
    @ns.marshal_with(reservas_model)
    def get(self, id):
        reserva = Reservas.query.get_or_404(id)
        return reserva

    @ns.expect(reservas_input_model)
    @ns.marshal_with(reservas_model)
    def put(self, id):
        reserva = Reservas.query.get_or_404(id)
        reserva.token = ns.payload["token"]
        reserva.usuario = ns.payload["usuario"]
        reserva.sala = ns.payload["sala"]
        reserva.inicio_fecha = ns.payload["inicio_fecha"]
        reserva.termino_fecha = ns.payload["termino_fecha"]
        db.session.commit()
        return reserva

    def delete(self, id):
        reserva = Reservas.query.get_or_404(id)
        db.session.delete(reserva)
        db.session.commit()
        return "", 204

@ns.route("/reservas/<string:token>")  # Operación GET para obtener una reserva específica
class ReservaTokenResource(Resource):
    @ns.marshal_with(reservas_model)
    def get(self, token):
        reserva = Reservas.query.filter_by(token=token).first()
        return reserva
    
@ns.route("/reservas/busqueda")  # Operación GET para obtener la agenda de una sala y fecha dada
class ReservaBusquedaResource(Resource):
    @ns.marshal_list_with(reservas_model)
    def get(self):
        sala = ns.payload["sala"]
        fecha = ns.payload["fecha"]
        reservas = Reservas.query.filter_by(sala=sala, inicio_fecha=fecha).all()
        return reservas

# Fin endpoints de las reservas

# Inicio endpoints de los usuarios

@ns.route("/usuarios")  # Operación GET para obtener la lista de usuarios y POST para crear un usuario
class UsuariosResource(Resource):
    @ns.marshal_list_with(usuarios_model)
    def get(self):
        usuarios = Usuarios.query.all()
        return usuarios

    @ns.expect(usuarios_input_model)
    @ns.marshal_with(usuarios_model)
    def post(self):
        usuario = Usuarios(
            nombre=ns.payload["nombre"],
            apellido=ns.payload["apellido"],
            correo=ns.payload["correo"],
            contrasena=ns.payload["contrasena"],
            rol=ns.payload["rol"]
        )
        db.session.add(usuario)
        db.session.commit()
        return usuario, 201

@ns.route("/usuarios/<int:id>")  # Operación GET para obtener un usuario específico, PUT para actualizar y DELETE para eliminar
class UsuarioResource(Resource):
    @ns.marshal_with(usuarios_model)
    def get(self, id):
        usuario = Usuarios.query.get_or_404(id)
        return usuario

    @ns.expect(usuarios_input_model)
    @ns.marshal_with(usuarios_model)
    def put(self, id):
        usuario = Usuarios.query.get_or_404(id)
        usuario.nombre = ns.payload["nombre"]
        usuario.apellido = ns.payload["apellido"]
        usuario.correo = ns.payload["correo"]
        usuario.contrasena = ns.payload["contrasena"]
        usuario.rol = ns.payload["rol"]
        db.session.commit()
        return usuario

    def delete(self, id):
        usuario = Usuarios.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return "", 204

# Fin endpoints de los usuarios