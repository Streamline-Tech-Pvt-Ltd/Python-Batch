from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def display_message(request):
    message = "Welcome to the Home Page!"
    return HttpResponse(message)