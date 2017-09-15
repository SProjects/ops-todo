from flask_restful import Resource, fields, marshal
from sqlalchemy import desc

from todo.models.todo import Todo

todo_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'done': fields.String,
}


class Todos(Resource):
    def get(self):
        todos = Todo.query.order_by(desc(Todo.created_at)).all()
        return dict(results=marshal(todos, todo_fields)), 200
