from django.db import models
from apps.core.models import CustomUser
from apps.core.basemodel import Basemodel
from utils.choices import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from apps.core.manager import UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone


class Address(Basemodel):
    # customer = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name= 'customer_address' ,null=True, blank=True)
    appt_no = models.CharField(_("Appartment Number"), max_length=150, blank=True, null=True)
    street_number = models.CharField(_("Street Number"), max_length=100, blank=True, null=True)
    street_name =  models.CharField(_("Street Name"), max_length=150, blank=True, null=True)
    suburb = models.CharField(_("Suburb"), max_length=150, blank=True, null=True)
    state = models.CharField(_("State"), max_length=150, blank=True, null=True)
    postal_code = models.CharField(_("Postal Code"), max_length=150, blank=True, null=True)
    lat = models.CharField(_("Latitude"), max_length=150, blank=True, null=True)
    long = models.CharField(_("Longitude"), max_length=150, blank=True, null=True)
    country = models.CharField(_("Country"), max_length=150, default="Australia")

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")
        ordering = ['-created_on']

    def __str__(self):
            return f"{self.appt_no}, {self.street_number} {self.street_name} {self.suburb} {self.state} {self.postal_code} {self.country}"



# Create your models here.
class Customer( CustomUser):
    source = models.CharField(_("Source of Lead"), max_length=255, blank=True, null=True, choices=LEAD_SOURCE)
    dnc = models.BooleanField(_("Do Not Call"), default=False)
    description = models.TextField(_("Description"), blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='customer_address', null=True,
                                 blank=True)

    user = UserManager()

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")
        ordering = ['-created_on']


