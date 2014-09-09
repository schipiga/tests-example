# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from os import path
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException

from waiter import Waiter
from web_app import WebApp


TIMEOUT = 30


class Browser(object):

    def __init__(self):
        self.web_driver = webdriver.Chrome(path.join(path.dirname(__file__),
                                                     'chromedriver'))

    def find_element(self, id_selector, timeout=TIMEOUT):

        def _is_element_present():
            return self.web_driver.find_element_by_id(id_selector)

        element = Waiter.poll(timeout, _is_element_present)
        if element:
            return element

        raise TimeoutException('Element "%s" was present after %s seconds.' %
                               (id_selector, timeout))

    def open_app(self, url):
        return WebApp(self, url)

    def close(self):
        self.web_driver.quit()

    def open(self, url):
        self.web_driver.get(url)
        self.wait_page_load()

    def switch_to_active_tab(self):

        def is_window_active():
            return self.web_driver.execute_script(
                "return document.visibilityState == 'visible'")

        if not is_window_active():
            for window_handle in self.web_driver.window_handles:
                self.web_driver.switch_to.window(window_handle)
                if is_window_active():
                    break

    def wait_page_load(self, timeout=TIMEOUT):

        def _wait_page_load():
            return self.is_document_ready

        if Waiter.poll(timeout, _wait_page_load):
            return
        else:
            raise TimeoutException(
                "Page wasn't load after %s seconds." % timeout)

    @property
    def is_document_ready(self):
        try:
            result = self.web_driver.execute_script(
                "return document.readyState == 'complete'")
        except WebDriverException:
            result = False
        return result
