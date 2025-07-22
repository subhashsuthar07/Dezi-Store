from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('product/', views.store, name='product'),
    path('product/<slug:category_slug>', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
] 


