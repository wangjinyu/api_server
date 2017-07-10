
from django.conf.urls import url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^$', views.hello, name='hello'),
    url(r'^saySomthing/', views.saySomthing, name='saySomthing'),
    url(r'^current_time/', views.current_time, name='current_time'),
    url(r'^home/', views.home, name='home'),
]
