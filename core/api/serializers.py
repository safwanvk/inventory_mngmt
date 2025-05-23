from rest_framework import serializers
from core.models import Product

class ProductSerializer(serializers.ModelSerializer):

      class Meta:
            model = Product
            fields = '__all__'

      def validate_price(self, value):
            if value < 1:
                  raise serializers.ValidationError("Price cannot be negative.")
            return value

      def validate_quantity_in_stock(self, value):
            if value < 1:
                  raise serializers.ValidationError("Quantity in stock cannot be negative.")
            return value


class StockManagementSerializer(serializers.ModelSerializer):
      quantity_to_sell = serializers.IntegerField()
      class Meta:
            model = Product
            fields = ['id', 'quantity_to_sell']

      def validate_quantity_to_sell(self, value):
            if value < 1:
                  raise serializers.ValidationError("Quantity to sell must be positive.")
            product = self.instance
            if product and value > product.quantity_in_stock:
                  raise serializers.ValidationError("Insufficient stock available.")
            return value

