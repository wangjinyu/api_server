
from django.conf.urls import *
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
]
