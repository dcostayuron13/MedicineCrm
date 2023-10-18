from django.contrib import admin

# Register your models here.
from django.contrib import admin

from apps.customer.models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'phone', 'address','remarks','dnc')
  search_fields = ['username', 'email']

admin.site.register(Customer, MemberAdmin)
admin.site.register(Address)