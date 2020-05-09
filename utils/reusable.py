from datetime import datetime 
from flask import request

class Reusable():
    def fechadecambio(self, data):
        data = request.get_json()
        fecha = data['fnacimiento']
        fecha1 = datetime.strptime(fecha, '%Y-%m-%d').date()
        return fecha1
    
