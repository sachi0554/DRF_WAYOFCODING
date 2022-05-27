from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import Wards
from .serilizer import WardsSerializer
# Create your views here.


class WardCreateView(CreateAPIView):
    queryset = Wards.objects.all()
    serializer_class = WardsSerializer
