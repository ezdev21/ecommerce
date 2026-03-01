
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('<uuid:cart_id>/', views.cart_detail, name='cart_detail'),
    path('create/', views.cart_create, name='cart_create'),
    path('<uuid:cart_id>/update/', views.cart_update, name='cart_update'),
    path('<uuid:cart_id>/delete/', views.cart_delete, name='cart_delete'),
]
