from django.urls import path
from orders import views


urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
