from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
 
@api_view(['GET', 'POST', 'PUT'])
#the index function can work for the mentiomd Get, Post and Put methods
def index(request):
    if request.method=="POST":
        courses={
            "course_name": "python",
            "courses_included": ["django", "fastapi", "mysql", "mongodb"],
            "course_provider":"Adex_International"
        }
        return Response(courses)

    elif request.method=="GET":
        print("You have hit the post method")
        return Response("hi")

    elif request.method=="PUT":
        print("put method enabled")
        return Response("hello from the put method")

        


