from django.shortcuts import render

from rest_framework import viewsets

from todo.api.rest.serializers import TaskSerializer
from todo.models import Task

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer