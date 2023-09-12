from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon !")
 
def about(request):
    about_content={'about': "<p> lorem 4 p random </p>"}
    return render(request, "about.html", about_content)

def menu(request):
    return HttpResponse("Menu for Little Lemon")
 
def book(request):
    return HttpResponse("Make a booking")

