from django.contrib import admin

from .models import Account, Address, Bank, Branch, Transaction

admin.site.register(Account)
admin.site.register(Address)
admin.site.register(Bank)
admin.site.register(Branch)
admin.site.register(Transaction)
