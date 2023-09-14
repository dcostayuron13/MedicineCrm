from rest_framework import serializers
from .models import CustomUser
from datetime import datetime
import random
from django.contrib.auth import authenticate, get_user_model
from .models import OTP

User = get_user_model()


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields =['otp_code', 'created_at', 'expires_at']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6, min_length=6)
    new_password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})


class ResendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only= True)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'phone', 'password', 'password2', 'first_name', 'last_name', 'role', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Custom create method to hash the password before creating the user.
        """
        # Extract the password from the validated data
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords much match.'})

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    # def save(self):
    #     uaer = CustomUser(
    #         email = self.validated_data['email'],
    #         username = self.validated_data['email'],
    #     )
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']
    #
    #     if password!= password2:
    #         raise serializers.ValidationError({'password': 'Passwords much match.'})




