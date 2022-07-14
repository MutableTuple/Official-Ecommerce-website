from operator import mod
from statistics import mode
from turtle import Turtle

from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Authentication(models.Model):
    product_image = models.ImageField(null=True, blank=True, upload_to='images/')
    item_name= models.CharField(max_length=1000, blank=True, null=True)
    item_description= models.TextField(blank=True, null=True)
    amount = models.IntegerField(null=True, blank=True)
    category=models.ManyToManyField('Categories', blank=True)
    is_on_sale = models.BooleanField(default=False, null=True, blank=True)
    sale_amount = models.IntegerField(null=True, blank=True)
    offers= models.TextField(blank=True, null=True)
    

    
    # following = models
    
    def __str__(self):
        return self.item_name

class SellerProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email=models.EmailField(max_length=500, blank=True,null=True)
    def __str__(self):
        return self.user.username


class Categories(models.Model):
    product = models.ManyToManyField(Authentication)
    category_name = models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return self.category_name
