from django.shortcuts import render
from http import *
# Create your views here.
def hello(request):
    return HttpResponse("Hello, my first api.")
