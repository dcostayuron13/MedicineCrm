# from rest_framework import serializers
# from .models import Customer, Address
# from datetime import datetime
# import random
# from django.contrib.auth import authenticate, get_user_model
# from utils.dynamicfields import DynamicFieldsModelSerializer
#
#
# User = get_user_model()
#
#
# class EmployeeSerializer(DynamicFieldsModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only= True)
#     # address = AddressSerializer()
#     class Meta:
#         model = Employee
#         fields = ('email', 'username', 'phone', 'password', 'password2','title', 'first_name', 'last_name', 'role', 'dnc' ,'is_staff', 'address')
#         extra_kwargs = {'password': {'write_only': True}}
#
#         def validate(self, data):
#             # Ensure that the passwords match
#             if data['password'] != data['password2']:
#                 raise serializers.ValidationError({'password': 'Passwords must match.'})
#             return data
#
#         def create(self, validated_data):
#
#             validated_data.pop('password2', None)
#             address_data = validated_data.pop('address')
#
#             customer = Customer.objects.create(**validated_data)
#
#             address, created = Address.objects.get_or_create(**address_data)
#             customer.address = address
#             customer.set_password(validated_data['password'])
#             customer.save()
#             return customer
