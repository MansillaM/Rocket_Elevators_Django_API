from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ...models import Employees



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name', 'title', 'email', 'user_id', 'created_at', 'updated_at', 'facial_keypoints']