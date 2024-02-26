from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    inn = models.CharField(max_length=12, unique=True)
    fiz_lico = models.BooleanField()
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MyCompany(Company):
    short_name = models.CharField(max_length=127)


class Partner(Company):
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    comment = models.TextField(blank=True)


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

