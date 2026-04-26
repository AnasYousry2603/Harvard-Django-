from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
# we write the directory before the index.html
# so to specify which index.html is it for so no conflict happens

def Anas(request):
    return HttpResponse("hello, anas")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })