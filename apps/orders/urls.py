from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = DefaultRouter()
router.register(r'add_order', OrderViewSet,basename="add_order")


urlpatterns = [
    path('', include(router.urls)),
# path('', include(simple_router.urls)),
    ]