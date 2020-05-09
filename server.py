from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Configuración Inicial Flask
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "12usuario12"
app.config['JWT_ALGORITHM'] = "HS256"

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(
        app,
        title='Usuarios corporativos',
        version='2.0',
        description='Creando servicio a usuarios corporativos',
    )

from utils.environment import Environment
config = Environment().settingsGeneral()
