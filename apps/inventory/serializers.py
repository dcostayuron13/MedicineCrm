from rest_framework import serializers
from apps.inventory.models import Inventory
from utils.dynamicfields import DynamicFieldsModelSerializer


# class CategorySerializer(serializers.ModelSerializer,):
#     class Meta:
#         model = Category
#         fields = '__all__'

class InventorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Inventory
        fields = [
             'product_name',   'price',   'category',
            'instock_quantity',

        ]

# class InventorySerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#
#     class Meta:
#         model = Inventory
#         fields = ['id', 'product', 'quantity', 'received_quantity', 'sold_quantity','name', 'product_id', 'description', 'category','price', 'manufacturer']