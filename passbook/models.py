import uuid

from django.conf import settings
from django.db import models

from accounts.model_mixins import AddressModelMixin
from core.models import TimeStampModel


class Address(AddressModelMixin):
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Bank(models.Model):
    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"

    class BankType(models.TextChoices):
        CB = ("Central Bank",)
        COPB = ("Cooperative Bank",)
        COMB = ("Commercial Bank",)
        RRB = ("Regional Rural Banks",)
        LAB = ("Local Area Banks",)
        SB = ("Specialized Banks",)
        SFB = ("Small Finance Banks",)
        PB = ("Payments Banks",)

    bank_name = models.CharField(max_length=100)
    bank_type = models.CharField("type", choices=BankType.choices, max_length=20)
    bic = models.CharField(max_length=7)
    head_office_address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name="head_office_address"
    )

    def __str__(self):
        return self.bank_name


class Branch(models.Model):
    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    branch_name = models.CharField(max_length=500)
    ifsc = models.CharField(max_length=15)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank")
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name="address"
    )

    def __str__(self):
        return self.branch_name


class Account(TimeStampModel):
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    class AccountType(models.TextChoices):
        SAVING = "Savings Account"
        CURRENT = "Current Account"
        SALARY = "Salary Account"
        NRI = "NRI Account"
        RD = "Recurring Deposit Account"
        FD = "Fixed Deposit Accounts"

    MAX_TOTAL_BALANCES = 10000000

    MAX_BALANCE = 10000
    MIN_BALANCE = 0

    MAX_DEPOSIT = 1000
    MIN_DEPOSIT = 1

    MAX_WITHDRAW = 1000
    MIN_WITHDRAW = 1

    balance = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Current balance",
    )
    account_type = models.CharField(
        "type",
        choices=AccountType.choices,
        max_length=30,
    )
    uid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="Public identifier",
    )

    branch = models.OneToOneField(Branch, on_delete=models.PROTECT)
    account_number = models.IntegerField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.account_number)


class Action(models.Model):
    class Meta:
        verbose_name = "Account Action"
        verbose_name_plural = "Account Actions"

    ACTION_TYPE_CREATED = "CREATED"
    ACTION_TYPE_DEPOSITED = "DEPOSITED"
    ACTION_TYPE_WITHDRAWN = "WITHDRAWN"
    ACTION_TYPE_CHOICES = (
        (ACTION_TYPE_CREATED, "Created"),
        (ACTION_TYPE_DEPOSITED, "Deposited"),
        (ACTION_TYPE_WITHDRAWN, "Withdrawn"),
    )

    REFERENCE_TYPE_BANK_TRANSFER = "BANK_TRANSFER"
    REFERENCE_TYPE_CHECK = "CHECK"
    REFERENCE_TYPE_CASH = "CASH"
    REFERENCE_TYPE_NONE = "NONE"
    REFERENCE_TYPE_CHOICES = (
        (REFERENCE_TYPE_BANK_TRANSFER, "Bank Transfer"),
        (REFERENCE_TYPE_CHECK, "Check"),
        (REFERENCE_TYPE_CASH, "Cash"),
        (REFERENCE_TYPE_NONE, "None"),
    )

    id = models.AutoField(
        primary_key=True,
    )
    user_friendly_id = models.CharField(
        unique=True,
        editable=False,
        max_length=30,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        help_text="User who performed the action.",
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
    )
    type = models.CharField(
        max_length=30,
        choices=ACTION_TYPE_CHOICES,
    )
    delta = models.IntegerField(
        help_text="Balance delta.",
    )
    reference = models.TextField(
        blank=True,
    )
    reference_type = models.CharField(
        max_length=30,
        choices=REFERENCE_TYPE_CHOICES,
        default=REFERENCE_TYPE_NONE,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type
