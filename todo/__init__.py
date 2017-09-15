from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .config import configuration

db = SQLAlchemy()


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(configuration[env_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.url_map.strict_slashes = False
    db.init_app(app)

    from api.v1.todos import todos as todos_blueprint
    api = Api(todos_blueprint)
    app.register_blueprint(todos_blueprint, url_prefix='/api/v1')
    from api.v1.todos.views import Todos
    api.add_resource(Todos, '/todos', endpoint='todos')

    return app
