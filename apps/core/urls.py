
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = DefaultRouter()
router.register(r'user', UserViewSet,basename="user")
router.register(r'login', LoginView)



simple_router = SimpleRouter()
simple_router.register(r'forgot_password', PasswordResetViewSet, basename='forgot_password')
simple_router.register(r'resend_otp', ResendOTPView, basename='resend_otp')
simple_router.register(r'2FA', OTPVerificationView, basename='2FA')
# simple_router.register(r'logout', LogoutView, basename='logout')
# router.register(r'logout', LogoutView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(simple_router.urls)),
    path('get_user/', get_user_data ),
    path('logout/', logout),
]
