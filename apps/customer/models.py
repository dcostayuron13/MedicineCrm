from django.db import models
from apps.core.models import CustomUser
from apps.core.basemodel import Basemodel
from utils.choices import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from apps.core.manager import UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone
from django.core.validators import RegexValidator

landline_phone_regex = RegexValidator(
    regex=r"^\((0[2-9]|[2-9]\d)\)\s?\d{4}\s?\d{4}$|^(0[2-9]|[2-9]\d)\s?\d{8}$",
    message="Landline phone number must be in the format: (XX) XXXX XXXX or XX XXXX XXXX",
)

class Address(Basemodel):
    address1 = models.CharField(_("Address Line 1"), max_length=250, blank=True, null=True)
    address2 = models.CharField(_("Address Line 2"), max_length=250, blank=True, null=True)
    city = models.CharField(_("Town/City"), max_length=150, blank=True, null=True)
    postal_code = models.CharField(_("Postal Code"), max_length=150, blank=True, null=True)
    country = models.CharField(_("Country"), max_length=150, blank=True, null=True)
    # customer = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name= 'customer_address' ,null=True, blank=True)
    # appt_no = models.CharField(_("Appartment Number"), max_length=150, blank=True, null=True)
    # street_number = models.CharField(_("Street Number"), max_length=100, blank=True, null=True)
    # street_name =  models.CharField(_("Street Name"), max_length=150, blank=True, null=True)
    # suburb = models.CharField(_("Suburb"), max_length=150, blank=True, null=True)
    # state = models.CharField(_("State"), max_length=150, blank=True, null=True)
    # postal_code = models.CharField(_("Postal Code"), max_length=150, blank=True, null=True)
    # lat = models.CharField(_("Latitude"), max_length=150, blank=True, null=True)
    # long = models.CharField(_("Longitude"), max_length=150, blank=True, null=True)
    # country = models.CharField(_("Country"), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")
        ordering = ['-created_on']

    def __str__(self):
            return f"{self.address1}, {self.address2} {self.city} {self.country} {self.postal_code}"


    # def __str__(self):
    #         return f"{self.appt_no}, {self.street_number} {self.street_name} {self.suburb} {self.state} {self.postal_code} {self.country}"



# Create your models here.
class Customer( CustomUser):
    title = models.CharField(_("Title"), max_length=50, blank=True, null=True)
    # first_name = models.CharField(_("First name"), max_length=150, blank=True)
    # middle_name = models.CharField(_("Middle name"), max_length=150, blank=True)
    # last_name = models.CharField(_("Last name"), max_length=150, blank=True)

    landline_phone = models.CharField(
        _("Landline Phone: "),
        max_length=15,
        unique=True,
        error_messages={"unique": _("A user with that landline phone number already exists.")},
        validators=[landline_phone_regex],
    )

    # source = models.CharField(_("Source of Lead"), max_length=255, blank=True, null=True, choices=LEAD_SOURCE)
    dnc = models.BooleanField(_("Do Not Call"), default=False)

    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='customer_address', null=True,
                                 blank=True)

    remarks = models.TextField(_("Remark"), blank=True, null=True)

    user = UserManager()

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")
        ordering = ['-created_on']
