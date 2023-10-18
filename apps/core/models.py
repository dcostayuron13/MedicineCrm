from django.db import models
from .basemodel import Basemodel
from utils.choices import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .manager import  *
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone

# For token auth
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.core.validators import RegexValidator

mobile_phone_regex = RegexValidator(
    regex=r"^\d{10}$",
    message="Mobile phone number must be 10 digits.",
)

class CustomUser(AbstractBaseUser, Basemodel, PermissionsMixin):
    # username_validator = ASCIIUsernameValidator()
    unique_error_message = _("A user with that {} already exists.")

    first_name = models.CharField(_("First name"), max_length=150, blank=True)
    middle_name = models.CharField(_("Middle name"), max_length=150, blank=True)
    last_name = models.CharField(_("Last name"), max_length=150, blank=True)

    # username = models.CharField(
    #     _("username"),
    #     max_length=150,
    #            help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
    #     error_messages={"unique": unique_error_message.format("username")},
    # )

    email = models.EmailField(
        _("Email address"),
        unique=True,
        error_messages={"unique": unique_error_message.format("email address")},
    )

    phone = models.CharField(
        _("Mobile Phone: "),
        max_length=15,
        unique=True,
        error_messages={"unique": _("A user with that mobile phone number already exists.")},
        validators=[mobile_phone_regex],
    )

    # role = models.CharField(_("Role"), max_length=50, choices=USER_ROLES)



    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_admin = models.BooleanField(_('Admin User'), default=False,
                                   help_text=_('Designates whether this user should be treated as admin user. '), )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created= False, **kwargs):
    if created:
        Token.objects.create(user = instance)


class OTP(Basemodel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    otp_code = models.CharField(max_length=6)
    # created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(timezone.timedelta(minutes=5))

    def is_expired(self):
        return self.expires_at < timezone.now()









