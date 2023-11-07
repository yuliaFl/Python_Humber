from django.http import HttpResponse
import datetime

def greetings(request):
    name = "Yulia"  
    student_id = "n01342767"  
    return HttpResponse(f'<h1>Name: {name}</h1><h1>Student ID: {student_id}</h1>')

def current_datetime(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f'Date and Time: {current_time}')

