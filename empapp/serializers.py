from rest_framework import serializers
from empapp.models import EmpModel,Task
from django.contrib.auth.models import User

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmpModel
        fields="__all__"
        read_only_fields=["joining_date","owner"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

