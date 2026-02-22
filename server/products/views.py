from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def product_list(request):
    return JsonResponse({'message': 'List of products'})

def product_detail(request, product_id):
    return JsonResponse({'message': f'Details of product {product_id}'})

def product_create(request):
    return JsonResponse({'message': 'Create a new product'})

def product_update(request, product_id):
    return JsonResponse({'message': f'Update product {product_id}'})

def product_delete(request, product_id):
    return JsonResponse({'message': f'Delete product {product_id}'})