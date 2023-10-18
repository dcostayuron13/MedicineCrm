
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.core.models import *
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
          'fields': ('email', 'phone', 'password1', 'password2'),
      }),
  )
  list_display = ['id','email', 'first_name', 'last_name', 'is_staff', "phone"]
  search_fields =['email', 'first_name', 'last_name', 'is_staff', 'phone']
  ordering = ('id', )

class OTPDisplay(admin.ModelAdmin):
    list_display = ('otp_code', 'user', 'expires_at')
    search_fields = ['user']

admin.site.register(CustomUser, UserAdmin)
admin.site.register(OTP, OTPDisplay)

