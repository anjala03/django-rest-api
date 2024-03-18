from Home.views import *
from django.urls import path


urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('ColorAp/', Colorapi.as_view()),    
    path('PeopleAp/', PeopleApi.as_view()),
# this is the standaed form of routing the viewclass api, ypu have to use "classname.as_view()"in every function call section


    
]
