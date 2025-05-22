from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      name = models.CharField(max_length=100)
      description = models.TextField(blank=True, null=True, max_length=500)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      quantity_in_stock = models.IntegerField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
          return self.name