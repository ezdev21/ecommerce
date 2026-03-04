
from django.contrib import admin
from django.urls import include, path
from .views import home

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
]
