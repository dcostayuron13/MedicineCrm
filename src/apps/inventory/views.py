from django.shortcuts import render
from rest_framework import generics
from .models import Category, Inventory
from .serializers import  CategorySerializer, InventorySerializer


class ListCategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListInventoryView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class DeleteProductView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Inventory.objects.all()