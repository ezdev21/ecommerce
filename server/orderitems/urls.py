
from django.urls import path
from . import views

urlpatterns = [
    path('', views.orderitem_list, name='orderitem-list'),
    path('<uuid:order_id>/<uuid:product_id>/', views.orderitem_detail, name='orderitem-detail'),
    path('create/', views.orderitem_create, name='orderitem-create'),
    path('<uuid:order_id>/<uuid:product_id>/update/', views.orderitem_update, name='orderitem-update'),
    path('<uuid:order_id>/<uuid:product_id>/delete/', views.orderitem_delete, name='orderitem-delete'),
]
