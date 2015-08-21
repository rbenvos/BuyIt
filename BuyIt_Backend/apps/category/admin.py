from django.contrib import admin
from apps.category.models import Category, Subcategory


class CategoryAdmin(admin.ModelAdmin): #ImportExportModelAdmin,

    list_display = ['id','active','name','getSubcategories','created_at','modified_at']
    list_display_links = ['id','name']
    list_filter = ['active','name','created_at','modified_at']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

    #Importador - Exportador
    #resource_class = CategoryResource

"""
Administracion Order
"""
"""
class SubcategoryResource(resources.ModelResource):
    class Meta:
        model = Subcategory
"""

class SubcategoryAdmin(admin.ModelAdmin): #ImportExportModelAdmin,
    list_display = ['id','active','name','created_at','modified_at']
    list_display_links = ['id','name']
    list_filter = ['active','name','created_at','modified_at']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

    #Importador - Exportador
    #resource_class = SubcategoryResource

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)