from django.db import models
from apps.core.basemodel import Basemodel
from utils.choices import *
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Do not remove Commented out fields

class Comments(Basemodel):
    description = models.TextField(_("Description"), null=True, blank=True)
    # created_by = models.ForeignKey(User, _("Created By"), null=True, blank=True, on_delete=models.CASCADE)
    tag = models.TextField(_("Tags"), null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # related_to = models.ForeignKey(User,_("Related To"), null=True, blank = True, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ['-created_on']

    # def __str__(self):
    #     return   created_by


class Tickets(Basemodel):
 subject = models.CharField(_("Subject"), null= True, blank=True,max_length=100)
 description = models.TextField(_("Description"), null= True, blank=True)
 status = models.CharField(_("Status"),max_length=25, null= True, blank=True, choices= TICKET_STATUS)
 priority = models.CharField(_("Priority"),null=True, blank=True, max_length=25, choices=PRIORITY)
 type = models.CharField(_("Ticket Type"), null=True, blank=True, max_length=100)
 # created_by = models.ForeignKey(User, _("Created By"), null=True, blank=True, on_delete=models.CASCADE)
 # assigned_to = models.ForeignKey(User,_("Assigned To"), null=True, blank = True, on_delete=models.CASCADE)
 # raised_by = models.ForeignKey(User,_("Raised By"), null=True, blank = True, on_delete=models.CASCADE)
 comments = GenericRelation(Comments)

 class Meta:
     verbose_name = _("ticket")
     verbose_name_plural = _("tickets")
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


