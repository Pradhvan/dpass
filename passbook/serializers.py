from rest_framework import serializers

from .models import Account, Action, Address, Bank, Branch


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "address1",
            "address2",
            "pin_code",
            "city",
        )
        model = Address


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "bank_name",
            "bank_type",
            "bic",
            "head_office_address",
        )
        model = Bank


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "branch_name",
            "ifsc",
            "bank",
            "address",
        )
        model = Branch


class BranchListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        fields = ("branch_name", "ifsc", "address")
        model = Branch


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "user_friendly_id",
            "delta",
            "type",
            "reference_type",
            "reference",
        )
        model = Action


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "balance",
            "account_type",
            "account_number",
        )
        model = Account
