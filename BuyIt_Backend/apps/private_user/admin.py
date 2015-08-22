from django.contrib import admin
from models import PrivateUser, Friend

"""
Administracion User
"""


class FriendInline(admin.TabularInline):
    model = Friend
    fk_name = "user"


class PrivateUserAdmin(admin.ModelAdmin):
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
    list_display = ['id','active','email','name','last_name','get_num_friends_active','get_num_devices',
                    'get_num_groups','created_at','modified_at']
    list_display_links = ['name', 'last_name','email']
    list_filter = ['active','created_at','modified_at']
    search_fields = ['id','name', 'last_name','email']
    actions = ['make_active','make_desactive']
    inlines = [
        FriendInline,
    ]


    def make_active(self, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(self, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"


admin.site.register(PrivateUser, PrivateUserAdmin)