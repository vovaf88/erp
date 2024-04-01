from rest_framework import serializers
from .models import (Product,
                     ProductCategory,
                     MeasureUnit,
                     Partner,
                     MyCompany,
                     Bank,
                     MyBankAccount,
                     PartnerBankAccount,
                     PurchaseOfGood,
                     StrOfTabPurchaseOfGood,
                     StrOfTabSaleOfGood,
                     SaleOfGood,
                     RemainingStock,
                     MoneyOffBank,
                     MoneyOnBank,
                     )


class ProductSerializer(serializers.ModelSerializer):
    measure_unit = serializers.SlugRelatedField(slug_field='name', read_only=False, queryset=MeasureUnit.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', read_only=False, queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'measure_unit', 'category', 'price', 'service']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('__all__')


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ('__all__')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('__all__')


class MyCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCompany
        fields = ('__all__')


class MyCompanyForBankAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCompany
        fields = ['name']


class MyBankAccountSerializer(serializers.ModelSerializer):
    bank = serializers.SlugRelatedField(slug_field='name', read_only=True)
    owner = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = MyBankAccount
        fields = ['id', 'number', 'owner', 'bank']


class PartnerBankAccountSerializer(serializers.ModelSerializer):
    bank = serializers.SlugRelatedField(slug_field='name', read_only=True)
    owner = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = PartnerBankAccount
        fields = ['id', 'number', 'owner', 'bank']


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('__all__')


# Documents
# Purchase
class PurchaseOfGoodListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOfGood
        fields = ('__all__')


class StrOfTabPurchaseOfGoodListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StrOfTabPurchaseOfGood
        fields = ('__all__')


class PurchaseOfGoodDetailSerializer(serializers.ModelSerializer):
    str_purchase = StrOfTabPurchaseOfGoodListSerializer(many=True)

    class Meta:
        model = PurchaseOfGood
        fields = ('id', 'number', 'operation', 'my_company', 'partner', 'summa', 'str_purchase')


# Sale
class SaleOfGoodListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleOfGood
        fields = ('__all__')


class StrOfTabSaleOfGoodListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StrOfTabSaleOfGood
        fields = ('__all__')


class SaleOfGoodDetailSerializer(serializers.ModelSerializer):
    str_sale = StrOfTabSaleOfGoodListSerializer(many=True)

    class Meta:
        model = SaleOfGood
        fields = ('id', 'number', 'operation', 'my_company', 'partner', 'summa', 'str_sale')


class MoneyOnBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoneyOnBank
        fields = ('id', 'number', 'doc_date', 'operation', 'my_company', 'partner', 'summa')


class MoneyOnBankDetailSerializer(serializers.ModelSerializer):
    my_company = serializers.SlugRelatedField(slug_field='name', read_only=False, queryset=MyCompany.objects.all())
    partner = serializers.SlugRelatedField(slug_field='name', read_only=False, queryset=Partner.objects.all())

    class Meta:
        model = MoneyOnBank
        fields = ('id', 'number', 'doc_date', 'operation', 'my_company', 'partner', 'summa')


class MoneyOffBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoneyOffBank
        fields = ('id', 'number', 'doc_date', 'operation', 'my_company', 'partner', 'summa')


class MoneyOffBankDetailSerializer(serializers.ModelSerializer):
    my_company = serializers.SlugRelatedField(slug_field='name', read_only=False, queryset=MyCompany.objects.all())
    partner = serializers.SlugRelatedField(slug_field='name', read_only=False, queryset=Partner.objects.all())

    class Meta:
        model = MoneyOffBank
        fields = ('id', 'number', 'doc_date', 'operation', 'my_company', 'partner', 'summa')


class RemainingStockSerializer(serializers.Serializer):
    product = serializers.CharField()
    count = serializers.DecimalField(max_digits=10, decimal_places=2)


