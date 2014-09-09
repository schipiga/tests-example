# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase

from posts.models import Post
from users.models import User


USER_DATA = {'email': 'user@example.com',
             'first_name': 'John',
             'last_name': 'Smith',
             'password': '123456'}


POST_DATA = {'title': 'post title',
             'content': 'post content'}


class UserTestCase(TestCase):
    
    def setUp(self):
        User.objects.all().delete()

    def test_user_create(self):
        user = User(**USER_DATA)
        user.save()

        self.assertEqual(User.objects.count(), 1)

    def test_user_no_password(self):
        with self.assertRaises(AttributeError):
            user = User()
            user.save()

    def test_user_no_data(self):
        user = User(password='1')
        user.save()

        self.assertEqual(User.objects.count(), 0)

    def test_valid_has_password(self):
        user = User(**USER_DATA)
        user.save()

        self.assertTrue(user.has_password('123456'))

    def test_invalid_has_password(self):
        user = User(**USER_DATA)
        user.save()

        self.assertFalse(user.has_password('invalid_password'))

    def test_user_doesnot_create_with_non_uniq_email(self):
        with self.assertRaises(IntegrityError):
            for _ in xrange(2):
                user = User(**USER_DATA)
                user.save()


class PostTestCase(TestCase):

    def setUp(self):
        User.objects.all().delete()
        user = User(**USER_DATA)
        user.save()

        Post.objects.all().delete()
        self.post_data = POST_DATA.copy()
        self.post_data.update({'pub_data': datetime.now(), 'user': user})

    def test_post_create(self):
        post = Post(**self.post_data)
        post.save()

        self.assertEqual(Post.objects.count(), 1)

    def test_invalid_length_title(self):
        self.post_data['title'] = 101 * 'a'

        post = Post(**self.post_data)
        post.save()

        self.assertEqual(Post.objects.count(), 0)

    def test_post_no_data
        post = Post()
        post.save()

        self.assertEqual(Post.objects.count(), 0)
