from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'created_at', 'status', 'description',)
    list_editable = ('price', 'quantity', 'description',)
    search_fields = ('name',)
    list_filter = ('price',)
    
    @admin.display(description='Status')
    def status(self, product):
        if product.quantity == 0:
            return 'Sold Out'
        return 'Available'
    status.short_description = 'Status'  
