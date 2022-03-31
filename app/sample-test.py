from main import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        
    def test_home_title(self):
        response = self.client.get("/")
        self.assertEqual(response.data.decode('UTF-8'), "Hey, we have Flask in a Docker container!")

        
if __name__ == '__main__':
    unittest.main()