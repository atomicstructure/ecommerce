from django.urls import path

from store.views import store

path('', store, name='store'),