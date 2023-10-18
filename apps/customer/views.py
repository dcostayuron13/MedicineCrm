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


# class CustomerSearchView(viewsets.ViewSet):
#     serializer_class = CostumerSerializer  # Use your Customer serializer
#
#     def list(self, request):
#         id = request.query_params.get('id', None)
#         first_name = request.query_params.get('first_name', None)
#         last_name = request.query_params.get('last_name', None)
#         phone = request.query_params.get('phone', None)
#         postal_code = request.query_params.get('postal_code', None)
#
#         print(id)
#         print(first_name)
#
#         # Create a filter dictionary to build the query dynamically
#         filters = {}
#
#         if id:
#             filters['id__icontains'] = id
#
#         if first_name:
#             filters['first_name__icontains'] = first_name
#
#         if last_name:
#             filters['last_name__icontains'] = last_name
#
#         if phone:
#             filters['phone__icontains'] = phone
#
#         if postal_code:
#             filters['address__postal_code__icontains'] = postal_code
#
#         # Apply filters to the Customer queryset
#         customers = Customer.objects.filter(**filters)
#
#         serializer = self.serializer_class(customers, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class CustomerSearchView(viewsets.ViewSet):
#     serializer_class = CostumerSerializer  # Use your Customer serializer
#
#     def list(self, request):
#
#         id = request.query_params.get('id', None)
#         first_name = request.query_params.get('first_name', None)
#         last_name = request.query_params.get('last_name', None)
#
#         phone = request.query_params.get('phone', None)
#         postal_code = request.query_params.get('postal_code', None)
#
#         # Filter customers based on the provided query parameters
#         customers = Customer.objects.all()
#
#         if id:
#             customers = customers.filter(id__icontains=id)
#
#         if first_name:
#             customers = customers.filter(first_name__icontains=first_name)
#         if last_name:
#             customers = customers.filter(last_name__icontains=last_name)
#         if postal_code:
#             customers = customers.filter(postal_code__icontains=first_name)
#         if phone:
#             customers = customers.filter(phone__icontains=phone)
#
#         serializer = self.serializer_class(customers, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


