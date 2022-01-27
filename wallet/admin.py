from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from wallet.models import Movement, Transfer, Account, Category, Debt


class AccountAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


admin.site.register(Account, AccountAdmin)
admin.site.register(Transfer)
admin.site.register(Movement)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Debt)
