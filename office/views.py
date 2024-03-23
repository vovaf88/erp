from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .record_to_registers import add_goods_to_stock, remove_goods_from_stock
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
                     PurchaseOfGood,
                     StrOfTabPurchaseOfGood,
                     StrOfTabSaleOfGood,
                     SaleOfGood,
                     RemainingStock,
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
                          PurchaseOfGoodListSerializer,
                          PurchaseOfGoodDetailSerializer,
                          StrOfTabPurchaseOfGoodListSerializer,
                          SaleOfGoodListSerializer,
                          SaleOfGoodDetailSerializer,
                          StrOfTabSaleOfGoodListSerializer,
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


# Test document
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


# Documents
# PurchaseOfGood
class PurchaseOfGoodListView(generics.ListCreateAPIView):
    queryset = PurchaseOfGood.objects.all()
    serializer_class = PurchaseOfGoodListSerializer


class PurchaseOfGoodDetailView(APIView):
    def get(self, request, pk):
        doc = PurchaseOfGood.objects.get(id=pk)
        serializer = PurchaseOfGoodDetailSerializer(doc)
        return Response(serializer.data)


class StrOfTabPurchaseOfGoodCreateView(generics.CreateAPIView):
    queryset = StrOfTabPurchaseOfGood.objects.all()
    serializer_class = StrOfTabPurchaseOfGoodListSerializer

    def post(self, request):
        tab = StrOfTabPurchaseOfGoodListSerializer(data=request.data)
        if tab.is_valid():
            tab.save()
        add_goods_to_stock(tab.data)
        return Response(status=201)


# SaleOfGood
class SaleOfGoodListView(generics.ListCreateAPIView):
    queryset = SaleOfGood.objects.all()
    serializer_class = SaleOfGoodListSerializer


class SaleOfGoodDetailView(APIView):
    def get(self, request, pk):
        doc = SaleOfGood.objects.get(id=pk)
        serializer = SaleOfGoodDetailSerializer(doc)
        return Response(serializer.data)


class StrOfTabSaleOfGoodCreateView(generics.CreateAPIView):
    queryset = StrOfTabSaleOfGood.objects.all()
    serializer_class = StrOfTabSaleOfGoodListSerializer

    def post(self, request):
        tab = StrOfTabSaleOfGoodListSerializer(data=request.data)
        if tab.is_valid():
            tab.save()
        success = remove_goods_from_stock(tab.data)
        if success:
            return Response(status=201)
        else:
            return Response(status=403)

