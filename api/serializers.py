from rest_framework import serializers
from api.models import ProductList, ProductDetails


class ProductListSerializer(serializers.ModelSerializer):
    # 在返回json中新增字段，数据源指向数据库字段
    create_time = serializers.DateTimeField(source="pub_date",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)
    # 设置字段必填/非必填
    pub_date = serializers.DateTimeField(required=False)

    class Meta:
        model = ProductList
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'
