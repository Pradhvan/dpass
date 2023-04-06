from django.contrib import admin

from .models import Account, Action, Address, Bank, Branch

admin.site.register(Account)
admin.site.register(Address)
admin.site.register(Action)
admin.site.register(Bank)
admin.site.register(Branch)
