from django.urls import path

from .views import (
    ActionDateFilter,
    ActionList,
    BankList,
    BranchList,
    FetchBalance,
    LastTenActionList,
)

urlpatterns = [
    path("banks/", BankList.as_view(), name="banks"),
    path("action/last/", LastTenActionList.as_view(), name="last_ten_actions"),
    path("branch/info/", BranchList.as_view(), name="fetch_branch_info"),
    path("account/balance/", FetchBalance.as_view(), name="fetch_balance"),
    path(
        "actions/filter/date/", ActionDateFilter.as_view(), name="actions_date_filter"
    ),
    path("actions/", ActionList.as_view(), name="actions"),
]
