from django.db import models

from accounts.model_mixins import AddressModelMixin


class BankAddress(AddressModelMixin):
    class Meta:
        verbose_name = "Bank Address"


class Bank(models.Model):
    class BankType(models.TextChoices):
        CB = ("Central Bank",)
        COPB = ("Cooperative Bank",)
        COMB = ("Commercial Bank",)
        RRB = ("Regional Rural Banks",)
        LAB = ("Local Area Banks",)
        SB = ("Specialized Banks",)
        SFB = ("Small Finance Banks",)
        PB = ("Payments Banks",)

    name = models.CharField(max_length=100)
    bank_type = models.CharField("type", choices=BankType.choices, max_length=20)
    bic = models.CharField(max_length=7)
    head_office_address = models.ForeignKey(
        BankAddress, on_delete=models.CASCADE, related_name="head_office_address"
    )


class Account(models.Model):
    ...


class Transaction(models.Model):
    ...


class Branch(models.Model):
    ...


class AccountType(models.Model):
    ...
