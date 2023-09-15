from django.contrib import admin
from apps.orders.models import Order
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'date', 'status', 'total_amount')
#     list_filter = ('status',)
#     search_fields = ('customer__name', 'customer__email')
#     filter_horizontal = ('inventory',)
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         queryset = queryset.select_related('customer')
#         return queryset
#
#     def customer_name(self, obj):
#         return obj.customer.name
#
#     customer_name.short_description = 'Customer Name'
