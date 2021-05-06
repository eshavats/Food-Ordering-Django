from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    price = models.FloatField()
    img = models.CharField(max_length=250)
