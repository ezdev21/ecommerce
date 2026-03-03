from django.urls import path
from . import views

urlpatterns = [
    path('', views.tag_list, name='tag_list'),
    path('<uuid:tag_id>/', views.tag_detail, name='tag_detail'),
    path('create/', views.tag_create, name='tag_create'),
    path('<uuid:tag_id>/update/', views.tag_update, name='tag_update'),
    path('<uuid:tag_id>/delete/', views.tag_delete, name='tag_delete'),
    path('<uuid:tag_id>/products/', views.tag_products, name='tag_products'),
]
