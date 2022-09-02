from http.client import HTTPResponse
import json
from lib2to3.pgen2.parse import ParseError
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, action
import face_recognition
from serializers import UserSerializer, GroupSerializer, EmployeesSerializer
from ...models import Employees
from PIL import Image
import numpy as np
from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Employees.objects.all().order_by('-id')
    serializer_class = EmployeesSerializer

    @action(methods=['post'])
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        employee = Employees.objects.create(image=file)
        return HTTPResponse(json.dumps({'message': "Uploaded"}), status=200)

    @action(methods=['get'])
    def getEmployee(request):
        print('------------')
        file = Image.open(request.data['file'])
        print('heeereeee')
        numpy_photo = np.array(file)
        encode_photo = face_recognition.face_encodings(numpy_photo)[0]
        employees = Employees.objects.all()
        for i in employees:
            employee_photo = np.array(i.facial_keypoints)
        if (face_recognition.compare_faces([encode_photo], employee_photo)):
            employee =  Employees.objects.get(pk = i.id)
            serializer = EmployeesSerializer(employee)
            output = JsonResponse(serializer.data, safe=False)
            return output
        else :
            return JsonResponse(status=404, data={'status':'false','message':"Not employee"})
