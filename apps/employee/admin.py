from django.contrib import admin

from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
  fieldsets = (
      # (None, {'fields': ('email', 'password', )}),
      # (_('Personal info'), {'fields': ('username', 'name')}),
      # (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
      #                                'groups', 'user_permissions')}),
      # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
      #   (_('user_info'), {'fields': ( 'phone')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'phone', 'password1', 'password2', 'role'),
      }),
  )
  list_display = ['id','email', 'first_name', 'last_name', 'role', "phone"]
  search_fields =['email', 'first_name', 'last_name', 'role', 'phone']
  ordering = ('id', 'first_name' )

admin.site.register(Employee , UserAdmin)