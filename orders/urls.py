from django.urls import path
from orders import views


urlpatterns = [
    path('', views.order_list, name='order_list'),
]
