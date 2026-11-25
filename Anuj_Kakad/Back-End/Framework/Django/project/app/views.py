from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import requests

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


def calculator(request):
    message = ''
    if (request.method == 'GET'):
        if (request.GET.get('message') == 'Add'):
            a = int(request.GET.get('a'))
            b = int(request.GET.get('b'))
            message = a + b

        elif (request.GET.get("message") == "Sub"):
            a = int(request.GET.get ("a"))
            b = int(request.GET.get ("b"))
            message = a - b

        elif (request.GET.get('message') == 'Mul'):
            a = int(request.GET.get('a'))
            b = int(request.GET.get('b'))
            message = a * b

        elif (request.GET.get("message") == "Div"):
            a = int(request.GET.get ("a"))
            b = int(request.GET.get ("b"))
            message = a / b

        else:
            return HttpResponse("Invalid Operation")

    return HttpResponse(f"The Result is :- {message}")


def ifdemo(request):
    Data = {
        'Name': 'Anuj Kakad',
        'Age': 25,
        'City': 'Pune',
        'Country': 'India',
    }
    templatefilename = 'ifdemo.html'
    dict1 = {'data': Data}
    return render(request,templatefilename,dict1)


def fordemo(request):
    Products = [
        {'id':101,"prod_name":"shirt","price":500,"quantity": 5},
        {'id':102,"prod_name":"shorts","price":1000,"quantity": 2},
        {'id':103,"prod_name":"jeans","price":700,"quantity": 1},
        {'id':104,"prod_name":"hat","price":200,"quantity": 4},
        {'id':105,"prod_name":"formal shirt","price":400,"quantity": 10},
    ]
    templatefilename = 'fordemo.html'
    dict1 = {'products':Products}
    return render(request,templatefilename,dict1)


def CallRestAPI(request):
    url = 'https://fakestoreapi.com/users'
    responce = requests.get(url)
    return responce

def user_Data(request):
    templatefile = 'user_data.html'
    response = CallRestAPI(request)
    dict = {'data': response.json()}
    return render(request, templatefile, dict)
