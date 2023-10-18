import random
import string
from django.test import TestCase
from apps.core.models import CustomUser, OTP
from django.utils import timezone

class UserModelTest(TestCase):
    def generate_random_email(self):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(10)) + "@gmail.com"

    def generate_random_password(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

    def create_user(self, email=None, password=None):
        if email is None:
            email = self.generate_random_email()
        if password is None:
            password = self.generate_random_password()

        return CustomUser.objects.create_user(email=email, password=password)

    def create_superuser(self, email=None, password=None):
        if email is None:
            email = self.generate_random_email()
        if password is None:
            password = self.generate_random_password()


        superuser = CustomUser.objects.create_superuser(email=email, password=password)
        return superuser

    def test_create_user(self):
        user = self.create_user()

        self.assertIsNotNone(user.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        self.assertIsNotNone(user.check_password)

    def test_create_superuser(self):
        superuser = self.create_superuser()
        self.assertIsNotNone(superuser.email)
        self.assertTrue(superuser.is_active)
        self.assertFalse(superuser.is_admin)
        self.assertTrue(superuser.is_staff)
        self.assertIsNotNone(superuser.check_password)
