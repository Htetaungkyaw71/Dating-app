from django.http import response
from django.test import TestCase,Client


class Index(TestCase):
    def test_valid_index(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code,302)

    def test_valid_login(self):
        c = Client()
        response = c.get('/login/')
        self.assertEqual(response.status_code,200)

    def test_valid_register(self):
        c = Client()
        response = c.get('/register/')
        self.assertEqual(response.status_code,200)