from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import AddBookForm, EditBookForm
from django.contrib.auth import logout, login

def homepage(request):
    books = Book.objects.all()
    context = {
        "page_title": "Homepage",
        "books": books,
    }
    return render(request, 'homepage.html', context)

def book(request, pk):
    book = Book.objects.get(id=pk)
    context = {
        "page_title": "Book",
        "book": book,
    }
    return render(request, "book.html", context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book', pk=book.id) 
    else:
        form = AddBookForm()
    context = {'form': form}
    return render(request, 'add_book.html', context)

def edit_book(request, pk):
    if request.method == 'POST':
        form = EditBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book', pk=pk)  
    else:
        form = EditBookForm()
    context = {'form': form, 'book': book}
    return render(request, 'edit_book.html', context)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('/')
    return render(request, 'delete_book.html', {'book': book})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration.html', {'form': form})
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage')  
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')  