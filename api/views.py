from django.shortcuts import render
from django.http import *
# Create your views here.
def hello(request):
    return HttpResponse("Hello, my first api.")

def saySomthing(request):
    return HttpResponse("restart test.")
