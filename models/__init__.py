# Librerías para SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Módulos propios
from server import app
from database.connection import DBConnection
# Instanciar la clase DBConnection
dbConnection = DBConnection()

app.config['SQLALCHEMY_DATABASE_URI'] = dbConnection.run("MYSQL")
app.config['SQLALCHEMY_BINDS'] = {
    'appmeta':      dbConnection.run("SQLLITE")
}

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = dbConnection.TRACK_MODIFICATIONS
app.config["SQLALCHEMY_ECHO"] = dbConnection.ECHO

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Importar Modelos, cada modelo viene hacer una tabla
from models.modelUsuario import *
from models.userModel import *

db.create_all()

