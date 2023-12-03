from email.policy import default
import pdb
from django.shortcuts import render
from django.http import HttpResponse

todo_array = [
    {"id": 1, "name": "homework"},
    {"id": 2, "name": "work"},
    {"id": 3, "name": "doctors"},
]

# View function for base
def base(request):
    return (HttpResponse("<h2>Base Page<h2>"))

def about(request):
    return (render(request, "about.html"))

def add(request):
    return (render(request, "add.html"))

def completing(request):
    return (render(request, "completing.html"))

# View function for render contact us template
def todo(request):
    print(todo_array)
    return (render(
        request, "todo.html",
        {"todo": todo_array}))
