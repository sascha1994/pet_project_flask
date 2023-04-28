from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from app.database import db
from app.helpers.create_data import create_data
from app.views.auth.auth import auth_ns
from app.views.auth.favorites import favorite_ns
from app.views.auth.user import user_ns
from app.views.main.directors import directors_ns
from app.views.main.genres import genres_ns
from app.views.main.movies import movies_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()

# def register_extensions(application: Flask):
    db.init_app(application)
    CORS(application)
    api = Api(application, doc='/docs')
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorite_ns)
    api.add_namespace(user_ns)
    return application

