from django.urls import path
from .views import product_list, product_detail, filter_product_list, add_product, edit_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('filter/', filter_product_list, name='filter_product_list'),
    path('add_product/', add_product, name='add_product'),
    path('<int:id>/edit/', edit_product, name='edit_product'),
    path('<int:id>/', product_detail, name='product_detail'),
    ]