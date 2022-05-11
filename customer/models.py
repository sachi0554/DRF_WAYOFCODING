from django.db import models
from django.utils import timezone

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
