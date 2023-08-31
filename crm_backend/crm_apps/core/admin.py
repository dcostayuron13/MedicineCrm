from django.contrib import admin

from .models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
  search_fields = ['username', 'email']

admin.site.register(CustomUser, MemberAdmin)
