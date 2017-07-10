
from django.conf.urls import url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^$', views.hello, name='hello'),
    url(r'^saySomthing/', views.saySomthing, name='saySomthing')
]
