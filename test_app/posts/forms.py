# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from django import forms

from posts.models import Post


class PostForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)

    def save(self):
        post = Post(title=self.cleaned_data['title'],
                    content=self.cleaned_data['content'],
                    pub_date=self.pub_date, user_id=self.user_id)
        post.save()
