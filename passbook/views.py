from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bank, Branch
from .serializers import BranchSerializer


class BankList(APIView):
    def get(self, request, format=None):
        banks = [bank.name for bank in Bank.objects.all()]
        return Response(banks)


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
