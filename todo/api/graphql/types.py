from graphene_django import DjangoObjectType

from todo.models import Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'
        
