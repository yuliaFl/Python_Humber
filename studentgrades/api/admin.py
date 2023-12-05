from django.contrib import admin
from .models import Student, CompletedCourse, OngoingCourse

admin.site.register(Student)
admin.site.register(CompletedCourse)
admin.site.register(OngoingCourse)
