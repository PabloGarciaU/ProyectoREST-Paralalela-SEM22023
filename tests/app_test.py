"""Para ejecutar las pruebas, usar sete comando:,
$ nosetests --verbose
"""

from nose.tools import assert_true
import requests

# BASE_URL = "http://127.0.0.1"
BASE_URL = "http://localhost:5000"
# BASE_URL = "https://python3-flask-uat.herokuapp.com/"


class NewUUID():  
    def __init__(self, value):
        self.value = value
