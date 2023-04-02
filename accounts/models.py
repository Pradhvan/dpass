from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .model_mixins import AddressModelMixin


class UserAddress(AddressModelMixin):
    class Meta:
        verbose_name = "User Address"


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    phone_number = PhoneNumberField(blank=True)
    address = models.ForeignKey(
        UserAddress, on_delete=models.CASCADE, related_name="address"
    )
