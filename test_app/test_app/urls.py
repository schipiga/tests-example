# -*- coding: utf-8 -*-

__author__ = "svchipiga@yandex-team.ru"

from django.conf.urls import patterns, include, url
from django.contrib import admin

from posts.views import show_posts, show_post, create_post
from users.views import show_users, show_user, create_user
from views import login, logout, registration, main


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', main, name='main'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^registration$', registration, name='registration'),
    url(r'^users$', show_users, name='show_users'),
    url(r'^users/(\d+)$', show_user, name='show_user'),
    url(r'^users/create$', create_user, name='create_user'),
    url(r'^users/(\d+)/posts$', show_posts, name='show_posts'),
    url(r'^users/(\d+)/posts/(\d+)$', show_post, name='show_post'),
    url(r'^users/(\d+)/posts/create$', create_post, name='create_post'),
)
