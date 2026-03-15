
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartitem_list, name='cartitem-list'),
    path('<uuid:cartitem_id>/', views.cartitem_detail, name='cartitem-detail'),
    path('create/', views.cartitem_create, name='cartitem-create'),
    path('<uuid:cartitem_id>/update/', views.cartitem_update, name='cartitem-update'),
    path('<uuid:cartitem_id>/delete/', views.cartitem_delete, name='cartitem-delete'),
]
