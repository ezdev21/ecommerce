from rest_framework import serializers
from tags.serializers import TagSerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity')
        read_only_fields = ("id", "created_at", "updated_at", "user")