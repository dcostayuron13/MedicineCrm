from rest_framework import serializers
from .models import Category,Inventory



class CategorySerializer(serializers.ModelSerializer,):
    class Meta:
        model = Category
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'quantity', 'received_quantity', 'sold_quantity','name', 'product_id', 'description', 'category','price', 'manufacturer']