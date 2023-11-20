from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api(title='API-PROYECTOREST-PARALELA-SEM22023 PROF. Sebastian Salazar', version='1.0', description='Integrantes: Pablo Garcia Urzua - Victor Toledo Cerna - Fabian Rojas Gamboa',license='PRESIONA AQUI PARA OBTENER TOKEN JWT (Google Oauth 2.0)',license_url='/login')
db = SQLAlchemy()