from django.contrib import admin

# Register your models here.
from .models import CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at',)
    list_editable = ('quantity',)
    search_fields = ('product__name',)
    list_filter = ('created_at',)
    