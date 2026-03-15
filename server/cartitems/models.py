import uuid

from django.db import models

from django.conf import settings

# Create your models here.
class CartItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      related_name="cartitems",
    )
    
    product = models.ForeignKey(
      'products.Product', 
      on_delete=models.CASCADE
    )
    
    cart = models.ForeignKey(
      'carts.Cart', 
      on_delete=models.CASCADE,
      related_name='cart_items'
    )
    
    quantity = models.PositiveIntegerField(default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"