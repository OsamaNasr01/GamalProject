from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(unique=True, auto_created=True)

    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    coutry = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, auto_created=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, auto_created=True)
    
    
    def __str__(self):
        return self.name