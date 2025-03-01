import unittest
from cloneapp import app

class TestApp(unittest.TestCase):
    def home(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, CI/CD with Jenkins!")
        
if __name__ == "__main__":
    unittest.main