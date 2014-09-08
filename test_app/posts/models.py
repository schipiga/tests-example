# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from datetime import datetime

from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    pub_date = models.DateTimeField(null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)
