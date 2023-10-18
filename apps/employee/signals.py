from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Employee

@receiver(post_save, sender=Employee)
def create_employee_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)