from django.urls import path
from .views import ProductListCreateView, ProductDetailView, StockManagementView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<uuid:product_id>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<uuid:product_id>/sell/', StockManagementView.as_view(), name='stock-management'),
]