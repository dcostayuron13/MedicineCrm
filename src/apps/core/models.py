from django.db import models
from .basemodel import Basemodel
from utils.choices import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .manager import  *
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone

class CustomUser(AbstractBaseUser, Basemodel, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()
    unique_error_message = _("A user with that {} already exists.")

    username = models.CharField(
        _("username"),
        max_length=150,
               help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages={"unique": unique_error_message.format("username")},
    )

    title = models.CharField(_("Title"), max_length=50, blank=True, null=True)
    first_name = models.CharField(_("First name"), max_length=150, blank=True)
    last_name = models.CharField(_("Last name"), max_length=150, blank=True)
    email = models.EmailField(
        _("Email address"),
        unique=True,
        error_messages={"unique": unique_error_message.format("email address")},
    )

    phone = models.CharField(_("Phone: "), max_length=20, unique=True,
        error_messages={
            "unique": _("A user with that contact number already exists."),
        },)

    dob = models.DateField(_("Date of Birth"), blank=True, null=True)

    role = models.CharField(_("Role"), max_length=50, choices=USER_ROLES)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_admin = models.BooleanField(_('Admin User'), default=False,
                                   help_text=_('Designates whether this user should be treated as admin user. '), )


    objects = UserManager()

    # EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")









# class MedicalHistory(Basemodel):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_address')
#     disease = models.CharField(_("Disease"), max_length=100, blank=True, null=True)
#     allergies = models.CharField(_("Allergies"), max_length=250, blank=True, null=True)
#     description = models.TextField(_("Description"), blank=True, null=True)
#     family_history
#     symptoms
#
#     class Meta:
#         verbose_name = _("Medical remark")
#         verbose_name_plural = _("Medical remarks")
#         ordering = ['-created_on']






