from django.shortcuts import render
from django.http import HttpResponse  
import datetime 


def home(request):
    return HttpResponse("Hello, streamline tech python batch")

def example(request):
    Message = ''

    if request.method == 'GET':
        Operation = request.GET.get('Message')

        if Operation == 'add':
            a = int(request.GET.get('a'))
            b = int(request.GET.get('b'))
            result = a + b
            Message = f"The result of addition is {result}"

        elif Operation == 'sub':
            a=int(request.GET.get('a'))
            b=int(request.GET.get('b'))
            result = a - b
            Message = f"The result of subtraction is {result}"

        elif Operation == 'mul':
            a=int(request.GET.get('a'))
            b=int(request.GET.get('b'))
            result = a * b
            Message = f"The result of multiplication is {result}"

        elif Operation == 'div':
            a=int(request.GET.get('a'))
            b=int(request.GET.get('b'))
            if b != 0:
                result = a / b
                Message = f"The result of division is {result}"

        else:
            Message = "Invalid operation"

    return HttpResponse(Message)   

def date(request):
    date = datetime.datetime.now()
    templatefile= 'date.html'
    dict = {'date': date}
    return render(request,templatefile,dict)
    
    
    
def ifdemo(request):
    Data ={
        'name':'Pramod Shende',
        'inVisible':True,
        'LoggedIn':False,
        'CountryCode':'india',
        'workExperiance':15,
        'stateCode':'maharashtra',
        
    }    
    
    templatefile ='ifdemo.html'
    dict = {'Data': Data}
    return render(request,templatefile,dict)



def fordemo(request):
    products = []
    products.append({'Emp_id':101,'Emp_name':'Pramod','Emp_salary':50000,'Emp_Experience':15})
    products.append({'Emp_id':102,'Emp_name':'omkar','Emp_salary':40000,'Emp_Experience':5})
    products.append({'Emp_id':103,'Emp_name':'Rushikesh','Emp_salary':45000,'Emp_Experience':3})
   
    templatefile ='fordemo.html'
    dict = {'products': products}
    return render(request,templatefile,dict)



def CallRestAPI(request):
    url = 'https://fakestoreapi.com/users'
    response = requests.get(url)
    return response

def user_data(request):
    templatefile = 'userdata.html'
    response = CallRestAPI(request)
    dict = {'users': response.json()}
    return render(request, templatefile, dict)

def user_data2(request):
    templatefile = 'userdata2.html'
    image = 'https://pravatar.cc/'
    response = CallRestAPI(request)
    dict = {'users': response.json()}
    return render(request, templatefile, dict)

def CallRestAPI2(userid):
    BASE_URL = 'https://fakestoreapi.com'
    response =requests.get(f"{BASE_URL}/users/{userid}")
    return(response)
    
def LoadUserDetails(request):
    if request.method == "POST":
        counter = int(request.POST.get("useridcounter") or 1)
        if(request.POST.get("btnNext")):
            counter += 1
            if counter >= 11:
                counter = 1
        elif(request.POST.get("btnPrevious")):
                counter -= 1
            
    else:
        counter = 1
                
    templateFileName = 'user3.html'
    response = CallRestAPI2(counter)
    image = 'https://i.pravatar.cc/'
    context = {"user": response.json(), "image": image}
    return render(request, templateFileName, context)
