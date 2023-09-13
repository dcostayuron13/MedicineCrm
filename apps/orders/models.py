from django.db import models
from apps.core.basemodel import Basemodel
from apps.customer.models import Customer
from apps.inventory.models import Inventory
from utils.choices import ORDER_STATUS_CHOICES


# Create your models here.
class Order(Basemodel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    inventory = models.ManyToManyField(Inventory, )
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)


