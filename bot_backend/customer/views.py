from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer
from .serializers import CustomerSerializer


class CustomerList(APIView):
    """get list of all users or create a new user"""

    def get(self, request: HttpRequest) -> Response:
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest) -> Response:
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)