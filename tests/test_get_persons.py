import unittest
import json

from tests.BaseCase import BaseCase


class TestGetPersons(BaseCase):

    def test_empty_response(self):
        response = self.app.get('/api/v1/persons')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    def test_person_response(self):
        # Given
        email = "myfakeemail@gmail.com"
        password = "myfakepassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        response = self.app.post('/api/v1/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        user_id = response.json['id']
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        person_payload = {
            "name": "Babru2",
            "resources": ["R1", "R2"],
            "limit": 7
        }
        response = self.app.post('/api/v1/persons',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(person_payload))

        # When
        response = self.app.get('/api/v1/persons')
        added_movie = response.json[0]

        # Then
        self.assertEqual(person_payload['name'], added_movie['name'])
        self.assertEqual(person_payload['resources'], added_movie['resources'])
        self.assertEqual(person_payload['limit'], added_movie['limit'])
        self.assertEqual(user_id, added_movie['added_by']['$oid'])
        self.assertEqual(200, response.status_code)
