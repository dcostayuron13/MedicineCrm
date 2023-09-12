from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price', 'manufacturer',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name', 'manufacturer',)
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category')
        }),
        ('Additional Information', {
            'fields': ('quantity', 'price', 'manufacturer')
        }),
    )
