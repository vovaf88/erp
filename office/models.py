from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
    

class MeasureUnit(models.Model):
    name = models.CharField(max_length=128, unique=True)
    short_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.short_name
    

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(default=0)
    service = models.BooleanField(default=False)

    def __str__(self):
        return self.name

