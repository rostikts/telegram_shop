from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import CartSerializer, CartItemSerializer
from .services import CartService


class CartView(APIView):
    def post(self, request: HttpRequest) -> Response:
        data = CartService.init_cart(request.data)
        return Response(data, status=status.HTTP_201_CREATED)


class CartDetailView(APIView):
    def get(self, request: HttpRequest, cart_id):
        cart = CartService.get_active_cart_by_id(cart_id)
        data = CartSerializer(instance=cart).data
        return Response(data=data, status=status.HTTP_200_OK)


class CartItemsView(APIView):
    def get(self, request: HttpRequest, cart_id):
        items = CartService().get_all_items_by_cart_id(cart_id)
        data = CartItemSerializer(instance=items, many=True).data
        return Response(data, status.HTTP_200_OK)

    def post(self, request: HttpRequest, cart_id: int):
        data = request.data
        response = CartService().add_item_to_cart(cart_id, data)
        return Response(response, status=status.HTTP_201_CREATED)


class CartItemDetails(APIView):
    def get(self, request: HttpRequest, cart_id: int, item_id: int):
        item = CartService().get_item_from_cart_by_id(cart_id, item_id)
        data = CartItemSerializer(item).data
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, cart_id: int, item_id: int):
        data = request.data
        response = CartService.edit_item_in_cart(data, cart_id, item_id).data
        return Response(response, status=status.HTTP_201_CREATED)


class CompleteActiveChatView(APIView):
    def put(self, request: HttpRequest, cart_id):
        CartService.complete_order(cart_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
