from rest_framework import serializers
from .models import Product, ProductCategory, MeasureUnit


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')