from rest_framework import status
from rest_framework.exceptions import ValidationError

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartService:

    @staticmethod
    def init_cart(data: dict) -> CartSerializer:
        customer = data.get('customer')
        if Cart.objects.filter(customer=customer).filter(checked_out=False).first():
            raise ValidationError('The cart is already created')
        serializer = CartSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors, code=status.HTTP_400_BAD_REQUEST)
        return serializer

    @staticmethod
    def get_active_cart_by_id(cart_id: int) -> Cart:
        cart = Cart.objects.filter(id=cart_id).filter(checked_out=False).first()
        return cart

    @staticmethod
    def get_all_items_by_cart_id(cart_id: int) -> CartItem:
        items = CartItem.objects.filter(cart__id=cart_id).all()
        return items

    @staticmethod
    def add_item_to_cart(cart_id: int, data: dict) -> CartItemSerializer:
        data['cart'] = cart_id
        serializer = CartItemSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors, code=status.HTTP_400_BAD_REQUEST)
        return serializer

    @staticmethod
    def get_item_from_cart_by_id(cart_id: int, item_id: int) -> CartItem:
        item = CartItem.objects.filter(cart__id=cart_id).filter(id=item_id).first()
        return item

    @staticmethod
    def edit_item_in_cart(data: dict, cart_id: int, item_id: int) -> CartItemSerializer:
        item = CartService.get_item_from_cart_by_id(cart_id, item_id)
        data['cart'] = cart_id
        serializer = CartItemSerializer(instance=item, data=data, partial=True)
        if serializer.is_valid():
            serializer.update(item, serializer.validated_data)
            return serializer
        raise ValidationError(serializer.errors, code=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def complete_order(order_id) -> None:
        order = CartService.get_active_cart_by_id(order_id)
        order.checked_out = True
        order.save()