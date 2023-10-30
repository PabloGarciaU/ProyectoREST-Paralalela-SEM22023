"""Los endpoints del proyecto"""
import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

from validate_email import validate_email
REQUEST_API = Blueprint('request_api', __name__)

def get_blueprint():
    """Devuelve la api al modulo principal"""
    return REQUEST_API

