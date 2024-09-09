from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product_list, name='product_list'),           # List all products
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # View product details
    path('product/new/', views.product_create, name='product_create'),      # Create a new product
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),  # Update product
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'), # Delete product
]
