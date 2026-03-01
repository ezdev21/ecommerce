
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'created_at', 'updated_at', 'products')
        read_only_fields = ("id", "created_at", "updated_at", "user")