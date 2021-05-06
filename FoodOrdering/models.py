from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    contact = models.CharField(max_length=12)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    gender = models.CharField(max_length=10)
    
class Food(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    price = models.FloatField()
    img = models.CharField(max_length=250)
