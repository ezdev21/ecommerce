from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from products.serializers import ProductSerializer
from .models import Tag
from .serializers import TagSerializer

# Create your views here.
@api_view(['GET'])
def tag_list(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response({"tags": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    serializer = TagSerializer(tag)
    return Response(serializer.data)

@api_view(['POST'])
def tag_create(request):
    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def tag_update(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    serializer = TagSerializer(tag, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def tag_delete(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def tag_products(request, tag_id):
  try:  
    tag = Tag.objects.get(id=tag_id)
    products = tag.products.all()
    serializer = ProductSerializer(products, many=True)
    return Response({"products": serializer.data}, status=status.HTTP_200_OK)    
  except Tag.DoesNotExist:
        return Response({'error': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)   
  