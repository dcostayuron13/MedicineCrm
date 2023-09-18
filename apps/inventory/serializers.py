from rest_framework import serializers
from .models import Category,Inventory
from utils.dynamicfields import DynamicFieldsModelSerializer



class CategorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InventorySerializer(DynamicFieldsModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'quantity', 'received_quantity', 'sold_quantity','name', 'product_id', 'description', 'category','price', 'manufacturer']