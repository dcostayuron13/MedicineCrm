from rest_framework import serializers
from .models import Order
from apps.customer.serializers import CustomerSerializer
from utils.choices import ORDER_STATUS_CHOICES
from utils.dynamicfields import DynamicFieldsModelSerializer



class OrderSerializer(DynamicFieldsModelSerializer):
    customer = CustomerSerializer()
    status = serializers.ChoiceField(choices=ORDER_STATUS_CHOICES)
    date = serializers.DateTimeField(read_only=True)



    class Meta:
        model = Order
        fields = ['id', 'customer', 'date', 'status', 'total_amount']
        read_only_fields = ['date']