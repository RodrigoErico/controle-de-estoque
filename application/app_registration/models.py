from django.db import models

class Product(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=50)
    stock = models.PositiveSmallIntegerField()
    
    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.item, self.stock)
    
    