from django.contrib import admin

from payment.models import Item, Order

admin.site.empty_value_display = '-empty'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
    )


admin.site.register(Order)
