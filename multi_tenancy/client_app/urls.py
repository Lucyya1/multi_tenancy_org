from .views import index
from django.urls import path
# from django.contrib import admin

urlpatterns = [

    path('', index, name = 'client_index'),
]