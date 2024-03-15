from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PeopleSerializer
from .models import People
from rest_framework import status

# Create your views here.
 
@api_view(['GET', 'POST', 'PUT'])
#the index function can work for the mentiomd Get, Post and Put methods
def index(request):
    if request.method=="GET":
        print(request.GET.get('search'))
        courses={
            "course_name": "python",
            "courses_included": ["django", "fastapi", "mysql", "mongodb"],
            "course_provider":"Adex_International"
        }
        return Response(courses)
        
    elif request.method=="POST":
        print("You have hit the post method")
        data=request.data
        print(data)
        print(data.get("name"))
        print(data["religion"])

        return Response("You have hit the post method")

    elif request.method=="PUT":
        print("put method enabled")
        return Response("hello from the put method")

        
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method=="GET":
        obj=People.objects.all()
        #use of serializer
        seri=PeopleSerializer(obj, many=True)
        #if has to get single data then no need to use many=True, else have to
        return Response(seri.data)
    #.data should be used to send the response
    
    elif request.method=="POST":
        data=request.data
        serializer=PeopleSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)

            # return Response("Added successfully to the database", status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #serializer.errors throws the errors message if the user is sending the random data not defined in serializer class
    elif request.method=="PUT":
        data=request.data
        print(data["id"])
        try:
            obj=People.objects.get(id=data["id"])
            print(obj)

            serializer=PeopleSerializer(obj,data=data)
            if serializer.is_valid():
                serializer.save()   
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("object not found", status=status.HTTP_404_NOT_FOUND)
        
    elif request.method=="PATCH":
        data=request.data
        try:
            obj=People.objects.get(id=data["id"])
            #in patch has to set partial =True
            serializer=PeopleSerializer(obj,data=data, partial=True)
            if serializer.is_valid():
                serializer.save()   
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("object not found", status=status.HTTP_404_NOT_FOUND)
     
    
    elif request.method=="DELETE":
        try:
            data = request.data
            obj = People.objects.get(id=data["id"])
            obj.delete()
            return Response({"message": "obj deleted"}, status=status.HTTP_200_OK)
        except People.DoesNotExist:
            print("Object not found")
            return Response({"message": "obj not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("Error:", e)
            return Response({"message": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
