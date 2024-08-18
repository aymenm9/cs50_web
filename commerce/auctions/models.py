from django.contrib.auth.models import AbstractUser 
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    img = models.ImageField(upload_to="categories/")

class Listings(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sbid = models.FloatField(default=0.00)
    date = models.DateField()
    active = models.BooleanField(default=True)
    Categorie = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_by = models.ManyToManyField(User, related_name="watchlist")

class Imgs(models.Model):
    url = models.URLField()
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)

class Bids(models.Model):
    bid = models.FloatField()
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)

class Comments(models.Model):
    comment = models.TextField()
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)





