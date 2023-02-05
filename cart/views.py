from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer
from .models import Cart

class CartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user).select_related('menu_item')
        if carts.exists():
            serialized_carts = CartSerializer(carts, many=True)
            return Response(serialized_carts.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "The cart is empty"}, status=status.HTTP_200_OK)

    def post(self, request):
        context = {"request": self.request,}
        serialized_cart = CartSerializer(data=request.data, context=context)
        serialized_cart.is_valid(raise_exception=True)
        serialized_cart.save()
        return Response(serialized_cart.data, status=status.HTTP_201_CREATED)
        
    def delete(self, request):
        carts = Cart.objects.filter(user=request.user).select_related('menu_item')
        if carts.exists():
            carts.delete()
            return Response({"message":"Cart is emptied successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Cart is allready empty"}, status=status.HTTP_200_OK)
        

"""class DeleteCartView(APIView):
    def delete(self, request, menu_item_id):
        carts = request.user.prefetch_related("cart_set")
        if carts.exists():
            carts.delete()
            return Response({"message":"Cart is emptied successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Cart is allready empty"}, status=status.HTTP_200_OK)"""
