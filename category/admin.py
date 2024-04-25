from django.contrib import admin
from . models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Category_Name',)}
    list_display = ('Category_Name', 'slug')


admin.site.register(Category, CategoryAdmin)