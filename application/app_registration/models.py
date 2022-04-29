from django.db import models

class Product(models.Model):
    code=models.CharField(primary_key=True, max_length=6)
    item=models.CharField(max_length=50)
    stock=models.PositiveBigIntegerField()
    