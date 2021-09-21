from rest_framework import serializers

from .models import Cart, CartItem
from customer.models import Customer
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data: dict):
        customer = Customer.objects.filter(customer_uuid=validated_data.get('customer')).first()
        validated_data['customer'] = customer
        cart = Cart(**validated_data)
        cart.save()
        return cart


class CartItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # cart = CartSerializer(read_only=True)
    # product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'
