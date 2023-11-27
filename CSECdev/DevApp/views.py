from django.shortcuts import render,redirect
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
        passs = request.POST.get('user_password')
        request.session['name'] = name
        if name and passs is None:
            print("none")
        
        if name+passs in temp_store:
            return  member(request)
        else:
            return redirect('login')   

            


    return render(request, "login.html")

def logout(request):
    request.session.flush()
    return redirect('login')


def base(request):
    return render(request, "base.html")


def member(request):
    name = request.session.get('name')
    if name:
        return render(request, "member.html")
    else:
        return redirect('login') 
def feedback(request):
    name = request.session.get('name')
    if name:
        return render(request, "feedback.html")
    else:
        return redirect('login')

def event(request):
    name = request.session.get('name')
    if name:
        return render(request, "event.html")
    else:
        return redirect('login')



def dashboard(request):
    name = request.session.get('name')
    if name:
        return render(request, "dashboard.html")
    else:
        return redirect('login')


def settings(request):
    name = request.session.get('name')
    if name:
        return render(request, "settings.html")
    else:
        return redirect('login')
    