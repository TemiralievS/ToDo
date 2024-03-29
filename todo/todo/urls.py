"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todoapp.views import ToDoViewSet, ProjectViewSet
from userapp.views import UserViewSet
from rest_framework.authtoken import views
from graphene_django.views import GraphQLView
from userappV2.views import UserListAPIView
from django.contrib.auth import get_user_model
User = get_user_model()

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('todos', ToDoViewSet)
router.register('projects', ProjectViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="TODO",
        default_version='0.2',
        description="Documentation to ToDo project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),

    path("graphql/", GraphQLView.as_view(graphiql=True)),

    path('api/<str:version>/users/', UserListAPIView.as_view()),
    # path('api/users/0.1', include('userapp.urls', namespace='0.1')),
    # path('api/users/0.2', include('userapp.urls', namespace='0.2')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


