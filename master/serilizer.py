from rest_framework import serializers, status
from .models import Wards

class WardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wards
        fields = '__all__'