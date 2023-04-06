from django.urls import path

from .views import BankList, BranchList, FechBranchInfo, LastTenActionList

urlpatterns = [
    path("banks/", BankList.as_view(), name="banks"),
    path("branches/", BranchList.as_view(), name="branch_list"),
    path("lasttenactions/", LastTenActionList.as_view(), name="last_ten_actions"),
    path("branchinfo/", FechBranchInfo.as_view(), name="fetch_branch_info"),
]
