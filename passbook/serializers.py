from rest_framework import serializers

from .models import Bank, Branch


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "bank_type",
            "bic",
            "head_office_address",
        )
        model = Bank


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "branch_address",
            "ifsc",
            "bank",
        )
        model = Branch
