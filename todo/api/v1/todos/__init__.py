from flask import Blueprint

todos = Blueprint('todos', __name__)

from todo.api.v1.todos import views

