from django.conf import settings
from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class OrderItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      related_name="orderitems",
    )
    
    order_id = models.IntegerField()
    
    product_id = models.IntegerField()
    
    quantity = models.IntegerField()
    
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.id} - Order {self.order_id} - Product {self.product_id}"