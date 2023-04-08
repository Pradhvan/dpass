from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

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


class ActionSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    def to_representation(self, instance):
        representation = super(ActionSerializer, self).to_representation(instance)
        representation["created"] = instance.created.strftime("%Y-%m-%d %H:%M:%S")
        return representation

    class Meta:
        fields = (
            "user_friendly_id",
            "delta",
            "type",
            "reference_type",
            "reference",
            "created",
            "tags",
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
