from Home.views import *
from django.urls import path, include
from Home.views import PeopleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('people/', PeopleViewSet, basename='people')



#here the pattern is what you want to keep after api/ and the viewset classname in views.py, may or may not include basename, its optional 
urlpatterns= router.urls

urlpatterns = [
    #this is the way viewset are given the configurations
    path('', include(router.urls)),
    path('register/', register.as_view()),
    path('login/', login.as_view()),
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('ColorAp/', Colorapi.as_view()),    
    path('PeopleAp/', PeopleApi.as_view()),
# this is the standard form of routing the viewclass api, you have to use "classname.as_view()"in every function call section
    
]
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
