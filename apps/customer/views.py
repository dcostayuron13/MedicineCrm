from apps.core.utils.common import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import CostumerSerializer
from django.contrib.auth import get_user_model
from apps.core.models import CustomUser
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from .models import Customer

User = get_user_model()


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Customer.objects.all()
    serializer_class = CostumerSerializer


