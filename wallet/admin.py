from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from wallet.models import Movement, Transfer, Account, Category

admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Movement)
admin.site.register(Category, MPTTModelAdmin)
