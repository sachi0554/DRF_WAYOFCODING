from django.utils import timezone
from .models import Customers

 

def customer_create(* _, **customer) -> Customers:
    obj = Customers.objects.create(**customer)

    obj.full_clean()
    obj.save()

    return obj