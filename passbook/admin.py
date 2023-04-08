from django.contrib import admin

from .models import Account, Action, Address, Bank, Branch

admin.site.register(Account)
admin.site.register(Address)

admin.site.register(Bank)
admin.site.register(Branch)


class ActionAdmin(admin.ModelAdmin):
    list_display = (
        "user_friendly_id",
        "user",
        "account",
        "type",
        "delta",
        "created",
        "reference_type",
    )


admin.site.register(Action, ActionAdmin)
