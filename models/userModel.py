from . import db, ma
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

class Users(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    correo       = db.Column(db.String(200), unique=True, nullable=False)
    password    = db.Column(db.String(200), nullable=False)
    activo      = db.Column(db.Boolean, unique=False, nullable=False, default=1)

    def hash_password(self):
        self.password = bcrypt.generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","correo", "estado")

userSchema = UserSchema()
