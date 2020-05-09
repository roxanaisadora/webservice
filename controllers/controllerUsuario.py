from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


# Módulos propios
from models import *
from controllers.loginController import LoginController
from utils.reusable import Reusable
reusable = Reusable()
Logincontroller = LoginController()

class UsuarioController(Resource):
    @jwt_required
    def get(self, id):
        current_user = get_jwt_identity()
        usuario = Usuario.query.get_or_404(id)
        return usuarioSchema.dump(usuario)
    
    # Metodo para actualizar usuario 

    def put(self, id):
        data = request.get_json()
        celular = data['celular']
        celular2 = str(celular)
        
        print(type(celular))
        usuario = Usuario.query.filter_by(id=id).first()
        
        #error en el enlace
        if usuario is None:
            return {'message': 'el enlace es invalido'} ,404
        
        if type(celular) != str:
            if int(celular2[0]) == 9:
                if 99999999 <= celular <= 999999999:
                    #enlace valido
                    if "fnacimiento" in data: usuario.fnacimiento = reusable.fechadecambio(data)
                    if "celular" in data: usuario.celular = data["celular"]
                    if "nombre" in data: usuario.nombre = data["nombre"]
                    if "apellidos" in data: usuario.apellidos = data["apellidos"]
                    if "foto" in data: usuario.foto = data["foto"]
                    if "estado" in data: usuario.estado = data["estado"]
                    db.session.commit()

                    usuario = Usuario.query.filter_by(id=id).first()
                    return "se actualizo usuario"
                else:
                    return{'message':'el numero debe ser de 9 digitos'} 
            else:
                return{'message':'el numero ingresado debe comenzar con 9'}
        else:
                return{'message':'el campo ingresado es incorrecto'}


class UsuarioPostController(Resource):
  # metodo para traer los datos generados en la tabla de usuarios

    def get(self):
        usuario = Usuario.query.all()
        return usuarioSchema.dump(usuario)

    # metodo para el metodo crear medio del postman
    
    def post(self):
        data = request.get_json()
        celular = data['celular']
        celular2 = str(celular)
        if type(celular) != str:
            if int(celular2[0]) == 9:
                if 99999999 <= celular <= 999999999:
                    new_usuario = Usuario(
                    fnacimiento=reusable.fechadecambio(data),
                    celular=data['celular'],
                    nombre=data['nombre'],
                    apellidos=data['apellidos']
                    )
                    db.session.add(new_usuario)
                    db.session.commit()
                    return "se creo un nuevo nuevo usuario"
                else:
                    return{'message':'el numero debe ser de 9 digitos'} 
            else:
                return{'message':'el numero ingresado debe comenzar con 9'}
        else:
                return{'message':'el campo ingresado es incorrecto'}
        
class EstadoController(Resource):
    # Metodo para realizar el cambio de ESTADOS

    def put(self, id):
        data = request.get_json()
        usuario = Usuario.query.filter_by(id = id).first()
        #error en el enlace
        if usuario is None:
            return {'message': 'el enlace es invalido'} ,404
      
        #enlace valido
        if "estado" in data: usuario.estado = data["estado"]
        db.session.commit()
        usuario = Usuario.query.filter_by(id=id).first()
        return "se cambio su estado a " + data["estado"], 200


class UsuarioNombreController(Resource):
      # Metodo para traer el dato del usuario por nombre

    def get(self):
        data = request.get_json()
        nombre1=data['nombre']
        usuario = db.session.query(Usuario).filter(Usuario.nombre.like(nombre1+'%')).all()
        usuario2 = usuarioSchema.dump(usuario)
        
        if len(usuario2) == 0:
            print(usuario2)
            return {'message': 'No se tiene ningun usuario registrado'}
        else:
            return usuario2


class UsuarioMostraidController(Resource):  
    # Metodo para mostrar los datos el usuario personal

    def get(self, id):
        data = request.get_json()
        usuario = Usuario.query.filter_by(id = id).first()
        #error en el enlace
        if usuario is None:
            return {'message': 'el enlace es invalido'} ,404
        
        #enlace valido
        usuario = Usuario.query.filter_by(id = id).all()
        return usuarioSchema.dump(usuario)

class UsuarioMostrarestadoController(Resource):    
    # Metodo para mostrar los datos el usuario personal

    def get(self):
        data = request.get_json()
        estado1=data['estado']
        
        usuario = Usuario.query.filter_by(estado = estado1).all()
        return usuarioSchema.dump(usuario)