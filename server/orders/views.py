
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all();
    serializer = OrderSerializer(orders, many=True)
    return Response({'orders': serializer.data}, status=200)
def order_detail(request,order_id):    
    try:
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response({'order': serializer.data},status=200)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)

@api_view(['POST'])
def order_create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Order created successfully', 'order': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def order_update(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Order {order_id} updated successfully', 'order': serializer.data},status=200)
        return Response(serializer.errors, status=400)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)

@api_view(['DELETE'])
def order_delete(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response({'message': f'Order {order_id} deleted successfully'},status=204)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)
    
