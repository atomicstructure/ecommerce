from django.contrib import admin

from .models import Order, OrderProduct, Payment

# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price')

class OrderAdmin(admin.ModelAdmin):
    # Display the following fields in the Admin Panel
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 
                        'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'full_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
