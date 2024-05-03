from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length= 100, null= False, blank= False, unique=True)
    class Meta():
        db_table = 'brand'
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length= 100, null= False, blank= False)
    description = models.TextField()
    price = models.FloatField(null= False, blank= False)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)

    class Meta():
        db_table = 'product'

    def __str__(self):
        return self.name
    