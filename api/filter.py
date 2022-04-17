import django_filters
from .models import *


class ProductListFilter(django_filters.rest_framework.FilterSet):
    product_id = django_filters.NumberFilter(field_name='product_id', lookup_expr='exact')
    product_name = django_filters.CharFilter(field_name='product_name', lookup_expr='icontains')
    product_description = django_filters.CharFilter(field_name='product_description', lookup_expr='icontains')
    product_price = django_filters.CharFilter(field_name='product_price', lookup_expr='icontains')

    class Meta:
        model = ProductList
        fields = ['product_id', 'product_name', 'product_description', 'product_price']
