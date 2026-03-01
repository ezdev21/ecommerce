from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer

@api_view(['GET'])
def cart_list(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response({'carts': serializer.data})

@api_view(['GET'])
def cart_detail(request,cart_id):    
    try:
        cart = Cart.objects.get(id=cart_id)
        serializer = CartSerializer(cart)
        return Response({'cart': serializer.data})
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=404)

@api_view(['POST'])
def cart_create(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Cart created successfully', 'cart': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def cart_update(request, cart_id):
    try:
        cart = Cart.objects.get(id=cart_id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Cart {cart_id} updated successfully', 'cart': serializer.data})
        return Response(serializer.errors, status=400)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=404)

@api_view(['DELETE'])
def cart_delete(request, cart_id):
    try:
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        return Response({'message': f'Cart {cart_id} deleted successfully'})
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=404)
