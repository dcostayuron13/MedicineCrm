from rest_framework import serializers
from .models import Order, Quotes
# from apps.customer.serializers import CustomerSerializer
from utils.choices import ORDER_STATUS_CHOICES
from utils.dynamicfields import DynamicFieldsModelSerializer
from apps.customer.serializers import CostumerSerializer

class OrderSerializer(DynamicFieldsModelSerializer):
    # customer = CustomerSerializer()
    status = serializers.ChoiceField(choices=ORDER_STATUS_CHOICES)
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'date', 'status', 'total_amount']
        read_only_fields = ['date']


# class QuotesSerializer(DynamicFieldsModelSerializer):
#     customer = CostumerSerializer()  #many=True) #read only
#     class Meta:
#         model = Quotes
#         fields = ('id', 'created_on', 'customer', 'password', 'password2','title', 'first_name', 'last_name', 'role', 'dnc' ,'is_staff', 'address')

