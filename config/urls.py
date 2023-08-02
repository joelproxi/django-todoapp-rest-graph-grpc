
from django.contrib import admin
from django.urls import path, include

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/rest/', include('todo.api.rest.urls')),
    path("api/v1/graphql/", GraphQLView.as_view(graphiql=True)),
]
