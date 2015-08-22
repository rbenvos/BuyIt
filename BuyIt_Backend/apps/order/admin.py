from django.contrib import admin
from models import Order


"""
Administracion Order
"""
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','active','get_groups','order_num_products','created_at','modified_at']
    list_display_links = ['id','name']
    list_filter = ['active','created_at','modified_at']

    fieldsets = (
        ('Order information', {
            'fields': ['name', 'active']
        }),
        ('Products information', {
            'classes' : ['wide'],
            'fields': ['items']
        }),
    )
    search_fields = ['id','name']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

admin.site.register(Order, OrderAdmin)
