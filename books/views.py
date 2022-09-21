from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import books
from login.views import login, verify_login

# Create your views here.
    # admin 
        # create , update, list , delete
    # student
        # list


def index(request):
    return HttpResponse('Hello From Books')


def create(request):
    if not verify_login(request):
        return redirect('login.login')

    if request.method == 'POST':
        title = request.POST['title']
        book = books.objects.create(title=title)
        return redirect("books.list")
    else:
        return render(request, "books/books_form.html", {'login': verify_login(request)})

def update(request, pk):
    if not verify_login(request):
        return redirect('login.login')

    if books.objects.filter(pk=pk).exists():
            book = books.objects.get(pk=pk)
    else:
        return redirect('books.list')

    if request.method == 'POST':
        newTitle = request.POST['title']
        book.title = newTitle
        book.save()
        return redirect('books.list')
    else:
        return render(request, "books/books_form.html", {'book':book})

def delete(request, pk):
    if not verify_login(request):
        return redirect('login.login')
        
    if books.objects.filter(pk=pk).exists():
        book = books.objects.get(pk=pk)
        book.delete()
    return redirect("books.list")

def list(request):
    login = verify_login(request)
    list_books = books.objects.all()
    return render(request, "books/books_list.html", {'list_books': list_books, 'login': login})
    
