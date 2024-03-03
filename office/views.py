from django.shortcuts import render
from .models import (Product,
                     ProductCategory,
                     MeasureUnit,
                     Partner,
                     MyCompany,
                     Bank,
                     MyBankAccount,
                     PartnerBankAccount,
                     )
from .serializers import (ProductSerializer,
                          ProductCategorySerializer,
                          MeasureUnitSerializer,
                          PartnerSerializer,
                          MyCompanySerializer,
                          BankSerializer,
                          MyBankAccountSerializer,
                          PartnerBankAccountSerializer,
                          )
from rest_framework import generics


# Product
class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Product Category
class ProductCategoryAPIList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


# Measure Unit
class MeasureUnitAPIList(generics.ListCreateAPIView):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer


# Partner
class PartnerAPIList(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerAPIUpdate(generics.UpdateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


# My Company
class MyCompanyAPIUpdate(generics.UpdateAPIView):
    queryset = MyCompany.objects.all()
    serializer_class = MyCompanySerializer


# Bank
class BankAPIList(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankAPIUpdate(generics.UpdateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


# My Bank Account
class MyBankAccountAPIList(generics.ListCreateAPIView):
    queryset = MyBankAccount.objects.all()
    serializer_class = MyBankAccountSerializer


class MyBankAccountAPIUpdate(generics.UpdateAPIView):
    queryset = MyBankAccount.objects.all()
    serializer_class = MyBankAccountSerializer


class MyBankAccountAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyBankAccount.objects.all()
    serializer_class = MyBankAccountSerializer


# Partner Bank Account
class PartnerBankAccountAPIList(generics.ListCreateAPIView):
    queryset = PartnerBankAccount.objects.all()
    serializer_class = PartnerBankAccountSerializer


class PartnerBankAccountAPIUpdate(generics.UpdateAPIView):
    queryset = PartnerBankAccount.objects.all()
    serializer_class = PartnerBankAccountSerializer


class PartnerBankAccountAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartnerBankAccount.objects.all()
    serializer_class = PartnerBankAccountSerializer



