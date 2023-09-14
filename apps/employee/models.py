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
    position = models.CharField(_("Position"), max_length=50,blank=True, null=True)
    joined_on = models.DateTimeField(_("Created On"), default=timezone.now)
    dept = models.CharField(_("Department"), max_length=50, blank=True, null=True)
    reporting_to = models.CharField(_("Reporting To"), max_length=100, blank=True, null=True)

    user = UserManager()

    class Meta:
        verbose_name = _("employee")
        verbose_name_plural = _("employees")
        ordering = ['-created_on']

