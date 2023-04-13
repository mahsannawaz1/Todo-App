from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.title