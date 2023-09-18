from rest_framework import serializers

from utils.dynamicfields import DynamicFieldsModelSerializer
from .models import Customer, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'appt_no', 'street_number', 'street_name', 'suburb', 'state', 'postal_code', 'country']


class CustomerSerializer(DynamicFieldsModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'title', 'landline_phone', 'dnc', 'address']