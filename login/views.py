from django.shortcuts import render, redirect
from .models import adminAccounts
# Create your views here.

def login(request):
    return render(request, "login/login.html", {})

def register(request):
    return render(request, "login/register.html", {})