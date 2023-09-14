
from django.contrib import admin

from .models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
  search_fields = ['username', 'email']

class OTPDisplay(admin.ModelAdmin):
    list_display = ('otp_code', 'user', 'expires_at')
    search_fields = ['user']

admin.site.register(CustomUser, MemberAdmin)
admin.site.register(OTP, OTPDisplay)
# admin.site.register(Customer, MemberAdmin)
# admin.site.register(Address)
# admin.site.register(MedicalHistory)
