from django.core.mail import send_mail
import random
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from apps.core.models import OTP
from django.conf import settings


def generate_otp(user):
    try:
        otp_code = str(random.randint(10000, 99999))
        expires_at = timezone.now() + timezone.timedelta(minutes=15)
        otp = OTP(user=user, otp_code=otp_code, expires_at=expires_at)
        otp.save()
        return otp_code
    except Exception as e:
        raise Exception('Failed to generate OTP.')


def send_otp_via_email(user, otp_code):
    try:
        subject = 'Your OTP for Login'
        message = f'Your OTP(One Time Password) is: {otp_code}. Do not share it with anyone.'
        from_email = settings.EMAIL_HOST_USER  # Replace with your email
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False,)
        return Response({'message': 'OTP sent successfully. Check your mail.'}, status=status.HTTP_200_OK)
    except Exception as e:
        raise Exception('Failed to send OTP email.')


def verify_otp(user, otp_value):
    try:
        expired_otps = OTP.objects.filter(user=user, expires_at__lt=timezone.now())

        for expired_otp in expired_otps:
            if expired_otp.otp_code == otp_value:
                return False  # Invalid otp

        otp = OTP.objects.get(user=user, otp_code=otp_value, expires_at__gte=timezone.now())
        # otp.delete()  # Delete the OTP after successful verification
        return True
    except OTP.DoesNotExist:
        return False

def delete_expired_otps():
    # Delete all expired OTPs
    expired_otps = OTP.objects.filter(expires_at__lt=timezone.now())
    expired_otps.delete()