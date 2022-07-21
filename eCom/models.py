from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    description = models.CharField(max_length=500, default='')
    category = models.CharField(max_length=200, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    numReviews = models.IntegerField(blank=True, default=0)
    countInStock = models.IntegerField(blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    img = models.TextField(default='')

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=True)
    rating = models.IntegerField(blank=True, default=0)
    comment = models.CharField(max_length=500, default='')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating
