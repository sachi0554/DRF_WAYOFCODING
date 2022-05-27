
from django.contrib import admin
 

from django.urls import path
from .views import WardCreateView

urlpatterns = [
    path('create/', WardCreateView.as_view(), name="create"),
    
]
