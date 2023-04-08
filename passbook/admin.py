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
        "tag_list",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())


admin.site.register(Action, ActionAdmin)
