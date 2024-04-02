from django_filters import rest_framework as filters
from .models import Product, Partner, RemainingStock, CostOfGoods, SettlementsWithPartners


class PartnerFilter(filters.FilterSet):
    seller = filters.BooleanFilter()
    buyer = filters.BooleanFilter()
    other = filters.BooleanFilter()

    class Meta:
        model = Partner
        fields = ['seller', 'buyer', 'other']


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['category']


class RemainingStockFilter(filters.FilterSet):
    product = CharFilterInFilter(field_name='product__name', lookup_expr='in')

    class Meta:
        model = RemainingStock
        fields = ['product']


class CostOfGoodsFilter(filters.FilterSet):
    product = CharFilterInFilter(field_name='product__name', lookup_expr='in')

    class Meta:
        model = CostOfGoods
        fields = ['product']


class SettlementsWithPartnersFilter(filters.FilterSet):
    partner = CharFilterInFilter(field_name='partner__name', lookup_expr='in')

    class Meta:
        model = SettlementsWithPartners
        fields = ['partner']

