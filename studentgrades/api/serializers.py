from rest_framework.serializers import ModelSerializer
from api.models import Student
from api.models import Course
from api.models import CompletedCourse
from api.models import OngoingCourse

class StudentSerializer (ModelSerializer):
    class Meta:
        model = Student
        fields='__all__'
class CourseSerializer (ModelSerializer):
    class Meta:
        model = Course
        fields='__all__'
class CompletedCourseSerializer (ModelSerializer):
    class Meta:
        model = CompletedCourse
        fields='__all__'
class OngoingCourseSerializer (ModelSerializer):
    class Meta:
        model = OngoingCourse
        fields='__all__'

