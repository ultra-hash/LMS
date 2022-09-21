from asyncio.proactor_events import _ProactorBaseWritePipeTransport
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
        return redirect("books.list")
    else:
        return render(request, "books/books_form.html", {})

def update(request, pk):

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

def delete(request):
    
    return

def list(request):
    list_books = books.objects.all()
    return render(request, "books/books_list.html", {'list_books': list_books})
    
