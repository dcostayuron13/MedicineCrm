# from rest_framework import serializers
# from apps.employee.models import Employee
# from datetime import datetime
# import random
# from django.contrib.auth import authenticate, get_user_model
# from .models import OTP
# from utils.dynamicfields import DynamicFieldsModelSerializer
#
# User = get_user_model()
#
#
# # class OTPSerializer(DynamicFieldsModelSerializer):
# #     class Meta:
# #         model = OTP
# #         fields =['otp_code', 'created_at', 'expires_at']
# #
# #
# # class LoginSerializer(DynamicFieldsModelSerializer):
# #     email = serializers.EmailField()
# #     password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
# #
# #     class Meta:
# #         model = CustomUser
# #         fields = ('email', 'password')
# #
# #
# # class OTPVerificationSerializer(DynamicFieldsModelSerializer):
# #     email = serializers.EmailField()
# #     otp = serializers.CharField(max_length=6)
# #
# #     class Meta:
# #         model = CustomUser
# #         fields = ('email', 'otp')
# #
# # class PasswordResetSerializer(DynamicFieldsModelSerializer):
# #     email = serializers.EmailField()
# #     otp = serializers.CharField(max_length=6, min_length=6)
# #     new_password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
# #     confirm_password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
# #
# #
# # class ResendOTPSerializer(DynamicFieldsModelSerializer):
# #     email = serializers.EmailField()
#
#
# class UserSerializer(DynamicFieldsModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only= True)
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'fname', 'lname', 'email', 'phone', 'role', 'password', 'password2', 'reporting_to')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         """
#         Custom create method to hash the password before creating the user.
#         """
#         # Extract the password from the validated data
#         password = validated_data.pop('password')
#         password2 = validated_data.pop('password2')
#
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords much match.'})
#
#         user = User.objects.create(**validated_data)
#         user.set_password(password)
#         user.save()
#         print(user.password)
#         return user
#
#
#
#
#
