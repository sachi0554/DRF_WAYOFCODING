from django.db import models
from django.utils import timezone

# Create your models here.

 


class Customers(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    # def __str__(self):
    #     return f"{self.id}-{self.name}"

    @property
    def Orders(self):
        instance = self
        qs = Orders.objects.filter_by_instance(instance)
        return qs


class OrdersManager(models.Manager):
     
    def filter_by_instance(self, instance):
        obj_id = instance.id
        qs = super(OrdersManager, self).filter(customer= obj_id)
        return qs


class Orders(models.Model):
     item = models.CharField(max_length=50)
     price = models.DecimalField(max_digits=5, decimal_places=0)
     customer = models.ForeignKey(Customers , on_delete=models.CASCADE)
     objects = OrdersManager()
     def __str__(self):
         return f"{self.id}"


class ShipmentManager(models.Manager):
     
    def filter_by_instance(self, instance):
        obj_id = instance.id
        qs = super(ShipmentManager, self).filter(order= obj_id)
        return qs

class Shipment(models.Model):
    is_shipped = models.BooleanField(default=False)
    ship_name = models.CharField(max_length=150 )
    order = models.ForeignKey(Orders , on_delete=models.CASCADE)
    objects = ShipmentManager()

    

