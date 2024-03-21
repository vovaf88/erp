from django_filters import rest_framework as filters
from .models import Product, Partner


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


