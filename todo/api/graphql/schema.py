import graphene

from todo.api.graphql.types import TaskType
from todo.models import Task


class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)
    task_by_id = graphene.Field(TaskType, id=graphene.Int())
    
    def resolve_all_tasks(root, info):
        return Task.objects.all()
    
    def resolve_task_by_id(root, info, id):
        return Task.objects.get(pk=id)
    
   
   
class CreateTaskMudation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        is_completed = graphene.Boolean() 
    
    task = graphene.Field(TaskType)
    
    @classmethod
    def mutate(cls, root, info, name):
        task = Task(name=name)
        task.save()
        return CreateTaskMudation(task=task)


class UpdateTaskMudation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        is_completed = graphene.Boolean() 
        id = graphene.ID()
        
    task = graphene.Field(TaskType)
    
    @classmethod
    def mutate(cls, root, info, name, is_completed, id):
        task = Task.objects.get(pk=id)
        task.name = name
        task.is_completed = is_completed
        task.save()
        return UpdateTaskMudation(task=task)
   
   
class DeleteTaskMudation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        
    task = graphene.Field(TaskType)
    
    @classmethod
    def mutate(cls, root, info, id):
        task = Task.objects.get(pk=id)
        task.delete()
        return DeleteTaskMudation()
     

class Mutation(graphene.ObjectType):
    create_task = CreateTaskMudation.Field()
    update_task = UpdateTaskMudation.Field()
    delete_task = DeleteTaskMudation.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)