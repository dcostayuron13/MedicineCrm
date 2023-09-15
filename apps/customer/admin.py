from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ('email', 'username', 'role', 'is_active', 'is_staff', 'dnc')
  search_fields = ['username', 'email']

admin.site.register(Customer, MemberAdmin)
admin.site.register(Address)