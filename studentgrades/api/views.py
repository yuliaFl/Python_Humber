from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def all_students(request):
    routes = {
        'GET /api/students/'
    }
    return Response(routes)
