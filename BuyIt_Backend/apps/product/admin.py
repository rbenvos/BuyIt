from django.contrib import admin
from .models import Product, Item

"""
Administracion Product
"""
"""
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        exclude = ('active','avatar','quantity','measure','created_at','modified_at')
"""

class ProductAdmin(admin.ModelAdmin): #ImportExportModelAdmin,
    list_display = ['id','active','name','quantity','measure','created_at','modified_at']
    list_display_links = ['id','name']
    list_filter = ['active','created_at','modified_at']

    fieldsets = (
        ('Product information', {
            'fields': ['name', 'active']
        }),
        ('Units measure', {
            'classes': ('wide',),
            'fields': ['quantity','measure']
        }),
    )
    search_fields = ['id','name', 'last_name','email']
    actions=['make_active','make_desactive']

    #Importador - Exportador
    #resource_class = ProductResource

    #Funciones
    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

"""
Administracion Item
"""
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','active','purchased','amount','product','get_order','created_at','modified_at']
    list_display_links = ['id']
    list_filter = ['active','purchased','created_at','modified_at']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"


admin.site.register(Product, ProductAdmin)
admin.site.register(Item, ItemAdmin)
