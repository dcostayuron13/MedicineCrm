from apps.core.utils.common import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer, LoginSerializer, ConfirmPasswordSerializer,  SendOTPSerializer, OTPVerificationSerializer
from django.contrib.auth import get_user_model, login
from .models import Employee
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from .permissions import IsAdminOrSuperAdmin



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrSuperAdmin]


class LoginView(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = Employee.objects.all()

    def create(self, request):  #create
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')
            except ObjectDoesNotExist:
                return Response({'message': 'User does not exist. Please register now!'}, status=status.HTTP_404_NOT_FOUND)

            delete_expired_otps()

            user = Employee.objects.filter(email=email).first()

            if not user:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            if user.check_password(password):
                otp_code = generate_otp(user)
                send_otp_via_email(user, otp_code)
                return Response({'message': 'OTP sent successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(viewsets.ModelViewSet):
    serializer_class = SendOTPSerializer
    queryset = Employee.objects.all()

    def create(self, request):  #create
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                email = serializer.validated_data.get('email')
            except ObjectDoesNotExist:
                return Response({'message': 'User does not exist. Please register now!'}, status=status.HTTP_404_NOT_FOUND)

            delete_expired_otps()

            user = Employee.objects.filter(email=email).first()

            if not user:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


            otp_code = generate_otp(user)
            send_otp_via_email(user, otp_code)
            return Response({'message': 'OTP sent successfully!'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OTPVerificationView(viewsets.ViewSet):
    serializer_class = OTPVerificationSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                email = serializer.validated_data.get('email')
                otp_code = serializer.validated_data.get('otp')
            except ObjectDoesNotExist:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            user = Employee.objects.filter(email=email).first()

            if user is not None:
                if verify_otp(user, otp_code):
                    token, created = Token.objects.get_or_create(user=user)

                    # login

                    return Response({'message': 'Login successful.', 'token': token.key}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'ID': user.id,
            'Username': user.username,
            'Email': user.email,
            'Phone': user.phone
        })

    return Response({'error': 'Not Authenticated!'}, status=400)


class ConfirmPasswordViewSet(viewsets.ViewSet):
    serializer_class = ConfirmPasswordSerializer
    # basename = 'forgot_password'

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                email = serializer.validated_data['email']
                otp = serializer.validated_data['otp']
                new_password = serializer.validated_data['new_password']
                confirm_password = serializer.validated_data['confirm_password']

                user = Employee.objects.get(email=email)


            except ObjectDoesNotExist:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            otp_code = generate_otp(user)

            if not verify_otp(user, otp):
                return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

            if new_password != confirm_password:
                return Response({'message': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user.set_password(new_password)
                user.save()
            except Exception as e:
                return Response({'message': 'Password change failed: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResendOTPView(viewsets.ViewSet):
    serializer_class = SendOTPSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                email = request.data.get('email')

                try:
                    user = Employee.objects.get(email=email)
                except User.DoesNotExist:
                    return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            except ObjectDoesNotExist:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            try:
                existing_otp = OTP.objects.get(user=user)
                existing_otp.delete()
            except OTP.DoesNotExist:
                pass

            # Generate a new OTP each time the user requests it
            otp_code = generate_otp(user)
            send_otp_via_email(user, otp_code)

            return Response({'message': 'New OTP sent successfully!'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LogoutView(viewsets.ViewSet):
#
# # def logout(request):
# #
# #     Token.objects.get(user=request.user).delete()
# #     return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         token = request.user.auth_token
#
#         if token is not None:
#             token_obj = Token.objects.get(key=token)
#             token_obj.delete()
#             return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'No token found.'}, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token_obj = Token.objects.filter(user=request.user)
            token_obj.delete()
            return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'No token found.'}, status=status.HTTP_400_BAD_REQUEST)
