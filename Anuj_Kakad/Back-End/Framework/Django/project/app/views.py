from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display_message(request):
    message = "hello welcome"
    return HttpResponse(message)

def home(request):
    data = {
        "name" : "Anuj",
        "Age" : 23,
        "City" : "Sangamner"}
    return render(request, 'home.html', data)