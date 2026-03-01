import uuid

from django.db import models
from django.conf import settings

class Order(models.Model):
  id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
  )
    
  user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
  )
  
  products = models.ManyToManyField('products.Product', related_name='orders')
  
  created_at = models.DateTimeField(auto_now_add=True)
  
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
        return f"Order {self.id} for {self.user.username}"