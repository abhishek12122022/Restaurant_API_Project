from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class MenuItemList(APIView):
    def get(self, request, format=None):
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        l_price = request.query_params.get('l_price')
        r_price = request.query_params.get('r_price')
        ordering = request.query_params.get('ordering')
        if category_name:
            items = items.filter(category__title__icontains=category_name)
        if l_price:
            items = items.filter(price__gte=l_price)
        if r_price:
            items = items.filter(price__lte=r_price)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)

class MenuItemDetail(APIView):
    def get(self, request, pk, format=None):
        item = get_object_or_404(MenuItem, pk=pk)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        item = get_object_or_404(MenuItem, pk=pk)
        serialized_item = MenuItemSerializer(item, data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk, format=None):
        item = get_object_or_404(MenuItem, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)