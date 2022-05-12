from django.contrib import admin

from .models import Customers,Orders,Shipment

# Register your models here.

admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(Shipment)
