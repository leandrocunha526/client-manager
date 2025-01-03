from .models import Sale, Item
from django.contrib import admin


class ItemSaleInline(admin.TabularInline):
    model = Item
    extra = 1


class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ['total',]
    list_filter = 'client', 'status'
    list_display = 'id', 'client', 'total', 'datetime', 'status'
    inlines = [ItemSaleInline]

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(Sale, SaleAdmin)
admin.site.register(Item)
