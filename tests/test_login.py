import json

from tests.BaseCase import BaseCase


class TestUserLogin(BaseCase):

    def test_successful_login(self):
        # Given
        email = "myfakeemail@gmail.com"
        password = "myfakepassword"
        payload = json.dumps({
            "email": email,
            "password": password
        })
        response = self.app.post('/api/v1/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # When
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    def test_login_with_invalid_email(self):
        # Given
        email = "myfakewrongemail@gmail.com"
        password = "myfakepassword"
        payload = {
            "email": email,
            "password": password
        }
        response = self.app.post('/api/v1/auth/signup', headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # When
        payload['email'] = "paurakh012@gmail.com"
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # Then
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(401, response.status_code)

    def test_login_with_invalid_password(self):
        # Given
        email = "myfakeemail@gmail.com"
        password = "myfakewrongpassword"
        payload = {
            "email": email,
            "password": password
        }
        response = self.app.post('/api/v1/auth/signup', headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # When
        payload['password'] = "mynotwrongpassword"
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # Then
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(401, response.status_code)
