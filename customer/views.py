from rest_framework.mixins import (
    DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .service import customer_create
from .models import Customers
from .serializer import CustomerSerializer, CustomerCreateResponseSerializer,CustomerDetailsSerializer


# Create your views here.

#method 1 with view and Serializer make campact version 

# class CustomerCreateView(APIView):
#     class CustomerSerializer(Serializer):
#          class Meta: 
#              model:Customers
#              fields = '__all__'
#     serializer_class = CustomerSerializer
#     def post(self, request, *args, **kwargs):
#            serializer = self.CustomerSerializer(data=request.data)
#            serializer.is_valid(raise_exception=True)
#            obj = Customers.objects.create(**serializer.validated_data)
#            return Response(data={"id": obj.id}, status=status.HTTP_201_CREATED)


#method 2 with view and Serializer and service
class CustomerViewSet(CreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        request_serializer = CustomerSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        request_serializer.save()

        response_serializer = CustomerCreateResponseSerializer({
            'token': 'randomusertoken',
            'user': request_serializer.instance,
        })
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED
        )


class CustomerDetailsView(RetrieveAPIView):

    queryset = Customers.objects.all()
    serializer_class = CustomerDetailsSerializer
    lookup_field ='id'
 
