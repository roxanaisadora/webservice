import datetime
from flask import request
from flask_jwt_extended import create_access_token


from models import *
from flask_restx import Resource
from flask_bcrypt import check_password_hash,Bcrypt
bcrypt = Bcrypt()
class LoginController(Resource):

    def post(self):
        # Obtener data de BODY
        data = request.get_json()
        email = data["correo"]
        password = data["password"]

        found_user = Users.query.filter_by(correo = email).first()
        print('el correo entro')
        if found_user and bcrypt.check_password_hash(found_user.password, password):
            authorized = True
            # Generamos el Token
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(1), expires_delta=expires)
            return {'token': access_token,
                    'loggin':'se ha logiado exitosamente'
                    }, 200
        else:
            return{'error': 'La contraseña o el correo es invalido'}, 401
  
       
        
