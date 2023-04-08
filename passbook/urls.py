from django.urls import path

from .views import (
    ActionDateFilter,
    ActionList,
    BankList,
    BranchList,
    FechAccountInfo,
    FechBranchInfo,
    LastTenActionList,
)

urlpatterns = [
    path("banks/", BankList.as_view(), name="banks"),
    path("branches/", BranchList.as_view(), name="branch_list"),
    path("action/last/", LastTenActionList.as_view(), name="last_ten_actions"),
    path("branch/info/", FechBranchInfo.as_view(), name="fetch_branch_info"),
    path("account/info/", FechAccountInfo.as_view(), name="fetch_account_info"),
    path(
        "actions/filter/date/", ActionDateFilter.as_view(), name="actions_date_filter"
    ),
    path("actions/", ActionList.as_view(), name="actions"),
]
