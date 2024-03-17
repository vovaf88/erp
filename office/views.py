from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .service import PartnerFilter, ProductFilter
from .models import (Product,
                     ProductCategory,
                     MeasureUnit,
                     Partner,
                     MyCompany,
                     Bank,
                     MyBankAccount,
                     PartnerBankAccount,
                     Mytestdoc1,
                     Mytesttab1,
                     )
from .serializers import (ProductSerializer,
                          ProductCategorySerializer,
                          MeasureUnitSerializer,
                          PartnerSerializer,
                          MyCompanySerializer,
                          BankSerializer,
                          MyBankAccountSerializer,
                          PartnerBankAccountSerializer,
                          Mytesttab1Serializer,
                          Mytestdoc1DetailSerializer,
                          Mytestdoc1ListSerializer,
                          )
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


# Product
class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PartnerFilter


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


class Mytestdoc1ListView(APIView):
    def get(self, request):
        docs = Mytestdoc1.objects.all()
        serializer = Mytestdoc1ListSerializer(docs, many=True)
        return Response(serializer.data)


class Mytestdoc1DetailView(APIView):
    def get(self, request, pk):
        docs = Mytestdoc1.objects.get(id=pk)
        serializer = Mytestdoc1DetailSerializer(docs)
        return Response(serializer.data)


class Mytesttab1CreateView(APIView):
    def post(self, request):
        tab = Mytesttab1Serializer(data=request.data)
        if tab.is_valid():
            tab.save()
        return Response(status=201)






