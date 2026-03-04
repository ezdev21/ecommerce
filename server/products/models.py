import uuid
from django.conf import settings
from django.db import models

from categories.models import Category
from stores.models import Store
from tags.models import Tag

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products",
    )

    name = models.CharField(max_length=255)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField()

    image = models.ImageField(
        upload_to='products/'
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
    )
  
    tags = models.ManyToManyField(
      Tag,
      related_name='products',
      blank=True
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name