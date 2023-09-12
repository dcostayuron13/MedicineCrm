from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class Basemodel(models.Model):
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    created_on = models.DateTimeField(_("Created On"), default=timezone.now)
    modified_on = models.DateTimeField(_("Modified On"), default=timezone.now)

    class Meta:
        abstract = True