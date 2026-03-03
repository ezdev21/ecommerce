from rest_framework.decorators import api_view
from rest_framework.response import Response

from tags.serializers import TagSerializer
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.order_by('-created_at')[:100]
    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data}, status=200)

@api_view(['GET'])
def product_detail(request,product_id):    
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response({'product': serializer.data},status=200)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Product created successfully', 'product': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def product_update(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Product {product_id} updated successfully', 'product': serializer.data},status=200)
        return Response(serializer.errors, status=400)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

@api_view(['DELETE'])
def product_delete(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response({'message': f'Product {product_id} deleted successfully'},status=204)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

@api_view(['GET'])
def product_tags(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        tags = product.tags.all()
        serializer = TagSerializer(tags, many=True)
        return Response({'tags': serializer.data}, status=200)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)