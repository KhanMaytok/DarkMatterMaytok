from django.contrib import admin

from wallet.models import Movement, Transfer, Account

admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Movement)
