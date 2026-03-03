from rest_framework import serializers
from products.serializers import ProductSerializer
from .models import Store

class StoreSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'products']
        read_only_fields = ['id', 'created_at', 'updated_at']
