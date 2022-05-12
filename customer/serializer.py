
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.fields import SerializerMethodField
from django.db import models
from .models import Customers, Orders,Shipment
from .service import customer_create


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('name','address','phone','email')

    def create(self, validated_data):
        return customer_create(**validated_data)

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'



class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrdersshipmentSerializer(serializers.ModelSerializer):
    shipment =  SerializerMethodField()
    class Meta:
        model = Orders
        fields = '__all__'

    def get_shipment(self, obj):
        c_qs = Shipment.objects.filter_by_instance(obj)
        shipment = ShipmentSerializer(c_qs, many=True).data
        return shipment

class CustomerCreateResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = CustomerSerializer()



#primary key by get order 
class CustomerDetailsSerializer(serializers.ModelSerializer):
    order =  SerializerMethodField()
    class Meta:
        model = Customers
        fields = ('id', 'name', 'order')

    def get_order(self, obj):
            c_qs = Orders.objects.filter_by_instance(obj)
            order = OrdersshipmentSerializer(c_qs, many=True).data
            return order


 