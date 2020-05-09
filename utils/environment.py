import os
from distutils.util import strtobool
import os.path

if os.path.isfile('env.py'):
    print ("Como existe importar archivo de ambiente de desarrollo")
    import env

class Environment():
    
    def settingsGeneral(self):
        return{
            'PORT': int(os.environ["PORTAPI"]),
            'DEBUG': strtobool(os.environ['DEBUG'])
        }

    def settingsSQLAlchemy(self):
        return{
            'TRACK_MODIFICATIONS': strtobool(os.environ["TRACK_MODIFICATIONS"]),
            'ECHO': strtobool(os.environ['ECHO'])
        }

    def settingBD(self, nameBD):
        if nameBD.upper() == "MYSQL": return self.__settingsMYSQL()
        if nameBD.upper() == "SQLLITE": return self.__settingsSQLLITE()

    def __settingsSQLLITE(self):
        return {
            'PATH': os.environ["SQLLITE_PATH"],
        }

    def __settingsMYSQL(self):
        return{
            'HOST': os.environ["MYSQL_HOST"],
            'DATABASE': os.environ["MYSQL_DATABASE"],
            'PORT': int(os.environ["MYSQL_PORT"]),
            'USER': os.environ["MYSQL_USER"],
            'PWD': os.environ["MYSQL_PASSWORD"],

        }
        



