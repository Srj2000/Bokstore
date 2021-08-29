from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile= models.IntegerField()
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()

class Addbook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    
    status=models.CharField(max_length=20)


# Create your models here.
