from django.db import models
from apps.core.basemodel import Basemodel
from apps.customer.models import Customer
from apps.inventory.models import Inventory
from apps.employee.models import Employee
from utils.choices import *

from django.utils.translation import gettext_lazy as _


# Create your models here.
# class Order(Basemodel):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     inventory = models.ManyToManyField(Inventory, )
#     date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')
#     total_amount = models.DecimalField(max_digits=8, decimal_places=2)


class Order(Basemodel):
    id = models.CharField(max_length=10, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agent = models.ForeignKey(Employee, verbose_name=_("Agent"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="agent",)
    inventory = models.ManyToManyField(Inventory, verbose_name=_("Product Name"))
    order_quantity = models.CharField(_("Order Quantity"), max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending', verbose_name=_("Status"))
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Total Amount"))
    remarks = models.TextField(_("Remark"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            last_order = Order.objects.order_by('-id').first()
            if last_order:
                last_id = int(last_order.id.split('-')[1])
            else:
                last_id = 0
            self.id = f'ORD-{str(last_id + 1).zfill(4)}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ['-created_on']





class Payment(Basemodel):
    # order = models.ForeignKey(Orders,_("Order"), null=True, blank = True, on_delete=models.CASCADE)
     ammount = models.CharField(_("Ammount"), null= True, blank=True,max_length=100)
     description = models.TextField(_("Description"), null= True, blank=True)
     method = models.CharField(_("Payment Method"),max_length=25, null= True, blank=True, choices= PAYMENT_METHOD)
     status = models.CharField(_("Payment Status"),null=True, blank=True, max_length=25, choices=PAYMENT_STATUS)

    # transaction_id = models.CharField(_("Transaction ID"), null=True, blank=True, max_length=100)
    # payment_gateway = models.CharField(_("Payment Gateway"), null=True, blank=True, max_length=100)

     class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
        ordering = ['-created_on']


class Quotes(Basemodel):
    quote_id = models.CharField(max_length=10, unique=True, editable=False)
    # order = models.ForeignKey(Customer,_("Customer Name"), null=True, blank = True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, blank = True, on_delete=models.CASCADE)
    # total = models.ForeignKey(Order, null=True, blank = True, on_delete=models.CASCADE)
    # admin = models.CharField(_("Payment Method"),max_length=25, null= True, blank=True, choices= PAYMENT_METHOD)
    status = models.CharField(_("Quote Status"),null=True, blank=True, max_length=25, choices=PAYMENT_STATUS)

    class Meta:
        verbose_name = _("Quote")
        verbose_name_plural = _("Quotes")
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        if not self.quote_id:
            last_quote = Quote.objects.last()
            if last_quote:
                last_id = int(last_quote.quote_id[3:]) + 1
            else:
                last_id = 1
            self.quote_id = f'QUO{str(last_id).zfill(4)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.quote_id

