# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from datetime import datetime

from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User)
