from django.contrib import admin
from models import Group, GroupSetting

"""
Administracion Group
"""


class MemberListInline(admin.TabularInline):
    model = Group.members.through


class OrderListInline(admin.TabularInline):
    model = Group.orders.through


class GroupSettingListInline(admin.TabularInline):
    model = Group.settings.through


class GroupSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','active']
    list_display_links = ['id','name']
    list_filter = ['active']
    fieldsets = (
        ('Setting information', {
            'fields': ['name', 'active']
        }),
    )
    search_fields = ['id', 'name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name','active','group_users','group_orders','created_at','modified_at']
    list_display_links = ['id','name']
    list_filter = ['active','created_at','modified_at']
    exclude = ('orders',)
    fieldsets = (
        ('Group information', {
            'fields': ['name', 'active']
        }),
    )
    search_fields = ['id', 'name']
    actions = ['make_active', 'make_desactive']
    inlines = [
        GroupSettingListInline, MemberListInline, OrderListInline
    ]

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupSetting, GroupSettingAdmin)
