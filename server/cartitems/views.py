from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CartItem
from .serializers import CartItemSerializer

# Create your views here.
@api_view(['GET'])
def cartitem_list(request):
    cartitems = CartItem.objects.all()
    serializer = CartItemSerializer(cartitems, many=True)
    return Response(serializer.data)
  
@api_view(['POST'])
def cartitem_create(request):
    serializer = CartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
  
@api_view(['GET'])
def cartitem_detail(request, cartitem_id):
    try:
        cartitem = CartItem.objects.get(pk=cartitem_id)
    except CartItem.DoesNotExist:
        return Response(status=404)
    
    serializer = CartItemSerializer(cartitem)
    return Response(serializer.data)
  
@api_view(['PUT'])
def cartitem_update(request, cartitem_id):
    try:
        cartitem = CartItem.objects.get(pk=cartitem_id)
    except CartItem.DoesNotExist:
        return Response(status=404)
    
    serializer = CartItemSerializer(cartitem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
  
@api_view(['DELETE'])
def cartitem_delete(request, cartitem_id):
    try:
        cartitem = CartItem.objects.get(pk=cartitem_id)
    except CartItem.DoesNotExist:
        return Response(status=404)
    
    cartitem.delete()
    return Response(status=204)