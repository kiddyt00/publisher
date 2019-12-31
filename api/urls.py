# coding=utf8
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rest_views
from . import views

app_name = 'api'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'apps', views.AppViewSet, basename="app")
router.register(r'deploypools', views.DeployPoolViewSet, basename="deploypool")
router.register(r'servers', views.ServerViewSet, basename="server")

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', rest_views.obtain_auth_token),
]