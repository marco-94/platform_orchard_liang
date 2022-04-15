from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import ProductList
# from api.models import ProductDetails


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'


# class ProductDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductDetails
#         fields = '__all__'
