from rest_framework.serializers import ModelSerializer
from .models import Cart
from MenuItemAPI.serializers import MenuItemSerializer
from rest_framework import serializers

class CartSerializer(ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.IntegerField(write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    

    class Meta:
        model = Cart
        fields = ("id", "menu_item", "menu_item_id", "quantity", "price", "user")
        extra_kwargs = {
            'quantity':{'min_value': 1},
            'price':{'read_only': True}
        }

    
