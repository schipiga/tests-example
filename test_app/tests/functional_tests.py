# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from os import path
from time import sleep

from selenium import webdriver
from django.test import TestCase


class FunctionalTestCase(TestCase):

    def setUp(self):
        tests_dir = path.dirname(__file__)
        self.chromedriver_path = path.join(tests_dir, 'chromedriver')
        browser = webdriver.Chrome(self.chromedriver_path)
        sleep(5)
        browser.get('http://localhost:8000/login')
        sleep(5)
        browser.quit()

    def tearDown(self):
        browser.quit()

    def test_authentication(self):

        browser = Browser.launch()
        app = browser.open_app(login_url)
        app.set_email(email)
        app.set_password(password)
        app.submit_login()
        self.assertEqual(app.get_first_name(), 'Sergey')
        app.click_logout()
        self.assertEqual(app.page_url, login_url)
        self.assertEqual(app.get_cookes(), {})

    def test_view_all_posts_and_create_post(self):
        browser = Browser.launch()
        app = browser.open_app(login_url)
        app.set_email(email)
        app.set_password(password)
        app.submit_login()
        app.open_posts()
        self.assertEqual(app.page_url, '/user/1/posts')
        app.click_new_post()
        self.assertEqual(app.page_url, '/user/1/create_post')
        app.set_post_title('hello world')
        app.set_post_content('my content')
        app.submit_post()
        self.assertEqual(app.page_url, '/user/1/posts')
        self.assertEqual(app.post_titles(), 'hello world')


    def test_view_one_post_and_create_post(self):
        browser = Browser.launch()
        app = browser.open_app(login_url)
        app.set_email(email)
        app.set_password(password)
        app.submit_login()
        app.open_posts()
        self.assertEqual(app.page_url, '/user/1/posts')
        app.click_post_title()
        self.assertEqual(app.page_url, '/user/1/post/1')
        app.click_new_post()
        self.assertEqual(app.page_url, '/user/1/create_post')
        app.set_post_title('hello world')
        app.set_post_content('my content')
        app.submit_post()
        self.assertEqual(app.page_url, '/user/1/posts')
        self.assertEqual(app.post_titles(), 'hello world')
