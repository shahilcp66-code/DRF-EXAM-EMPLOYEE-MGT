from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from empapp.serializers import EmpSerializer,TaskSerializer,UserSerializer
from empapp.models import EmpModel,Task
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Create your views here.


class EmployeeCreateList(CreateAPIView,ListAPIView):
    serializer_class=EmpSerializer
    queryset=EmpModel.objects.all()

class EmployeeRetrieveUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=EmpSerializer
    queryset=EmpModel.objects.all()

class TaskCreateList(CreateAPIView,ListAPIView):
    serializer_class=TaskSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=Task.objects.all()
    filter_backends=[
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    ]
    filterset_fields=["status"]
    ordering_fields=["joining_date","due_date"]


class TaskRetrieveUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=TaskSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=Task.objects.all()


class PendingTask(ListAPIView):
    serializer_class=TaskSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.kwargs['id'],status="Pending")







