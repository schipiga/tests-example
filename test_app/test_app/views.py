# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from forms import SessionForm, RegistrationForm
from users import login_user, logout_user, authenticate_user


def login(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            user = authenticate_user(form.cleaned_data['email'],
                                     form.cleaned_data['password'])
            if user:
                login_user(request, user)
                return redirect(reverse('show_user', args=(user.id,)))
    form = SessionForm()
    return render(request, 'login.html', {'form': form.as_p()})


def logout(request):
    logout_user(request)
    return redirect(reverse('login'))


def registration(request): 
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    form = RegistrationForm()   
    return render(request, "registration.html", {"form": form.as_p()})


def main(request):
    if request.session.get('token'):
        return redirect(reverse('show_user', args=(request.session['user'],)))
    else:
        return redirect(reverse('login'))
