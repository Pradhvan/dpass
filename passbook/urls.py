from django.urls import path

from .views import BankList, BranchList

urlpatterns = [
    path("banks", BankList.as_view(), name="banks"),
    path("branches", BranchList.as_view(), name="branch_list"),
]
