from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Course
from .models import CompletedCourse
from .models import OngoingCourse
from .serializers import StudentSerializer
from .serializers import CourseSerializer
from .serializers import CompletedCourseSerializer
from .serializers import OngoingCourseSerializer

@api_view(['GET'])
def routes(request):
    routes = [
         'GET /api/routes/',
         'GET /api/students/',
         'POST /api/student',
         'GET /api/averagegrade/:id',
         'GET /api/completedcourses/:id',
         'GET /api/ongoingcourses/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def course(request):
    routes = {
        #student= Course.objects.all()

    }
    return Response(routes)

@api_view(['GET'])
def students(request):
        students = Student.objects.all()
        serializer =StudentSerializer(students, many =True)
        return Response(serializer.data)

@api_view(['GET'])
def ongoingcourses(request):
        ongoingcourses = OngoingCourse.objects.all()
        serializer =OngoingCourseSerializer(ongoingcourses, many =True)
        return Response(serializer.data)

#Create POST route that accepts student id and display student details
@api_view(['POST'])
def completedcourses(request):
    routes = {
    }
    return Response(routes)

# Create POST route that accepts student id and display student details
@api_view(['POST'])
def student(request):
#    id = request.data.get('id')
#    student = get_object(Student, id=id)
    serializer = StudentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()    

    return Response({
        'name': "Success",
    })
# Create POST route to return student ongoing courses, accept student id
# Create POST route to return student completed courses, accept student id
# Create POST route to return grade of completed course, accept student id and course name
# Create POST route to return student average grade, accept student id