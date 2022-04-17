from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import ProductList
from api.models import ProductDetails
import time


class ProductListSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(source="pub_date", format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = ProductList
        fields = '__all__'


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'
