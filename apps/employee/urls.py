from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *
from apps.employee.views import *

router = DefaultRouter()
router.register(r'register', EmployeeViewSet,basename="register")
router.register(r'login', LoginView)



simple_router = SimpleRouter()
simple_router.register(r'forgot_password', ForgotPasswordView, basename='forgot_password')
simple_router.register(r'confirm_password', ConfirmPasswordViewSet, basename='confirm_password')
simple_router.register(r'resend_otp', ResendOTPView, basename='resend_otp')
simple_router.register(r'verify_otp', OTPVerificationView, basename='verify_otp')
# simple_router.register(r'logout', LogoutView, basename='logout')
# router.register(r'logout', LogoutView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(simple_router.urls)),
    path('get_user/', get_user_data ),
path('logout/', LogoutView.as_view({'post': 'post'}), name='logout')
    # path('logout/', logout),
]