# tests/test_app.py
import unittest
from app import app

class FlaskTodoTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'To-Do List', response.data)

if __name__ == '__main__':
    unittest.main()
