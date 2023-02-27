from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")

# takes a request and name then returns a html file given the name
def greet(request, name):
    # a dictionary is passed that has keys of variable names and values of the value of said variable
    return render(request, "hello/greet.html", {"name": name.capitalize()})