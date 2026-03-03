from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Store
from .serializers import StoreSerializer

@api_view(['GET'])
def store_list(request):
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response({'stores': serializer.data}, status=200)

@api_view(['GET'])
def store_detail(request, store_id):
    try:
        store = Store.objects.get(id=store_id)
        serializer = StoreSerializer(store)
        return Response({'store': serializer.data},status=200)
    except Store.DoesNotExist:
        return Response({'error': 'Store not found'},status=404)
    
@api_view(['POST'])
def store_create(request):
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Store created successfully', 'store': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def store_update(request, store_id):
    try:
        store = Store.objects.get(id=store_id)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Store {store_id} updated successfully', 'store': serializer.data},status=200)
        return Response(serializer.errors, status=400)
    except Store.DoesNotExist:
        return Response({'error': 'Store not found'}, status=404)
    
@api_view(['DELETE'])
def store_delete(request, store_id):
    try:
        store = Store.objects.get(id=store_id)
        store.delete()
        return Response({'message': f'Store {store_id} deleted successfully'},status=204)
    except Store.DoesNotExist:
        return Response({'error': 'Store not found'}, status=404)
    
@api_view(['GET'])
def store_products(request, store_id):
    try:
        store = Store.objects.get(id=store_id)
        products = store.products.all()
        serializer = StoreSerializer(store)
        return Response({'store': serializer.data, 'products': [product.name for product in products]},status=200)
    except Store.DoesNotExist:
        return Response({'error': 'Store not found'}, status=404)    