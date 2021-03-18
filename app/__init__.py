from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

# IMAGES_FOLDER = './app/static/Images'


app = Flask(__name__)


db = SQLAlchemy(app)

app.config.from_object(Config)

from app import views