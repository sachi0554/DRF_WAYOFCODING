from django.utils import timezone
from .models import Customers
from lib.event import post_event


def customer_create(* _, **customer) -> Customers:
    obj = Customers.objects.create(**customer)

    obj.full_clean()
    obj.save()
    post_event("user_registered", obj)
    return obj