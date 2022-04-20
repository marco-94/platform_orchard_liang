from django.db import models
from django.utils import timezone

# Create your models here.


class ProductList(models.Model):
    # 商品id、名称、描述、价格
    product_id = models.IntegerField(help_text="商品ID", unique=True)
    product_name = models.CharField(max_length=30, help_text="商品名称")
    product_description = models.CharField(max_length=200, help_text="商品描述")
    product_price = models.FloatField(max_length=10, help_text="商品价格")
    pub_date = models.DateTimeField('date published', default=timezone.now())

    # 指定数据库表信息
    class Meta:
        db_table = 'Product_list'
        verbose_name = '商品列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product_name


class ProductDetails(models.Model):
    # 商品id、详情
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    product_details = models.CharField(max_length=500, help_text="商品详情")
    pub_date = models.DateTimeField('date published')

    # 指定数据库表信息
    class Meta:
        db_table = 'Product_details'
        verbose_name = '商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product_details


class TestDemo(models.Model):
    # 自增列
    test_id = models.AutoField(primary_key=True)
    # 字符串字段
    test_str = models.CharField(max_length=30)
    # 布尔类型
    test_bool = models.BooleanField(null=True)
    # 允许为空的布尔类型
    # test_bool_null = models.NullBooleanField()
    # 用逗号分割的数字=varchar
    # test_var = models.CommaSeparatedIntegerField(max_length=100)
    # 日期类型 date
    test_date_now = models.DateField().auto_now  # 最后修改日期
    test_date_add = models.DateField().auto_now_add  # 创建日期
    # 日期时间类型
    test_time_now = models.DateTimeField().auto_now  # 最后修改时间
    test_time_add = models.DateTimeField().auto_now_add  # 创建时间
    # 设置了精度的十进制数字,例如要存储的数字最大长度为3位，而带有两个小数位
    test_dec = models.DecimalField(max_digits=3, decimal_places=2)
    # 邮箱检查
    test_email = models.EmailField(blank=True, default="")
    # 浮点数
    test_flo = models.FloatField()
    # text文本类型
    test_text = models.TextField()
    # 图片
    test_img = models.ImageField()
    # 文件
    test_file = models.FilePathField()
    # URL
    test_url = models.URLField()
