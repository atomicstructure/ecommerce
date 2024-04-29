from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('delete_cart_item/<int:product_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('cart/add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
]