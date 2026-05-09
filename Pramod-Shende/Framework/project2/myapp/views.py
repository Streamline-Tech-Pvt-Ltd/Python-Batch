from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    return HttpResponse('hello welcome to the Django Example')


def date(request):
    date = datetime.datetime.now()
    templatefile ='ex.html'
    dict ={'date': date}        
    return render(request,templatefile,dict)