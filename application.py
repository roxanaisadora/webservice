
#Módulos creados
#from server import *
#from models import *
#from controllers.controllerUsuario import UsuarioController, UsuarioPostController, EstadoController, UsuarioNombreController, UsuarioMostraidController, UsuarioMostrarestadoController
#from controllers.userController import UserPostController
#from controllers.loginController import LoginController

#usuario = api.namespace('api', description='Usuario API')
#usuario.add_resource(UsuarioPostController, '/usuario')
#usuario.add_resource(UsuarioController, '/usuario/<int:id>')
#usuario.add_resource(EstadoController, '/usuario/estado/<int:id>')
#usuario.add_resource(UsuarioMostrarestadoController, '/usuario/estado')
#usuario.add_resource(UsuarioNombreController, '/usuario/busqueda')
#usuario.add_resource(UsuarioMostraidController, '/usuario/iddata/<int:id>')

#user = api.namespace('api', description='User API')
#user.add_resource(UserPostController, '/user')

#login = api.namespace('api', description='Login API')
#login.add_resource(LoginController, '/login')
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
  	app.run()
   
#cambios realizados para demostracion el app service
