from django.shortcuts import render

from .serializers import InventorySerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Inventory



class InventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer