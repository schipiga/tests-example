# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from django import forms

from users.models import User

class SessionForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(),
                                            required=True)

    def save(self):
        user = User(email=self.cleaned_data['email'],
                    first_name=self.cleaned_data['first_name'],
                    last_name=self.cleaned_data['last_name'],
                    password=self.cleaned_data['password'])
        user.save()
