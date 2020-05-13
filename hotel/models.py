from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    venue_type = models.CharField(max_length=200)
    veg_price = models.FloatField(max_length=10, default=0)
    max_capacity = models.IntegerField(default=0, null=True)
