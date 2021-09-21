from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartView(APIView):
    def post(self, request) -> Response:
        if Cart.objects.filter(customer=request.data.get('customer')).filter(checked_out=False).first():
            return Response('You already have an active cart', status=status.HTTP_400_BAD_REQUEST)
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetailView(APIView):
    def get(self, request, cart_id):
        cart = Cart.objects.filter(id=cart_id).filter(checked_out=False).first()
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartItemsView(APIView):
    def get(self, request, cart_id):
        items = CartItem.objects.filter(cart__id=cart_id).all()
        serializer = CartItemSerializer(instance=items, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, cart_id: int):
        data = request.data
        data['cart'] = cart_id
        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDetails(APIView):
    def get(self, request, cart_id: int, item_id: int):
        item = CartItem.objects.filter(cart__id=cart_id).filter(id=item_id).first()
        print(item)
        serializer = CartItemSerializer(item)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, cart_id: int, item_id: int):
        item = CartItem.objects.filter(id=item_id).first()
        data = request.data
        data['cart'] = cart_id
        serializer = CartItemSerializer(instance=item, data=data, partial=True)
        if serializer.is_valid():
            serializer.update(item, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompleteActiveChatView(APIView):
    def put(self, request, chat_id):
        cart = Cart.objects.filter(customer__chat_id=chat_id).filter(checked_out=False).first()
        cart.checked_out = True
        cart.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
