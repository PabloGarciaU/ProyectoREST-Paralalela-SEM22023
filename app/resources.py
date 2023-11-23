from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity
from .api_models import salas_model, salas_input_model, reservas_model, reservas_input_model, usuarios_model, usuarios_input_model
from .extensions import db
from .models import Salas, Reservas, Usuarios

# Configuración de la autorización con JWT de google con la API

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
    }
}

# Configuración del espacio de nombres (namespace) de la API

ns = Namespace("api", authorizations=authorizations)

# Inicio endpoints de las salas

@ns.route("/salas")  # Operación GET para obtener la lista de salas y POST para crear una sala
class SalasResource(Resource):
    @ns.marshal_list_with(salas_model)
    def get(self):
        salas = Salas.query.all()
        return salas

    '''@ns.expect(salas_input_model)
    @ns.marshal_with(salas_model)
    def post(self):
        sala = Salas(
            codigo=ns.payload["codigo"],
            nombre=ns.payload["nombre"],
            capacidad=ns.payload["capacidad"]
        )
        db.session.add(sala)
        db.session.commit()
        return sala, 201'''

@ns.route("/salas/<string:codigo>")  # Operación GET para obtener una sala específica, PUT para actualizar y DELETE para eliminar
class SalaResource(Resource):
    @ns.marshal_with(salas_model)
    def get(self, codigo):
        sala = Salas.query.filter_by(codigo=codigo).first()
        if not sala:
            return {"message": "Sala no encontrada"}, 404
        return sala

    '''@ns.expect(salas_input_model)
    @ns.marshal_with(salas_model)
    def put(self, id):
        sala = Salas.query.get_or_404(id)
        sala.codigo = ns.payload["codigo"]
        sala.nombre = ns.payload["nombre"]
        sala.capacidad = ns.payload["capacidad"]
        db.session.commit()
        return sala'''

    '''def delete(self, id):
        sala = Salas.query.get_or_404(id)
        db.session.delete(sala)
        db.session.commit()
        return "", 204'''

# Fin endpoints de las salas

# Inicio endpoints de las reservas

'''@ns.route("/reservas")  # Operación GET para obtener la lista de reservas y POST para crear una reserva
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
        return reserva, 201'''

'''@ns.route("/reservas/<int:id>")  # Operación GET para obtener una reserva específica, PUT para actualizar y DELETE para eliminar
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
        return "", 204'''

@ns.route("/reservas/pedirreserva")
class ReservaPedirResource(Resource):
    method_decorators = [jwt_required()]
    @ns.doc(security="jsonWebToken")
    @ns.expect(reservas_input_model)
    @ns.marshal_with(reservas_model)
    def post(self):
        # Obtener el correo del usuario desde el token JWT
        usuario_email = get_jwt_identity()

        # Verificar si el correo del usuario está en la base de datos
        usuario_existente = Usuarios.query.filter_by(correo=usuario_email).first()

        if not usuario_existente:
            # Si el usuario no está en la base de datos, retornar un error
            ns.abort(403, message="No tienes permisos para realizar esta acción")

        # El usuario está en la base de datos, continuar con la creación de la reserva
        reserva = Reservas(
            token=ns.payload["token"],
            usuario=usuario_email,
            sala=ns.payload["sala"],
            inicio_fecha=ns.payload["inicio_fecha"],
            termino_fecha=ns.payload["termino_fecha"]
        )

        db.session.add(reserva)
        db.session.commit()

        return reserva, 201

@ns.route("/reservas/busqueda") # Operacion POST, Usando un método POST y un conjunto de atributos, se puede consultar las reservas en función de los parámetros dados
class ReservaBusquedaResource(Resource):
    @ns.expect(reservas_input_model)
    @ns.marshal_with(reservas_model)
    def post(self):
        reservas = Reservas.query.filter_by(**ns.payload).all()
        if not reservas:
            ns.abort(404, message="No se encontraron reservas para los parámetros proporcionados")
        return reservas

@ns.route("/reservas/<string:sala>/agenda/<string:inicio_fecha>") # Operacion GET, donde a través de un solicitud GET, se debe obtener la agenda para un código de sala y fecha dada.
class ReservaAgendarResource(Resource):
    @ns.marshal_with(reservas_model)
    def get(self, sala, inicio_fecha):
        reservas = Reservas.query.filter_by(sala=sala).filter_by(inicio_fecha=inicio_fecha).all()
        if not reservas:
            ns.abort(404, message="No se encontraron reservas para la sala y fecha proporcionadas")
        return reservas

# Fin endpoints de las reservas

# Inicio endpoints de los usuarios

'''@ns.route("/usuarios")  # Operación GET para obtener la lista de usuarios y POST para crear un usuario
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
            correo=ns.payload["correo"],
            contrasena=ns.payload["contrasena"],
            public_id=ns.payload["public_id"],
            google_id=ns.payload["google_id"]
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
        usuario.correo = ns.payload["correo"]
        usuario.contrasena = ns.payload["contrasena"]
        usuario.public_id = ns.payload["public_id"]
        usuario.google_id = ns.payload["google_id"]
        db.session.commit()
        return usuario

    def delete(self, id):
        usuario = Usuarios.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return "", 204

# Fin endpoints de los usuarios'''