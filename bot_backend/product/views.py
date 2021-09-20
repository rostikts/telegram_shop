from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):

    def get(self, request) -> Response:
        products = Product.objects.all()
        category = request.query_params.get('category')
        if category:
            products = products.filter(category__title=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductListByCategory(APIView):
    def get(self, request, category: int):
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
