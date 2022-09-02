"""Rocket_Elevators_Django_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import reset
import os 
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view, permission_classes, action
import face_recognition
from rest_framework import permissions
from PIL import Image
import numpy as np
from django.http import JsonResponse
from rest_framework import status
import sys
sys.path.append("..")
from models import Employees
    
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

###### EMPLOYEE ######

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name', 'title', 'email', 'user_id', 'created_at', 'updated_at', 'facial_keypoints']

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getEmployee(request):
    file = face_recognition.load_image_file(request.data['file'])
    numpy_photo = file
    encode_photo = face_recognition.face_encodings(numpy_photo)[0]
    employees = Employees.objects.all().exclude(facial_keypoints = None)
    for i in employees:
        employee_photo = np.array(i.facial_keypoints)
        results = face_recognition.compare_faces([employee_photo], encode_photo)
        if True in results:
            employee =  Employees.objects.get(pk = i.id)
            serializer = EmployeesSerializer(employee)
            output = JsonResponse(serializer.data, safe=False)
            return output
    return JsonResponse(status=404, data={'status':'false','message':"Not employee"})

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'employees', EmployeesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getEmployee/', getEmployee)
]


