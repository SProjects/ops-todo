from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

from .config import configuration

api = Api()
db = SQLAlchemy()


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(configuration[env_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.url_map.strict_slashes = False
    api.init_app(app)
    db.init_app(app)

    return app
