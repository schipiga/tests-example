# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from hashlib import md5

from users.models import User


def authenticate_user(email, password):
    user = User.objects.get(email=email)
    if user:
        if user.has_password(password):
            return user


def login_user(request, user):
    request.session['user'] = user.id
    request.session['token'] = md5(user.encrypted_password).hexdigest()


def logout_user(request):
    request.session.clear()
