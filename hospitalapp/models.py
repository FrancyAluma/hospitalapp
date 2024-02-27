from django.db import models

# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=200,default="francy aluma")
    username = models.CharField(max_length=50,default="francy aluma")
    email = models.EmailField(default="<EMAIL>")
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=100,default="francy aluma")
    date = models.DateField(default="2020-05-21")

    def __str__(self):
        return self.fullname

class Products(models.Model):
    product_name = models.CharField(max_length=200, default="poisson")
    product_price = models.CharField(max_length=50, default="poisson")
    product_quantity = models.IntegerField(default="<combien>")


    def __str__(self):
        return self.product_name