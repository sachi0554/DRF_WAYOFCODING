

from django.contrib import admin
 

from django.urls import path
from customer.views import CustomerViewSet,CustomerDetailsView

urlpatterns = [
    path('create/', CustomerViewSet.as_view(), name="create"),
    path('<int:id>', CustomerDetailsView.as_view(), name='detail'),
    
]
