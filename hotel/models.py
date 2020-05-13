from django.db import models

# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    venue_type = models.CharField(max_length=200)
