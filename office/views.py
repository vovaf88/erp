from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .record_to_registers import add_goods_to_stock, remove_goods_from_stock, increase_our_credit, decrease_our_credit, update_our_credit
from .service import PartnerFilter, ProductFilter
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
                     MoneyOnBank,
                     MoneyOffBank,
                     )
from .serializers import (ProductSerializer,
                          ProductCategorySerializer,
                          MeasureUnitSerializer,
                          PartnerSerializer,
                          MyCompanySerializer,
                          BankSerializer,
                          MyBankAccountSerializer,
                          PartnerBankAccountSerializer,
                          PurchaseOfGoodListSerializer,
                          PurchaseOfGoodDetailSerializer,
                          StrOfTabPurchaseOfGoodListSerializer,
                          SaleOfGoodListSerializer,
                          SaleOfGoodDetailSerializer,
                          StrOfTabSaleOfGoodListSerializer,
                          MoneyOnBankSerializer,
                          MoneyOffBankSerializer,
                          MoneyOffBankDetailSerializer,
                          MoneyOnBankDetailSerializer,
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


# Documents
# PurchaseOfGood
class PurchaseOfGoodListView(generics.ListCreateAPIView):
    queryset = PurchaseOfGood.objects.all()
    serializer_class = PurchaseOfGoodListSerializer


class PurchaseOfGoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOfGood.objects.all()
    serializer_class = PurchaseOfGoodListSerializer

    def get(self, request, pk):
        doc = PurchaseOfGood.objects.get(id=pk)
        serializer = PurchaseOfGoodDetailSerializer(doc)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        print('update sale')
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        #update_our_credit(self.request.data, instance.pk)


        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

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


class SaleOfGoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleOfGood.objects.all()
    serializer_class = SaleOfGoodListSerializer

    def get(self, request, pk):
        doc = SaleOfGood.objects.get(id=pk)
        serializer = SaleOfGoodDetailSerializer(doc)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        print('update sale')
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        #update_our_credit(self.request.data, instance.pk)


        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


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


# Money on bank account
class MoneyOnBankAPIList(generics.ListCreateAPIView):
    queryset = MoneyOnBank.objects.all()
    serializer_class = MoneyOnBankSerializer

    def post(self, request):
        doc = MoneyOnBankSerializer(data=request.data)
        if doc.is_valid():
            doc.save()
        increase_our_credit(doc.data)
        return Response(status=201)


class MoneyOnBankAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyOnBank.objects.all()
    serializer_class = MoneyOnBankSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        update_our_credit(self.request.data, instance.pk)


        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class MoneyOnBankAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyOnBank.objects.all()
    serializer_class = MoneyOnBankSerializer


# Money off bank account
class MoneyOffBankAPIList(generics.ListCreateAPIView):
    queryset = MoneyOffBank.objects.all()
    serializer_class = MoneyOffBankSerializer

    def post(self, request):
        doc = MoneyOffBankSerializer(data=request.data)
        if doc.is_valid():
            doc.save()
        decrease_our_credit(doc.data)
        return Response(status=201)


class MoneyOffBankAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyOffBank.objects.all()
    serializer_class = MoneyOffBankSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        update_our_credit(self.request.data, instance.pk)


        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class MoneyOffBankAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyOffBank.objects.all()
    serializer_class = MoneyOffBankDetailSerializer


