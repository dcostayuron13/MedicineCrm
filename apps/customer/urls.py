from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = DefaultRouter()
router.register(r'register', CustomerViewSet,basename="register")

# simple_router = SimpleRouter()
# router.register(r'search', CustomerSearchView, basename='search_customer')


urlpatterns = [
    path('', include(router.urls)),
# path('', include(simple_router.urls)),
    ]