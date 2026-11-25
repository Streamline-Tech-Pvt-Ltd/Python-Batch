from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def display_message(request):
    message = "Welcome to the Home Page!"
    return HttpResponse(message)


def home(request):
    data = {
        'Name': 'Anuj Kakad',
        'Age': 25,
        'City': 'Pune',
        'Country': 'India',
    }
    return render(request, 'home.html', data)

def date(request):
    data = datetime.now()
    context = {
        'current_date' : data,
    }
    return render(request, 'date.html', context)
