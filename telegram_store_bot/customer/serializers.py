from uuid import uuid4
from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    customer_uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data: dict):
        customer = Customer(customer_uuid=uuid4(),
                            phone=validated_data['phone'],
                            chat_id=validated_data['chat_id'])
        customer.save()
        self.validated_data['customer_uuid'] = customer.customer_uuid
        return customer
