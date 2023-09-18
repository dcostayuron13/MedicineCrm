from django.contrib import admin

from apps.content.models import *

class TicketsDisplay(admin.ModelAdmin):
  list_display = ('subject', 'status', 'priority', 'is_active') #, 'created_by')
  search_fields = ['subject', 'status']

admin.site.register(Tickets, TicketsDisplay)
admin.site.register(Comments)
