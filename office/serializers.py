from rest_framework import serializers
from .models import (Product,
                     ProductCategory,
                     MeasureUnit,
                     Partner,
                     MyCompany,
                     Bank,
                     MyBankAccount,
                     PartnerBankAccount,
                     )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


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


class MyBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBankAccount
        fields = ('__all__')


class PartnerBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerBankAccount
        fields = ('__all__')


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('__all__')

