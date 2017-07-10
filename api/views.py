from django.shortcuts import render
from django.http import *
# Create your views here.
def hello(request):
    return HttpResponse("Hello, my first api.")

def saySomthing(request):
    return HttpResponse("restart test.")


def current_time(request):
    return HttpResponse("将要显示当前时间")

def home(request):
    return HttpResponse("home")
