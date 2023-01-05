from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from decouple import config


USER = config('USER', cast=str)
PASSWORD = config('PASSWORD', cast=str)
HOST = config('HOST', cast=str)
PORT = config('PORT', cast=str)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USER}:{PASSWORD}@{HOST}/learningSQLAlchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db:SQLAlchemy = SQLAlchemy(app)