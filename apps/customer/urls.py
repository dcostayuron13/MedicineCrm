from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = DefaultRouter()
router.register(r'user', CustomerViewSet,basename="user")

urlpatterns = [
    path('', include(router.urls)),
    ]