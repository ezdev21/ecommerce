
from django.contrib import admin
from django.urls import include, path
from .views import home

admin.site.site_header = "E-commerce Admin"
admin.site.site_title = "E-commerce Admin Portal"
admin.site.index_title = "Welcome to the E-commerce Admin Portal"

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('stores/', include('stores.urls')),
    path('tags/', include('tags.urls')),
    path('categories/', include('categories.urls')),
    path('auth/', include('accounts.urls')),
    path('cartitems/', include('cartitems.urls')),
    path('orderitems/', include('orderitems.urls')),
]
