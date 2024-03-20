from rest_framework import serializers
from .models import (Product,
                     ProductCategory,
                     MeasureUnit,
                     Partner,
                     MyCompany,
                     Bank,
                     MyBankAccount,
                     PartnerBankAccount,
                     Mytesttab1,
                     Mytestdoc1,
                     PurchaseOfGood,
                     StrOfTabPurchaseOfGood,
                     StrOfTabSaleOfGood,
                     SaleOfGood,
                     RemainingStock,
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


# test doc
class Mytesttab1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mytesttab1
        fields = ('__all__')


class Mytestdoc1DetailSerializer(serializers.ModelSerializer):
    tabs = Mytesttab1Serializer(many=True)
    #products = ProductSerializer(many=True)

    class Meta:
        model = Mytestdoc1
        fields = ('id', 'number', 'doc_date', 'summa', 'tabs')


class Mytestdoc1ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mytestdoc1
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

