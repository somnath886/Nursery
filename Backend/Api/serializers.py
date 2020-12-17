from rest_framework import serializers

from .models import User, Plant, Order

class SaveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_normal_user', 'is_nursery_user']

class SavePlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['name', 'image', 'price', 'Seller']

class SaveOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderedItem', 'sellerId', 'buyer']

class ViewOrderSerializer(serializers.ModelSerializer):
    item = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = ['buyer', 'item']