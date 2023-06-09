from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '028c1dc90fd930af8107ca980bf16f6a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitebancosangue.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Realize login para prosseguir (Phillipe melhor professor <3)'
login_manager.login_message_category = 'alert alert-warning'
from application import routers