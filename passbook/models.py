from django.conf import settings
from django.db import models

from accounts.model_mixins import AddressModelMixin


class Address(AddressModelMixin):
    class Meta:
        verbose_name = "Address"


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
    head_office_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=500)
    branch_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=15)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)


class Account(models.Model):
    class AccountType(models.TextChoices):
        SAVING = "Savings Account"
        CURRENT = "Current Account"
        SALARY = "Salary Account"
        NRI = "NRI Account"
        RD = "Recurring Deposit Account"
        FD = "Fixed Deposit Accounts"

    balance = models.DecimalField(max_digits=6, decimal_places=2)
    account_type = models.CharField(
        "type",
        choices=AccountType.choices,
        max_length=30,
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_number = models.IntegerField()


class Transaction(models.Model):
    ammount = models.DecimalField(max_digits=6, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=22)
