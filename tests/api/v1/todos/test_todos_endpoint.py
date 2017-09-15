import json

from tests.base_test_case import BaseTestCase


class TestTodoEndpoints(BaseTestCase):
    def setUp(self):
        super(TestTodoEndpoints, self).setUp()
        self.todo = {'name': 'Todo item'}

    def test_get_returns_all_bucketlist(self):
        self.add_todos()
        response = self.client().get('/api/v1/todos')

        results = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(results.get('results')), 3)

    def test_get_all_returns_an_empty_array_if_no_todos_are_present(self):
        response = self.client().get('/api/v1/todos')

        results = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(results.get('results')), 0)
