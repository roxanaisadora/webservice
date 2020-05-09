from . import db, ma

# Se crear el modelo de columnas para el registro del usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fnacimiento = db.Column(db.Date,unique=False, nullable=False)
    celular = db.Column(db.Integer,unique=False, nullable=False)
    nombre = db.Column(db.String(100),unique=False, nullable=False)
    apellidos = db.Column(db.String(100),unique=False, nullable=False)
    foto = db.Column(db.String(1000),unique=False, nullable=True)
    estado = db.Column(db.String(100),unique=False, nullable=True)


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("idusuario", "correo","pws","fnacimiento","celular","nombre","apellidos","foto","estado")

usuarioSchema = UsuarioSchema()
usuarioSchema = UsuarioSchema(many=True)
