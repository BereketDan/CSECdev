from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.


def login(request):
    mydata = User_auth.objects.all()
    temp_store = []
    for _ in mydata:
        print(_.userName + _.password)
        temp_store.append(_.userName + _.password)
    if request.method == 'POST':
        name = request.POST.get('user_name')
        print(name)
        passs = request.POST.get('user_password')

        
        if name+passs in temp_store:
            return  member(request)
        else:
            print("run")    

            
          



    return render(request, "login.html")



def base(request):
    return render(request, "base.html")


def member(request):
    return render(request, "member.html")

def feedback(request):
    return render(request, "feedback.html")

def event(request):
    return render(request, "event.html")


def dashboard(request):
    return render(request, "dashboard.html")

def settings(request):
    return render(request, "settings.html")