from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from interns.forms import SignUpForm
# Create your views here.

def home(request):
    return render(request, 'interns/home.html')

def signup(request):
    if request.method == 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'interns/signup.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST' :
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'interns/login.html', {'form' : form})