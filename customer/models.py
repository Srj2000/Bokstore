from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile= models.IntegerField()
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()

class buyers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_by=models.CharField(max_length=20)
    item= models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    price=models.IntegerField()
    
