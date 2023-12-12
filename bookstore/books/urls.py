from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book/<str:pk>/', views.book, name='book'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<str:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<str:pk>/', views.delete_book, name='delete_book'),
    path('register/', views.registration, name='register'),
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'), 
]
