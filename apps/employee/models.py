from django.db import models
from apps.core.models import CustomUser
from apps.core.basemodel import Basemodel
from utils.choices import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from apps.core.manager import UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone


# Create your models here.
class Employee(CustomUser):
    role = models.CharField(_("Role"), max_length=50, choices=USER_ROLES)
    # role = models.OneToOneField(_("Role"), max_length=50, choices=USER_ROLES)
    reporting_to = models.ForeignKey(
        "self",
        verbose_name=_("Reporting to"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="reportees",
    )


    user = UserManager()

    class Meta:
        verbose_name = _("employee")
        verbose_name_plural = _("employees")
        ordering = ['-created_on']

