
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('<uuid:product_id>/update/', views.product_update, name='product_update'),
    path('<uuid:product_id>/delete/', views.product_delete, name='product_delete'),
    path('<uuid:product_id>/tags/', views.product_tags, name='product_tags'),
]
