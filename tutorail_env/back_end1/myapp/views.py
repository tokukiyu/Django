from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home (re):
    return HttpResponse('hello world')
def homeA (re):
    return HttpResponse('hello world') 