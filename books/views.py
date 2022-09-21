from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import books

# Create your views here.

def index(request):
    return HttpResponse('Hello From Books')


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        book = books.objects.create(title=title)
        return redirect("books.index")
    else:
        return render(request, "books/books_form.html", {})

def update(request):
    return

def delete(request):
    return

def list(request):
    return
    
