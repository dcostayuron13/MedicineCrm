from rest_framework import serializers
from apps.employee.models import Employee
from apps.core.models import OTP
from utils.dynamicfields import DynamicFieldsModelSerializer

class OTPSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = OTP
        fields =['otp_code', 'expires_at']


class LoginSerializer(DynamicFieldsModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = Employee
        fields = ('email', 'password')


class OTPVerificationSerializer(DynamicFieldsModelSerializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    class Meta:
        model = Employee
        fields = ('email', 'otp')



class ConfirmPasswordSerializer(DynamicFieldsModelSerializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6, min_length=4)
    new_password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = Employee
        fields = ('email','otp', 'new_password', 'confirm_password')



class SendOTPSerializer(DynamicFieldsModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Employee
        fields = ('email',)

class EmployeeSerializer(DynamicFieldsModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only= True)
    # address = AddressSerializer()
    class Meta:
        model = Employee
        fields = ('id', 'role', 'reporting_to', 'first_name', 'last_name','email', 'phone', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Ensure that the passwords match
        request = self.context.get('request')
        if request and request.method == "POST":
            if data['password'] != data['password2']: #and request.method == "POST":
                raise serializers.ValidationError({'password': 'Passwords must match.'})
        return data

    def create(self, validated_data):

        validated_data.pop('password2', None)

        employee = Employee.objects.create(**validated_data)
        employee.set_password(validated_data['password'])
        employee.save()
        return employee
