from django.db import models
import datetime
from django.utils.timezone import now


DOCUMENT_TYPE = {
    'Sell': "Продажа",
    'Buy': "Покупка",
    'Bank_on': "Поступление денег",
    'Bank_off': "Списание денег",
}


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


class Doc(models.Model):
    operation = models.CharField(choices=DOCUMENT_TYPE, max_length=20)

    def __str__(self):
        return f'{DOCUMENT_TYPE[self.operation]} номер {self.pk}'


class TradeDoc(Doc):
    pass


class BankDoc(Doc):
    pass


class TabDoc(models.Model):
    pass


class PurchaseOfGood(TradeDoc):
    number = models.CharField(max_length=7, blank=True, null=True,)
    doc_date = models.DateTimeField()
    #operation = models.ForeignKey(Operation, on_delete=models.SET_NULL, blank=True, null=True, related_name='purchase')
    my_company = models.ForeignKey(MyCompany, on_delete=models.CASCADE, blank=True, null=True, related_name='purchase')
    partner = models.ForeignKey(Partner, blank=True, null=True, on_delete=models.SET_NULL, related_name='purchase')
    summa = models.DecimalField(max_digits=8, decimal_places=2)


class StrOfTabPurchaseOfGood(TabDoc):
    doc = models.ForeignKey(PurchaseOfGood, on_delete=models.CASCADE, related_name='str_purchase')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='str_purchase')
    count = models.DecimalField(max_digits=6, decimal_places=3)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    summa = models.DecimalField(max_digits=8, decimal_places=2)


class SaleOfGood(TradeDoc):
    number = models.CharField(max_length=7, blank=True, null=True,)
    doc_date = models.DateTimeField()
    #operation = models.ForeignKey(Operation, on_delete=models.SET_NULL, blank=True, null=True, related_name='sale')
    my_company = models.ForeignKey(MyCompany, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='sale')
    partner = models.ForeignKey(Partner, blank=True, null=True, on_delete=models.SET_NULL, related_name='sale')
    summa = models.DecimalField(max_digits=8, decimal_places=2)


class StrOfTabSaleOfGood(TabDoc):
    doc = models.ForeignKey(SaleOfGood, on_delete=models.CASCADE, related_name='str_sale')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='str_sale')
    count = models.DecimalField(max_digits=6, decimal_places=3)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    summa = models.DecimalField(max_digits=8, decimal_places=2)


class RemainingStock(models.Model):
    doc = models.ForeignKey(TradeDoc, on_delete=models.CASCADE, related_name='stock')
    str_doc = models.ForeignKey(TabDoc, on_delete=models.CASCADE, related_name='stock')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='stock')
    count = models.DecimalField(max_digits=6, decimal_places=3)


class CostOfGoods(models.Model):
    doc = models.ForeignKey(TradeDoc, on_delete=models.CASCADE, related_name='cost_of_goods')
    str_doc = models.ForeignKey(TabDoc, on_delete=models.CASCADE, related_name='cost_of_goods')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='cost_of_goods')
    count = models.DecimalField(max_digits=6, decimal_places=3)
    summa = models.DecimalField(max_digits=8, decimal_places=2)


class SettlementsWithPartners(models.Model):
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE, related_name='settelments')
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='settelments')
    summa = models.DecimalField(max_digits=8, decimal_places=2)


class Revenue(models.Model):
    doc = models.ForeignKey(TradeDoc, on_delete=models.CASCADE, related_name='revenue')
    str_doc = models.ForeignKey(TabDoc, on_delete=models.CASCADE, related_name='revenue')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='revenue')
    count = models.DecimalField(max_digits=6, decimal_places=3)
    summa = models.DecimalField(max_digits=8, decimal_places=2)


class MoneyOnBank(BankDoc):
    number = models.CharField(max_length=7, blank=True, null=True,)
    doc_date = models.DateTimeField()
    #operation = models.ForeignKey(Operation, on_delete=models.SET_NULL, blank=True, null=True, related_name='moneyon')
    my_company = models.ForeignKey(MyCompany, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='moneyon')
    partner = models.ForeignKey(Partner, blank=True, null=True, on_delete=models.SET_NULL, related_name='moneyon')
    summa = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Поступление на счет от {self.partner}'


class MoneyOffBank(BankDoc):
    number = models.CharField(max_length=7, blank=True, null=True,)
    doc_date = models.DateTimeField()
    #operation = models.ForeignKey(Operation, on_delete=models.SET_NULL, blank=True, null=True, related_name='moneyoff')
    my_company = models.ForeignKey(MyCompany, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='moneyoff')
    partner = models.ForeignKey(Partner, blank=True, null=True, on_delete=models.SET_NULL, related_name='moneyoff')
    summa = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Списание со счета партнеру {self.partner}'

