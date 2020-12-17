from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    is_normal_user = models.BooleanField(default=False)
    is_nursery_user = models.BooleanField(default=False)

class Plant(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, blank=True)
    price = models.FloatField(blank=False)
    Seller = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    orderedItem = models.ForeignKey(Plant, on_delete=models.CASCADE)
    buyer = models.CharField(max_length=200)
    sellerId = models.ForeignKey(User, on_delete=models.CASCADE)