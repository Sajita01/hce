from django.db import models
from categories.models import Category

# from products.models import product
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    category= models.ForeignKey(Category , on_delete=models.CASCADE)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    def __str__(self):
        return self.name
    
    