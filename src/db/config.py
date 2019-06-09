from app import app

"""Importar ORM que desee utilizar, o bien cree uno en este archivo."""

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:miguelangel@localhost/PruebaFlask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.secret_key = 'clave-secreta'