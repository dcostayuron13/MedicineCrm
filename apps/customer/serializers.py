from rest_framework import serializers
from .models import Customer, Address
from datetime import datetime
import random
from django.contrib.auth import authenticate, get_user_model
from utils.dynamicfields import DynamicFieldsModelSerializer


User = get_user_model()

class AddressSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Address
        fields = ['address1', 'city', 'postal_code',  'country']


class CostumerSerializer(DynamicFieldsModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only= True)
    address = AddressSerializer()  #many=True) #read only
    class Meta:
        model = Customer
        fields = ('id', 'title', 'first_name','middle_name', 'last_name','email', 'phone', 'landline_phone', 'address', 'remarks','dnc')
        # extra_kwargs = {'password': {'write_only': True}}

        # def validate(self, data):
        #     # Ensure that the passwords match
        #     if data['password'] != data['password2']:
        #         raise serializers.ValidationError({'password': 'Passwords must match.'})
        #     return data

    def create(self, validated_data):
            address_data = validated_data.pop('address')

            address, created = Address.objects.get_or_create(**address_data)

            customer = Customer.objects.create(address=address, **validated_data)
            return customer


# class CustomerSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ('id', 'first_name', 'last_name', 'phone', 'postal_code')