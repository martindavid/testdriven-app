import json
import unittest
from http import HTTPStatus

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):

    def test_users(self):
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])



if __name__ == '__main__':
    unittest.main()

