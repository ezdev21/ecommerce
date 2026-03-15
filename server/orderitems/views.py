from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import OrderItem
from .serializers import OrderItemSerializer

# Create your views here.
@api_view(['GET'])
def orderitem_list(request):
    orderitems = OrderItem.objects.all()
    serializer = OrderItemSerializer(orderitems, many=True)
    return Response(serializer.data)
  
@api_view(['POST'])
def orderitem_create(request):
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
  
@api_view(['GET'])
def orderitem_detail(request, order_id, product_id):
    try:
        orderitem = OrderItem.objects.get(order_id=order_id, product_id=product_id)
    except OrderItem.DoesNotExist:
        return Response(status=404)
    
    serializer = OrderItemSerializer(orderitem)
    return Response(serializer.data)

@api_view(['PUT'])
def orderitem_update(request, order_id, product_id):
    try:
        orderitem = OrderItem.objects.get(order_id=order_id, product_id=product_id)
    except OrderItem.DoesNotExist:
        return Response(status=404)
    
    serializer = OrderItemSerializer(orderitem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def orderitem_delete(request, order_id, product_id):
    try:
        orderitem = OrderItem.objects.get(order_id=order_id, product_id=product_id)
    except OrderItem.DoesNotExist:
        return Response(status=404)
    
    orderitem.delete()
    return Response(status=204)