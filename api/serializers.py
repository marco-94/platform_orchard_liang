from rest_framework import serializers
from api.models import ProductList, ProductDetails, UserInfo, UserRights


class UserInfoSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(source="created_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)
    update_time = serializers.DateTimeField(source="updated_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)

    class Meta:
        model = UserInfo
        exclude = ('created_tm', 'updated_tm', 'is_delete')


class UserRightsSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(source="created_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)
    update_time = serializers.DateTimeField(source="updated_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)

    class Meta:
        model = UserRights
        exclude = ('created_tm', 'updated_tm')


class ProductListSerializer(serializers.ModelSerializer):
    # 在返回json中新增字段，数据源指向数据库字段
    create_time = serializers.DateTimeField(source="created_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)
    update_time = serializers.DateTimeField(source="updated_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)

    class Meta:
        model = ProductList
        # 映射全部字段
        # fields = '__all__'
        # 映射指定字段
        # fields = ('id', 'product_id', 'product_name')
        # 排除字段
        exclude = ('created_tm', 'updated_tm', 'is_delete', 'pub_date')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'
