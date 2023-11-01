"""A Python Flask REST API BoilerPlate (CRUD) Style"""

import argparse
import os
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes import request_api

APP = Flask(__name__)

### Configuracioon swagger ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API-PARAPELA-PROYECTOREST-2SEM2023"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

APP.register_blueprint(request_api.get_blueprint())

# Respuesta de errores de la api

@APP.errorhandler(400)
def handle_400_error(_error):
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@APP.errorhandler(401)
def handle_401_error(_error):

    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@APP.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@APP.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description="Proyectorestparalela")

    PARSER.add_argument('--debug', action='store_true',
                        help="Usando flask")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Ejecutando la api en modo debug/dev mod")
        CORS = CORS(APP)
        APP.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        APP.run(host='0.0.0.0', port=PORT, debug=False)
