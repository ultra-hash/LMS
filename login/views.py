from django.shortcuts import render, redirect
from .models import adminAccounts
from django.contrib import messages
# Create your views here.

def index(request):
    return redirect('books.list')

def login(request):
    if verify_login(request):
        return redirect('books.list')

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
    if verify_login(request):
        return redirect('books.list')
        
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if not adminAccounts.objects.filter(email=email).exists():
            admin = adminAccounts.objects.create(username=username, email=email, password=password)
            messages.success(request, "account created successfully")
            return redirect('login.login')
        else:
            messages.info(request, "email already registered")
            return redirect('login.register')
    else:
        return render(request, "login/register.html", {})


def logout(request):
    try:
        if request.session['login']:
            del request.session['login']
            messages.info(request, "logout successfull")
    except KeyError:
        pass
    finally:
        return redirect('books.list')


# return True or False
def verify_login(request):
    try:
        if request.session['login']:
            return True
    except KeyError:
        return False
