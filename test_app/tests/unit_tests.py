# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase

from posts.models import Post
from users.models import User


class PostTestCase(TestCase):
    def setUp(self):
        User.objects.all().delete()
        Post.objects.all().delete()
        self.user = User(email='user@example.com',
                    first_name='John',
                    last_name='Smith',
                    password='123456')
        self.user.save()

    def test_post_create(self):
        post = Post(title="post title",
                    content="post content")
        post.pub_date = datetime.now()
        post.user = self.user
        post.save()
        self.assertEqual(Post.objects.count(), 1)

    def test_invalid_length_title(self):
        post = Post(title=101*'a',
                    content='post content')
        post.pub_date = datetime.now()
        post.user = self.user
        post.save()


class UserTestCase(TestCase):
    
    def setUp(self):
        User.objects.all().delete()

    def test_user_create(self):
        user = User(email='user@example.com',
                    first_name='John',
                    last_name='Smith',
                    password='123456')
        user.save()
        self.assertEqual(User.objects.count(), 1)

    def test_user_doesnot_create_with_non_uniq_email(self):
        with self.assertRaises(IntegrityError):
            for _ in xrange(2):
                user = User(email='user@example.com',
                            first_name='John',
                            last_name='Smith',
                            password='123456')
                user.save()
