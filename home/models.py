from operator import mod
from re import M, T
from django.db import models
from django.contrib.auth.models import User , auth 

import cloudinary_storage
import cloudinary


# Create your models here.

class category_model(models.Model) :
    category = models.CharField(max_length=255)
    def __str__(self) :
        return self.category

class product_model(models.Model) :
    category = models.ForeignKey(category_model, on_delete=models.CASCADE, null = True)
    top_product = models.BooleanField(default=False)
    name = models.CharField(max_length=255 , null = True)
    price = models.IntegerField(null = True)
    image = models.ImageField(upload_to='images/portfolio/', blank=True, null=True)
    link = models.CharField(max_length=255 , null = True)
    model = models.FileField(upload_to='images/models/', blank=True, null=True)
    description = models.CharField(max_length=255 , null = True)


    def __str__(self):
        return self.name 