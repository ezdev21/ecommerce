
from .models import Cart
from  rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at', 'updated_at', 'products')
        read_only_fields = ("id", "created_at", "updated_at", "user")
