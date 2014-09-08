# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.shortcuts import render

from forms import PostForm
from posts.models import Post


def show_posts(request, user_id):
    posts = Post.objects.filter(user=user_id)    
    return render(request, 'show_posts.html',
                  {'user_id': user_id, 'posts': posts})

def show_post(request, user_id, post_id):
    post = Post.objects.get(id=post_id, user=user_id)
    return render(request, 'show_post.html', {'user_id': user_id, 'post': post})

def create_post(request, user_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.user_id = user_id
            form.pub_date = datetime.now()
            form.save()
            return redirect(reverse('show_posts', args=(user_id,)))
    form = PostForm()
    return render(request, 'create_post.html', {'user_id': user_id, 'form': form})
