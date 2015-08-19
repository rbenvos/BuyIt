from django.contrib import admin
from models import User

"""
Administracion User
"""


class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User information', {
            'fields': [('name', 'last_name'), 'email', 'password','active']
        }),
        ('Device', {
            'classes': ('wide',),
            'fields': ['device']
        }),
        ('Friends', {
            'classes': ('collapse',),
            'fields': ['friends']
        }),
    )
    list_display = ['id','active','email','name','last_name','getNumFriendsActive','getNumDevices','getNumGroups','created_at','modified_at']
    list_display_links = ['name', 'last_name','email']
    list_filter = ['active','created_at','modified_at']
    search_fields = ['id','name', 'last_name','email']
    actions=['make_active','make_desactive']

    def make_active(self, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(self, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"


admin.site.register(User, UserAdmin)