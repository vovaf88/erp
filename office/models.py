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


class Bank(models.Model):
    bik = models.CharField(max_length=9)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    number = models.CharField(max_length=20)

    class Meta:
        abstract = True


class PartnerBankAccount(BankAccount):
    bank = models.ForeignKey(Bank, blank=True, null=True, on_delete=models.SET_NULL, related_name='partner_bank_acc')
    owner = models.ForeignKey(Partner, blank=True, null=True, on_delete=models.SET_NULL, related_name='partner_bank_acc')

    def __str__(self):
        return f'{self.owner} - {self.number}'


class MyBankAccount(BankAccount):
    bank = models.ForeignKey(Bank, blank=True, null=True, on_delete=models.SET_NULL, related_name='my_bank_acc')
    owner = models.ForeignKey(MyCompany, blank=True, null=True, on_delete=models.SET_NULL, related_name='my_bank_acc')

    def __str__(self):
        return f'{self.owner} - {self.number}'


class Operation(models.Model):
    name = models.CharField(max_length=50)


class Doc(models.Model):
    number = models.CharField(max_length=7)
    doc_date = models.DateTimeField()
    operation = models.ForeignKey(Operation, on_delete=models.SET_NULL, blank=True, null=True, related_name='doc')
    my_company = models.ForeignKey(MyCompany, on_delete=models.CASCADE, related_name='doc')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.operation} номер {self.number} от {self.doc_date}'
