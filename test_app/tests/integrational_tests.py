# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from hashlib import md5

from django.test import TestCase, Client

from users.models import User


class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        User.objects.all().delete()
        self.user = User(email='user@example.com',
                         first_name='John',
                         last_name='Smith',
                         password='123456')
        self.user.save()

    def test_login(self):
        self.client.post('/login',
                         {'email': 'user@example.com', 'password': '123456'})

        expected_token = md5(self.user.encrypted_password).hexdigest()

        self.assertEqual(self.client.session['token'], expected_token)

    def test_logout(self):
        self.client.post('/login',
                         {'email': 'user@example.com', 'password': '123456'})
        self.client.get('/logout')

        with self.assertRaises(KeyError):
            self.client.session['token']

    def test_registration(self):
        User.objects.all().delete()

        self.client.post('/registration', {'email': 'user@example.com',
                                           'first_name': 'John',
                                           'last_name': 'Smith',
                                           'password': '123456',
                                           'password_confirmation': '123456'})

        self.assertEqual(User.objects.count(), 1)
