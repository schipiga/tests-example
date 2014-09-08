# -*- coding: utf-8 -*-

__author__ = 'f1ash@yandex-team.ru'

from time import sleep
from datetime import datetime, timedelta


class Waiter(object):

    @classmethod
    def poll(cls, timeout, function, *args, **kwargs):

        first_check = True
        delay = datetime.now() + timedelta(seconds=timeout)
        while first_check or datetime.now() <= delay:
            first_check = False
            result = function(*args, **kwargs) or False
            if result:
                break
            sleep(.5)

        return result
