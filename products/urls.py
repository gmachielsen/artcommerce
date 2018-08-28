from django.urls import path
from .views import product_list, product_detail, filter_product_list

urlpatterns = [
    path('', product_list, name='product_list'),
    path('filter/', filter_product_list, name='filter_product_list'),
    path('/<id>, products', product_detail, name='product_detail'),
    ]