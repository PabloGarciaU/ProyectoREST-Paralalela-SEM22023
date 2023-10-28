from flask import Flask, jsonify

app = Flask(__name__)

from products import products
from salas import salas
from reservas import reservas

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Metodos de de las salas

@app.route('/salas/code', methods=['GET']) 

@app.route('/salas', methods=['GET']) 

# Metodos de las reservas

@app.route('/reservas/request', methods=['POST']) 

@app.route('/reservas/search', methods=['POST']) 

@app.route('/reservas/code/date', methods=['GET'])