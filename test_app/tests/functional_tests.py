# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from datetime import datetime
from os import path
from time import sleep

from selenium import webdriver
from django.test import TestCase

from utils import Browser


class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = Browser()
        self.web_app = self.browser.open_app('http://localhost:8000/login')
        self.web_app.set_email('user@example.com')
        self.web_app.set_password('123456')
        self.web_app.submit_login()

    def tearDown(self):
        self.browser.close()

    def test_authentication(self):
        self.web_app.click_logout()

        self.assertEqual(self.web_app.page_title, 'Login page')

    def test_view_all_posts_and_create_post(self):
        post_title = 'another post title'
        post_content = 'another post content'

        self.web_app.click_posts()
        self.web_app.click_new_post()
        self.web_app.set_post_title(post_title)
        self.web_app.set_post_content(post_content)
        self.web_app.submit_post()

        self.assertIn(post_title, self.web_app.page_source)

    def test_view_one_post_and_create_post(self):
        post_title = 'just another post title'
        post_content = 'just another post content'

        self.web_app.click_posts()
        self.web_app.click_first_post()
        self.web_app.click_new_post()
        self.web_app.set_post_title(post_title)
        self.web_app.set_post_content(post_content)
        self.web_app.submit_post()

        self.assertIn(post_title, self.web_app.page_source)
