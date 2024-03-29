# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from hashlib import md5

from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    encrypted_password = models.CharField(max_length=255)

    def __init__(self, *args, **kwgs):
        password = kwgs.pop('password', None)
        if password:
            self.password = password
        super(User, self).__init__(*args, **kwgs)


    def save(self):
        self.encrypted_password = md5(self.password).hexdigest()
        return super(User, self).save()

    def has_password(self, password):
        return self.encrypted_password == md5(password).hexdigest()
