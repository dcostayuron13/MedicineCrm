from django.contrib import admin

from .models import *

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price', 'instock_quantity', 'category']
    search_fields = ['id', 'product_name', 'category', 'price']
    list_filter = ['category']
    ordering = ('id', 'product_name')

admin.site.register(Inventory, InventoryAdmin)

