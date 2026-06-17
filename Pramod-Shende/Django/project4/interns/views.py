from django.shortcuts import render,redirect
from .models import Intern
from .forms import InternForm
# Create your views here.
def intern_list(request):
    if request.method == 'POST':
        form = InternForm(request. POST)
        if form.is_valid():
            form. save()
            return redirect('/')

    else:
        form = InternForm()
    interns = Intern.objects.all()

    return render(request,'interns/interns_list.html', {'form': form,'interns': interns})