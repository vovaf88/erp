import json

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from django.urls import reverse

from office.models import (Product,
                           ProductCategory,
                           Partner,
                           PartnerBankAccount,
                           PurchaseOfGood,
                           StrOfTabPurchaseOfGood,
                           Bank,
                           MyBankAccount,
                           MeasureUnit)

from office.serializers import (ProductSerializer,
                                PartnerBankAccountSerializer,
                                StrOfTabPurchaseOfGoodListSerializer,
                                PartnerSerializer,
                                MyBankAccountSerializer,
                                PurchaseOfGoodListSerializer,
                                PurchaseOfGoodDetailSerializer,
                                BankSerializer)


class ProductApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.category1 = ProductCategory.objects.create(name='test_cat1')
        self.category2 = ProductCategory.objects.create(name='test_cat2')
        self.measure_unit = MeasureUnit.objects.create(name='metr', short_name='m')

        self.product = Product.objects.create(
            name='test_prod1', description='test_prod 1',
            category=self.category1, measure_unit=self.measure_unit,
            price=100, service=False
        )
        self.product = Product.objects.create(
            name='test_prod2', description='test_prod 2',
            category=self.category1, measure_unit=self.measure_unit,
            price=200, service=False
        )
        self.product = Product.objects.create(
            name='test_prod3', description='test_prod 3',
            category=self.category2, measure_unit=self.measure_unit,
            price=300, service=False
        )

    def test_get(self):
        url = '/api/v1/products/'
        print(url)
        response = self.client.get(url)
        products = Product.objects.all()
        serializer_data = ProductSerializer(products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        #print(serializer_data[0]['price'])
        self.assertEqual(serializer_data[0]['price'], 100.0)



