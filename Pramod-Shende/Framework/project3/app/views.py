from django.shortcuts import render

# Create your views here.
def interns(request):
    interns_list = []
    interns_list.append({"id":1,"name":"Pramod","dept":"Python","salary":50000,"s_date":'20-01-2026',"e_date":'25-06-2026'})
    interns_list.append({"id":2,"name":"Rushikesh","dept":"Java","salary":40000,"s_date":'20-02-2026',"e_date":'25-05-2026'})
    
    tempfile = 'data.html'
    dict = {"interns_list" : interns_list}
    return render(request,tempfile,dict)




