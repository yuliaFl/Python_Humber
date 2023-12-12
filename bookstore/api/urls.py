from django.urls import path
from . import views

# Define API routes
urlpatterns = [
    path('',  views.getRoutes),
    path('books/', views.getBooks),
    path('books/<str:pk>/', views.getBook),
]
