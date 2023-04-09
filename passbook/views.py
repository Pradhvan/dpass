import datetime

from django_filters.rest_framework import DjangoFilterBackend
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

    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)


class BranchList(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "ifsc",
        "address__city",
        "address__pin_code",
    ]
    queryset = Branch.objects.all()

class LastTenActionList(APIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def get(self, request):
        # select * from passbook_action order by passbook_action.created desc limit 10;
        actions = Action.objects.filter(user=request.user).order_by("-created")[:10]
        # By setting many=True you tell drf that queryset contains mutiple items.
        # If it's not set it might map id feild or some other feild from query set
        # to serializers feild that might give error like
        # AttributeError: Got AttributeError when attempting to get a value for field `branch_name` on serializer `BranchSerializer`.
        # The serializer field might be named incorrectly and not match any attribute or key on the `QuerySet` instance.
        # Original exception text was: 'QuerySet' object has no attribute 'branch_name'.

        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)


class ActionList(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = ActionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "user_friendly_id",
    ]

    def get_queryset(self):
        current_user = self.request.user
        return Action.objects.filter(user=current_user)


class ActionDateFilter(APIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def get(self, request):
        current_user = request.user
        actions = Action.objects.filter(
            user=current_user, created__gte=datetime.date.today()
        )
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        start_date = datetime.datetime.strptime(data.get("start_date"), "%Y-%m-%d")
        end_date = datetime.datetime.strptime(data.get("end_date"), "%Y-%m-%d")
        actions = Action.objects.filter(
            created__gt=start_date,
            created__lt=end_date,
            user=request.user,
        )
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)


class FetchBalance(APIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def get(self, request):
        account = Account.objects.filter(user=request.user).values()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)
