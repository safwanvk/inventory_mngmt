from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Product
import uuid

class ProductAPITestCase(TestCase):
      def setUp(self):
            self.client = APIClient()
            self.product = Product.objects.create(
                  name='Test Product',
                  price=100.0,
                  quantity_in_stock=10
            )
            self.base_url = '/api/v1/products/'

      def test_create_product_success(self):
            data = {'name': 'New Product', 'price': 50.0, 'quantity_in_stock': 5}
            response = self.client.post(self.base_url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

      def test_create_product_invalid_price(self):
            data = {'name': 'Invalid Product', 'price': -10.0, 'quantity_in_stock': 5}
            response = self.client.post(self.base_url, data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

      def test_create_product_invalid_quantity(self):
            data = {'name': 'Invalid Product', 'price': 50.0, 'quantity_in_stock': -5}
            response = self.client.post(self.base_url, data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

      def test_list_products(self):
            response = self.client.get(self.base_url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

      def test_filter_products_by_name_and_min_quantity(self):
            response = self.client.get(self.base_url + '?name=Test&minimum_quantity_in_stock=5')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

      def test_ordering_products_by_price_desc(self):
            response = self.client.get(self.base_url + '?ordering=-price')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

      def test_get_product_detail(self):
            response = self.client.get(f'{self.base_url}{self.product.id}/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

      def test_update_product(self):
            data = {'name': 'Updated Product', 'price': 150.0, 'quantity_in_stock': 20}
            response = self.client.put(f'{self.base_url}{self.product.id}/', data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

      def test_delete_product(self):
            response = self.client.delete(f'{self.base_url}{self.product.id}/')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

      def test_sell_product_success(self):
            data = {'quantity_to_sell': 5}
            response = self.client.post(f'{self.base_url}{self.product.id}/sell/', data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

      def test_sell_product_insufficient_stock(self):
            data = {'quantity_to_sell': 20}
            response = self.client.post(f'{self.base_url}{self.product.id}/sell/', data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

      def test_sell_product_invalid_quantity(self):
            data = {'quantity_to_sell': -2}
            response = self.client.post(f'{self.base_url}{self.product.id}/sell/', data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)