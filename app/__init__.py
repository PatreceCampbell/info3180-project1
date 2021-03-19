from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy


# IMAGES_FOLDER = './app/static/Images'


app = Flask(__name__)



app.config.from_object(Config)


db = SQLAlchemy(app)

print("Hey", app.config["SQLALCHEMY_DATABASE_URI"])
from app import views, models