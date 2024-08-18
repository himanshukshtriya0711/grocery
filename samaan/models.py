from django.db import models

class Grocery(models.Model):
    item = models.TextField(null=True)
    
    remove = models.BooleanField(default=False)
    quantity = models.IntegerField()

    
