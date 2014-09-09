# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from urlparse import urlparse


class WebApp(object):

    def __init__(self, browser, url):
        parsed_url = urlparse(url)
        self.host = "%s://%s" % (parsed_url.scheme, parsed_url.netloc)

        self.browser = browser
        self.browser.switch_to_active_tab()
        self.browser.open(url)

    def click_first_post(self):
        elem = self.browser.find_element('id_first_post')
        elem.click()
        self.browser.wait_page_load()

    def set_post_title(self, title):
        elem = self.browser.find_element('id_title')
        elem.send_keys(title)

    def set_post_content(self, content):
        elem = self.browser.find_element('id_content')
        elem.send_keys(content)

    def submit_post(self):
        elem = self.browser.find_element('id_post')
        elem.click()
        self.browser.wait_page_load()

    def click_posts(self):
        elem = self.browser.find_element('id_posts')
        elem.click()
        self.browser.wait_page_load()

    def click_new_post(self):
        elem = self.browser.find_element('id_new_post')
        elem.click()
        self.browser.wait_page_load()

    def set_email(self, email):
        elem = self.browser.find_element('id_email')
        elem.send_keys(email)

    def set_password(self, password):
        elem = self.browser.find_element('id_password')
        elem.send_keys(password)

    def submit_login(self):
        elem = self.browser.find_element('id_login')
        elem.click()
        self.browser.wait_page_load()

    def click_logout(self):
        elem = self.browser.find_element('id_logout')
        elem.click()
        self.browser.wait_page_load()
