from django.db import models

# Create your models here.

class places(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()