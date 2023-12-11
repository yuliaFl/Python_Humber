from django.urls import path
from . import views

urlpatterns = [
    path('routes', views.routes, name="api"),
    path('allstudents', views.students, name="students"),
    path('course', views.course, name="course"),
    path('student', views.student, name="student"),
    path('completedcourses', views.completedcourses, name="completedcourses"),
    path('ongoingcourses', views.ongoingcourses, name="ongoingcourses"),
]
