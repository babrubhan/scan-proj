import json

from tests.BaseCase import BaseCase


class TestUserLogin(BaseCase):

    def test_successful_login(self):
        # Given
        email = "myfakeemail@gmail.com"
        password = "myfakepassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        self.app.post('/api/v1/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        person_payload = {
            "name": "Babru",
            "resources": ["R1", "R2"],
            "limit": 5
        }
        # When
        response = self.app.post('/api/v1/persons',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(person_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
