from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Intern


def index(request):
    interns = Intern.objects.all()

    context = {
        'interns': interns
    }

    return render(request, 'index.html', context)


def add(request):

    if request.method == 'POST':

        Intern.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            department=request.POST.get('department')
        )

        messages.success(request, "Intern added successfully!")

    return redirect('/')


def update(request):

    if request.method == 'POST':

        intern_id = request.POST.get('intern_id')

        Intern.objects.filter(id=intern_id).update(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            department=request.POST.get('department')
        )

        messages.success(request, "Intern updated successfully!")

    return redirect('/')


def delete(request):

    if request.method == 'POST':
        intern_id = request.POST.get('intern_id')
        Intern.objects.filter(id=intern_id).delete()
        messages.success(request, "Intern deleted successfully!")

    return redirect('/')