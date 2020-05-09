from flask import request

from models import *
from flask_restx import Resource

class UserPostController(Resource):
   # Metodo para crear usuario
   def post(self):
      data = request.get_json()
      if db.session.query(Users).filter_by(correo = data['correo']).count() < 1:
         new_user = Users(**data)
         new_user.hash_password()
         db.session.add(new_user)
         db.session.commit()
         return userSchema.dump(new_user)
      else:
             return{'message' : 'ya se tiene el correo registrado'}
   
