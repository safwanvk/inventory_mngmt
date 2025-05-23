# products/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, StockManagementSerializer
import core.api.services as product_service
from django.db import transaction
from core.models import Product

class ProductListCreateView(APIView):
    def get(self, request):
        products = product_service.list_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = product_service.create_product(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            updated_product = product_service.update_product(product, serializer.validated_data)
            return Response(ProductSerializer(updated_product).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        product_service.delete_product(product)
        return Response({'detail': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)

class StockManagementView(APIView):

    def post(self, request, product_id):
        try:
            with transaction.atomic():
                product = product_service.get_product_by_id_locked(product_id)
                serializer = StockManagementSerializer(product, data=request.data)
                if serializer.is_valid():
                    sell_product = product_service.sell_product(product, serializer.validated_data)
                    return Response(ProductSerializer(sell_product).data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
