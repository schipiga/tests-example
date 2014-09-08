# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from hashlib import md5

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from users.models import User


def show_users(request):
    pass


def show_user(request, user_id):
    id = request.session['user']
    token = request.session['token']
    user = User.objects.get(id=id)
    if md5(user.encrypted_password).hexdigest() == token:
        return render(request, 'show_user.html', {'user': user})
    else:
        return redirect(reverse('login'))

def create_user(request):
    pass
