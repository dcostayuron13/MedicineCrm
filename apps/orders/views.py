from django.shortcuts import render

# Create your views here.
from apps.core.utils.common import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from .models import Order

User = get_user_model()


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer