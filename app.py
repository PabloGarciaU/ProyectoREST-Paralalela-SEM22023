from flask import Flask, jsonify, request

app = Flask(__name__)

# Importar datos de info.py

from info import salas
from info import reservas
from info import usuarios


#Metodos de testing

@app.route('/ping') # Testea ping paer si esta conectado
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/salas/listadesalas', methods=['GET']) # Obtener lista de salas
def getSalas():
    return jsonify({"salas": salas})

@app.route('/reservas/listadereservas', methods=['GET']) # Obtener lista de reservas
def getReservas():
    return jsonify({"reservas": reservas})

@app.route('/usuarios/listadeusuarios', methods=['GET']) # Obtener lista de usuarios
def getUsuarios():
    return jsonify({"usuarios": usuarios})

#Metodos requeridos por la API "Salas"

@app.route('/salas/obtenersala/<int:id>', methods=['GET']) # Obtener sala por su codigo (id)
def getSala(id):
    for sala in salas:
        if sala["id"] == id:
            return jsonify({"sala": sala})
    return jsonify({"message": "Sala no encontrada"})

@app.route('/salas/listadesalasexistentes', methods=['GET']) # Obtener lista de salas existentes
def getSalasExistentes():
    salasExistentes = []
    for sala in salas:
        salasExistentes.append(sala["id"])
    return jsonify({"salas": salasExistentes})

#Metodos requeridos por la API "Reservas"

@app.route('/reservas/crearreserva', methods=['POST']) # Crea reserva, el tema del usuario se vee despues
def createReserva():
    new_reserva = {
        "id": request.json["id"],
        "name": request.json["name"],
        "date": request.json["date"],
        "time": request.json["time"],
        "sala": request.json["sala"],
        "user": request.json["user"]
    }
    reservas.append(new_reserva)
    return jsonify({"message": "Reserva creada exitosamente", "reservas": reservas})

@app.route('/reservas/buscarreserva', methods=['POST']) # Busca reserva por id """
def getReserva():
    reservaFound = [reserva for reserva in reservas if reserva["id"] == request.json["id"]]
    if (len(reservaFound) > 0):
        return jsonify({"reserva": reservaFound[0]})
    return jsonify({"message": "Reserva no encontrada"})

@app.route('/reservas/agendareservas', methods=['GET']) # Obtiene agenda para un codigo de sala y fecha
def getAgenda():
    agendaFound = [reserva for reserva in reservas if reserva["sala"] == request.json["sala"] and reserva["date"] == request.json["date"]]
    if (len(agendaFound) > 0):
        return jsonify({"agenda": agendaFound}) 
    return jsonify({"message": "Agenda no encontrada"})

# Pa que funcione

if __name__ == '__main__':
    app.run(debug=True, port = 4000)