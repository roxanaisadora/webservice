from utils.environment import Environment

# Se genera la clase DBConnection para la proteccion de la base de datos a usar
class DBConnection(Environment):
    def __init__(self):
        # Variables de Entorno de la conexión a la BD
        self.__HOST     = ""
        self.__USER     = ""
        self.__PWD      = ""
        self.__PORT     = ""
        self.__DATABASE = ""

        # Variables de Entorno de configuración SQLAlchemy
        sqlAlchemy = self.settingsSQLAlchemy()
        self.TRACK_MODIFICATIONS = sqlAlchemy["TRACK_MODIFICATIONS"]
        self.ECHO = sqlAlchemy["ECHO"]

    def initParameters(self, nameBD):
        # Variables de Entorno de la conexión a la BD
        db = self.settingBD(nameBD)
        self.__HOST     = db.get("HOST")
        self.__USER     = db.get("USER")
        self.__PWD      = db.get("PWD")
        self.__PORT     = db.get("PORT")
        self.__DATABASE = db.get("DATABASE")

    def run(self, nameBD):
        # Se declara el tipo de base de datos a usar 
        self.initParameters(nameBD)

        dbConnection = {
            "SQLLITE"   : self.__sqlLite(),
            "MYSQL"     : self.__mysql(),
        }
        return dbConnection[nameBD]

    def __sqlLite(self):
        return "sqlite:///test.db"

    def __mysql(self):
        return f"mysql+mysqlconnector://{self.__USER}:{self.__PWD}@{self.__HOST}:{self.__PORT}/{self.__DATABASE}"

