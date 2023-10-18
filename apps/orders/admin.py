from django.contrib import admin

from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'agent', 'order_quantity', 'status']
    search_fields = ['id', 'customer__name', 'agent__name', 'status']
    list_filter = ['status']
    ordering = ('id', 'status')

admin.site.register(Order, OrderAdmin)
