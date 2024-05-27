from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address_line_1', 'address_line_2', 'country', 'state', 'city', 'order_total', 'tax', 'status', 'ip', 'order_note', 'is_ordered', ]
        widgets = {
            'shipping_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shipping Address'}),
            'shipping_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shipping City'}),
            'shipping_zip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shipping Zip'}),
            'shipping_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shipping Country'}),
        }