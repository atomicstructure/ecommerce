from django.contrib import admin
from .models import Product, Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'modified_date','is_available')
    list_display_links = ('product_name',)
    list_filter = ('category', 'created_date')
    list_editable = ('is_available',)
    search_fields = ('product_name', 'category')
    list_per_page = 20


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
    search_fields = ('product', 'variation_category', 'variation_value')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.site_header = 'SamMart E-commerce Admin'
admin.site.site_title = 'SamMart E-commerce Admin Portal'
admin.site.index_title = 'Welcome to SamMart E-commerce Admin Portal'
