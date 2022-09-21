from django.shortcuts import render, redirect
from .models import adminAccounts
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if adminAccounts.objects.filter(email=email, password=password).exists():
            admin = adminAccounts.objects.get(email=email, password=password)
            request.session['login'] = True
            messages.success(request, "login successfull")
            return redirect('books.list')
        else:
            messages.info(request, "Email and Password don't match.")
            return redirect('login.login')
    else:
        return render(request, "login/login.html", {})

def register(request):
    return render(request, "login/register.html", {})