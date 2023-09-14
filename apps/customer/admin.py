<<<<<<< HEAD
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
  search_fields = ['username', 'email']

admin.site.register(Customer, MemberAdmin)
=======
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ('email', 'username', 'role', 'is_active', 'is_staff')
  search_fields = ['username', 'email']

admin.site.register(Customer, MemberAdmin)
>>>>>>> development
admin.site.register(Address)