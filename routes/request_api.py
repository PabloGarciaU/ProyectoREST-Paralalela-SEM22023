"""Los endpoints del proyecto"""
import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

from validate_email import validate_email
REQUEST_API = Blueprint('request_api', __name__)

# Informacion de prueba para los endpoints

salas = [
    {"id": 1, "name": "Sala 1", "capacity": 10},
    {"id": 2, "name": "Sala 2", "capacity": 20},
    {"id": 3, "name": "Sala 3", "capacity": 30},
    {"id": 4, "name": "Sala 4", "capacity": 40},
    {"id": 5, "name": "Sala 5", "capacity": 50},
    {"id": 6, "name": "Sala 6", "capacity": 60},
    {"id": 7, "name": "Sala 7", "capacity": 70},
    {"id": 8, "name": "Sala 8", "capacity": 80},
    {"id": 9, "name": "Sala 9", "capacity": 90},
    {"id": 10, "name": "Sala 10", "capacity": 100},
]

reservas = [
    {"id": 1, "name": "Reserva 1", "date": "2021-10-10", "time": "10:00", "sala": 1, "user": "user1"},
    {"id": 2, "name": "Reserva 2", "date": "2021-10-10", "time": "10:00", "sala": 2, "user": "user2"},
]

usuarios = [
    {"id": 1, "name": "user1", "password": "1234"},
    {"id": 2, "name": "user2", "password": "1234"},
    {"id": 3, "name": "user3", "password": "1234"},
    {"id": 4, "name": "user4", "password": "1234"},
    {"id": 5, "name": "user5", "password": "1234"},
]

# Un apuntador para que app.py pueda acceder a la api

def get_blueprint():
    """Devuelve la api al modulo principal"""
    return REQUEST_API

# endpoint de prueba

@REQUEST_API.route('/ping', methods=['GET'])
def ping():
    """Endpoint de prueba"""
    return jsonify({'response': 'pong!'})

# endpoints de salas

@REQUEST_API.route('/salas/<string:id>', methods=['GET']) # Una operación GET que permite obtener los datos de la sala usando su código
def obtener_sala_por_codigo(codigo):
    """Obtiene una sala por su código."""
    sala = next((sala for sala in salas if sala['name'] == codigo), None)
    if sala is None:
        return jsonify({'mensaje': 'Sala no encontrada'}), 404
    return jsonify(sala)

@REQUEST_API.route('/salas', methods=['GET']) # Una operación GET que permite obtener los datos de todas las salas
def obtener_salas():
    """Obtiene todas las salas."""
    return jsonify(salas)

# endpoints de reservas

@REQUEST_API.route('/reservas/crearreserva', methods=['POST']) # Metodo para crear reserva
def crear_reserva():
    """Crea una nueva reserva."""
    data = request.json
    nueva_reserva = {
        "id": len(reservas) + 1,  # Asigna un nuevo ID
        "name": data.get("name"),
        "date": data.get("date"),
        "time": data.get("time"),
        "sala": data.get("sala"),
        "user": data.get("user")
    }
    reservas.append(nueva_reserva)
    return jsonify(nueva_reserva), 201

@REQUEST_API.route('/reservas/buscarreserva', methods=['POST']) # Metodo para buscar una reserva, segun el nombre de usuario
def buscar_reserva():
    """Busca una reserva por nombre de usuario."""
    data = request.json

    usuario = data.get("usuario")

    if usuario is None:
        return jsonify({'mensaje': 'Se requiere el nombre de usuario para realizar la búsqueda'}), 400

    resultados = []

    for reserva in reservas:
        if reserva.get("user") == usuario:
            resultados.append(reserva)

    if not resultados:
        return jsonify({'mensaje': 'No se encontraron reservas asociadas a ese usuario'}), 404

    return jsonify(resultados), 200

@REQUEST_API.route('/reservas/agenda', methods=['GET'])
def agenda_reserva():
    """Obtiene la agenda de reservas de una sala y fecha específica."""
    sala = request.args.get("sala")
    fecha = request.args.get("fecha")

    if sala is None or fecha is None:
        return jsonify({'mensaje': 'Se requiere el código de sala y la fecha para obtener la agenda'}), 400

    agenda = []

    for reserva in reservas:
        if reserva.get("sala") == int(sala) and reserva.get("date") == fecha:
            agenda.append(reserva)

    if not agenda:
        return jsonify({'mensaje': 'No hay reservas en la sala para la fecha especificada'}), 404

    return jsonify(agenda), 200