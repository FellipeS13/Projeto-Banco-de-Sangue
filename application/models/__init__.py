from application import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

@login_manager.user_loader
def load_usuarioSUS(id_usuario):
    return UsuarioSUS.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    telefone = database.Column(database.String, nullable=False)
    tiposanguineo = database.Column(database.String, nullable=False)

class UsuarioSUS(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True, unique=True)
    nome = database.Column(database.String, nullable=False)
    cnpj = database.Column(database.String, nullable=False)
    senha = database.Column(database.String, nullable=False)