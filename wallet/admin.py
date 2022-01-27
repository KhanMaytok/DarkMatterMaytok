from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from wallet.models import Movement, Transfer, Account, Category, Debt


class AccountAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    exclude = ('user',)

    def get_form(self, request, **kwargs):
        form = super(AccountAdmin, self).get_form(request, **kwargs)
        form.user = request.user
        return form


admin.site.register(Account, AccountAdmin)
admin.site.register(Transfer)
admin.site.register(Movement)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Debt)
