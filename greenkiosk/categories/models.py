from django.db import models

# Create your models here.
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=32, default='')