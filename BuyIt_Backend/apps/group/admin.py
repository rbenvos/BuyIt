from django.contrib import admin
from apps.member.admin import MemberInline
from models import Group, GroupSetting

"""
Administracion Group
"""


class OrderListInline(admin.TabularInline):
    model = Group.orders.through
    extra = 1


class GroupSettingListInline(admin.TabularInline):
    model = Group.settings.through
    extra = 1


class GroupSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']
    list_display_links = ['id', 'name']
    list_filter = ['active']
    fieldsets = (
        ('Setting information', {
            'fields': ['name', 'active']
        }),
    )
    search_fields = ['id', 'name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'active',
                    'group_users',
                    'group_orders',
                    'created_at',
                    'modified_at']

    list_display_links = ['id',
                          'name']

    list_filter = ['active',
                   'created_at',
                   'modified_at']

    exclude = ('orders',)

    fieldsets = (
        ('Group information', {
            'fields': ['name',
                       'active']
        }),
    )
    search_fields = ['id',
                     'name']

    actions = ['make_active',
               'make_desactive']

    inlines = [GroupSettingListInline,
               MemberInline,
               OrderListInline
    ]

    def make_active(self, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(self, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupSetting, GroupSettingAdmin)
