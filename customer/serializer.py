
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.viewsets import GenericViewSet
from .models import Customers
from .service import customer_create


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('name','address','phone','email')

    def create(self, validated_data):
        return customer_create(**validated_data)



class CustomerCreateResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = CustomerSerializer()