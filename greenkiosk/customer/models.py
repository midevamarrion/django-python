from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=7)
    second_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=7)
    email = models.EmailField()