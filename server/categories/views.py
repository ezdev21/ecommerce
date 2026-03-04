from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

@api_view(['GET'])
def category_list(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response({'categorys': serializer.data},status=200)

@api_view(['GET'])
def category_detail(request,category_id):    
    try:
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response({'category': serializer.data},status=200)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Category created successfully', 'category': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def category_update(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Category {category_id} updated successfully', 'category': serializer.data},status=200)
        return Response(serializer.errors, status=400)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

@api_view(['DELETE'])
def category_delete(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return Response({'message': f'Category {category_id} deleted successfully'},status=204)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)
