from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def display_message(request):
    message = "Hello, Welcome My First Django Project!"
    return HttpResponse(message)
