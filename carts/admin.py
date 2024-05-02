from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']
    
    

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'is_active']
    list_editable = ['is_active']
    list_display_links = ['product']
    list_filter = ['product']


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
