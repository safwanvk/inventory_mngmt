# products/services.py
from core.models import Product
from django.shortcuts import get_object_or_404
from django.db import transaction

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

def get_product_by_id_locked(product_id):
      return Product.objects.select_for_update().get(id=product_id)

def sell_product(instance, validated_data):
      quantity = validated_data.get('quantity_to_sell')

      if instance.quantity_in_stock < quantity:
        raise ValueError("Insufficient stock")

      instance.quantity_in_stock -= quantity
      instance.save()
      return instance
