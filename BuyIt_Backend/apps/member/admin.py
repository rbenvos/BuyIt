from django.contrib import admin
from apps.group.admin import MemberListInline
from apps.member.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','admin','active','private_user','created_at','modified_at']
    list_display_links = ['id']
    list_filter = ['admin','active','created_at','modified_at']
    fieldsets = (
        ('Member information', {
            'fields': ['active', 'admin']
        }),
        ('User information', {
            'classes': ['wide'],
            'fields': ['private_user']
        }),
    )
    search_fields = ['id']
    actions = ['make_active', 'make_desactive']
    inlines = [
        MemberListInline
    ]

    def make_active(self, queryset):
        queryset.update(active=True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(self,  queryset):
        queryset.update(active=False)
    make_desactive.short_description = "Mark selected as desactive"

admin.site.register(Member, MemberAdmin)
