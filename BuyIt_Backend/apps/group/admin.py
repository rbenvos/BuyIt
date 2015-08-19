from django.contrib import admin
from models import Group

"""
Administracion Group
"""
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name','active','groupUsers','groupOrders','created_at','modified_at']
    list_display_links = ['id','name']
    list_filter = ['active','created_at','modified_at']

    fieldsets = (
        ('Group information', {
            'fields': ['name', 'active']
        }),
        ('Users information', {
            'classes' : ['wide'],
            'fields': ['users']
        }),
        ('Order information', {
            'classes' : ['wide'],
            'fields': ['orders']
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

admin.site.register(Group, GroupAdmin)
