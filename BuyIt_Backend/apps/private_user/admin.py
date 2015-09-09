from django.contrib import admin
from apps.member.admin import MemberInline
from models import PrivateUser, Friend, Phone

"""
Administracion User
"""


class FriendInline(admin.TabularInline):
    model = Friend
    fields = ('active', 'get_user_name')
    readonly_fields = ('get_user_name',)
    can_delete = True


class DeviceInline(admin.TabularInline):
    model = PrivateUser.device.through
    extra = 1


class PrivateUserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User information', {
            'fields': [('name', 'last_name'), 'email', 'password', 'active']
        }),
        ('Phone information', {
            'fields': ['phones']
        }),
    )
    list_display = ['id', 'active', 'email', 'name', 'last_name', 'created_at', 'modified_at']
    list_display_links = ['name', 'last_name', 'email']
    list_filter = ['active', 'created_at', 'modified_at']
    search_fields = ['id', 'name', 'last_name', 'email']
    actions = ['make_active', 'make_desactive']
    inlines = [DeviceInline, FriendInline, MemberInline]

    def make_active(self, queryset):
        queryset.update(active=True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(self, queryset):
        queryset.update(active=False)
    make_desactive.short_description = "Mark selected as desactive"


class PhoneAdmin(admin.ModelAdmin):
    model = Phone
    list_display = ['id', 'active', 'phone', 'num_users', 'created_at']
    list_display_links = ['id', 'phone']
    readonly_fields = ['users']


admin.site.register(PrivateUser, PrivateUserAdmin)
admin.site.register(Phone, PhoneAdmin)
