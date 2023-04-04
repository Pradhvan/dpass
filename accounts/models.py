from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    phone_number = PhoneNumberField(blank=True)
