

from django.contrib import admin
from django.urls import path, include
from customer.views import CustomerViewSet

urlpatterns = [
    path('create/', CustomerViewSet.as_view(), name="create"),
]
