from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def login(request):
    return render(request, "login.html")


def base(request):
    return render(request, "base.html")


def member(request):
    return render(request, "member.html")

def feedback(request):
    return render(request, "feedback.html")

