# products/services.py
from core.models import Product
from django.shortcuts import get_object_or_404

def list_products():
    return Product.objects.all()

def create_product(validated_data):
    return Product.objects.create(**validated_data)

def update_product(instance, validated_data):
      for attr, value in validated_data.items():
            setattr(instance, attr, value)
      instance.save()
      return instance

def delete_product(instance):
      instance.delete()
      return {}

def get_product_by_id(pk):
      return get_object_or_404(Product, pk=pk)
