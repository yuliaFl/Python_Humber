from django.urls import path
from . import views

urlpatterns = [
    path('todo_app', views.todo),

    path('todo', views.todo, name="todo"),

    path('about', views.about, name="about"),

    path('add', views.add, name="add"),

    path('completing', views.completing, name="completing"),


]
