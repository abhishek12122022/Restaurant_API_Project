from rest_framework import serializers
from .models import MenuItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug', 'title']
    
    def create(self, validated_data):
        return super().create(validated_data)
    

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'category']
        extra_kwargs = {
            'price':{'min_value': 0},
            'inventory':{'min_value': 2}
        }

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance, created = Category.objects.get_or_create(title__iexact=category_data['title'], defaults=category_data)
        menu_item = MenuItem.objects.create(category=category_instance, **validated_data)

        return menu_item