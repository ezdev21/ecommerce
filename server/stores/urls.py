
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_list, name='store_list'),
    path('<uuid:store_id>/', views.store_detail, name='store_detail'),
    path('create/', views.store_create, name='store_create'),
    path('<uuid:store_id>/update/', views.store_update, name='store_update'),
    path('<uuid:store_id>/delete/', views.store_delete, name='store_delete'),
    path('<uuid:store_id>/products/', views.store_products, name='store_products'),
]
