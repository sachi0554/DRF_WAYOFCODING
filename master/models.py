from django.db import models

# Create your models here.
class Wards(models.Model):
    name = models.CharField(max_length=150)
    file = models.FileField()
    
