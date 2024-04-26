from django.contrib import admin
from .models import Products
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'modified_date','is_available')
    list_display_links = ('product_name',)
    list_filter = ('category', 'created_date')
    list_editable = ('is_available',)
    search_fields = ('product_name', 'category')
    list_per_page = 20

admin.site.register(Products, ProductAdmin)
