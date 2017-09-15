from flask_testing import TestCase
from unittest import TestCase as UnitTestCase

import todo
from todo.models.todo import Todo


class BaseTestCase(TestCase, UnitTestCase):
    def create_app(self):
        return todo.create_app('testing')

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.app = self.create_app()
        self.client = self.app.test_client

        self.todo = {'first_name': 'First', 'last_name': 'Last', 'email': 'first@email.com',
                          'password': 'test_password', 'password_confirm': 'test_password'}

        with self.app.app_context():
            todo.db.session.close()
            todo.db.drop_all()
            todo.db.create_all()

    def add_todos(self):
        todo1 = Todo(name="Todo 1")
        todo2 = Todo(name="Todo 2")
        todo3 = Todo(name="Todo 3")
        todo1.save(), todo2.save(), todo3.save()

    def tearDown(self):
        super(BaseTestCase, self).tearDown()
        todo.db.session.remove()
        todo.db.drop_all()
