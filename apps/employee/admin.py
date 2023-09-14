<<<<<<< HEAD
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
  search_fields = ['username', 'email']

=======
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

class MemberAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
  search_fields = ['username', 'email']

>>>>>>> development
admin.site.register(Employee , MemberAdmin)