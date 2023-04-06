from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account, Action, Bank, Branch
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    AccountSerializer,
    ActionSerializer,
    BankSerializer,
    BranchSerializer,
)


class BankList(APIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def get(self, request, format=None):
        banks = [bank.name for bank in Bank.objects.all()]
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)


class BranchList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)

    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class LastTenActionList(APIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def get(self, request):
        # select * from passbook_action order by passbook_action.created desc limit 10;
        actions = Action.objects.order_by("-created")[:10]
        # By setting many=True you tell drf that queryset contains mutiple items.
        # If it's not set it might map id feild or some other feild from query set
        # to serializers feild that might give error like
        # AttributeError: Got AttributeError when attempting to get a value for field `branch_name` on serializer `BranchSerializer`.
        # The serializer field might be named incorrectly and not match any attribute or key on the `QuerySet` instance.
        # Original exception text was: 'QuerySet' object has no attribute 'branch_name'.

        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)


class FechBranchInfo(APIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def post(self, request):
        data = request.data
        branch = Branch.objects.filter(ifsc=data.get("ifsc")).values()
        serializer = BranchSerializer(branch, many=True)
        return Response(serializer.data)


class FechAccountInfo(APIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def post(self, request):
        data = request.data
        account = Account.objects.filter(**data).values()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)
