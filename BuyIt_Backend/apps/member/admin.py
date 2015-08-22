from django.contrib import admin
from apps.member.models import Member


class MemberInline(admin.TabularInline):
    model = Member
    extra = 1


class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','active','admin','private_user','group', 'created_at','modified_at']
    list_display_links = ['id', 'private_user']
    list_filter = ['admin','active','created_at','modified_at']
    fieldsets = (
        ('Member information', {
            'fields': ['active', 'admin']
        }),
        ('User information', {
            'classes': ['wide'],
            'fields': ['private_user']
        }),
        ('Group information', {
            'classes': ['wide'],
            'fields': ['group']
        }),
    )
    search_fields = ['id']
    actions = ['make_active', 'make_desactive']

    def make_active(self, queryset):
        queryset.update(active=True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(self,  queryset):
        queryset.update(active=False)
    make_desactive.short_description = "Mark selected as desactive"

admin.site.register(Member, MemberAdmin)
