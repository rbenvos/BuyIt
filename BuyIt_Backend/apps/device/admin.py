from django.contrib import admin
from apps.private_user.admin import DeviceInline
from models import Device

"""
Administracion Device
"""


class DeviceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Device information', {
            'fields': ['id_device', 'active', 'os']
        }),
    )
    list_display = ['id', 'id_device', 'active', 'os', 'created_at', 'modified_at']
    list_filter = ['active', 'created_at']
    list_display_links = ['id', 'id_device']
    search_fields = ['id', 'id_device']
    actions=['make_active', 'make_desactive']
    inlines = [
        DeviceInline
    ]


    def make_active(self,queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(self,  queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

admin.site.register(Device, DeviceAdmin)