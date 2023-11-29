from django.shortcuts import render, redirect
from .models import Item

# Create your views here.

def item_list(request):
    items = Item.objects.all()
    return render(request, 'todo_app/todo_list.html', {'items': items})
