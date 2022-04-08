# Generated by Django 3.2.12 on 2022-04-08 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(help_text='商品ID', unique=True)),
                ('product_name', models.CharField(help_text='商品名称', max_length=30)),
                ('product_description', models.CharField(help_text='商品描述', max_length=200)),
                ('product_price', models.FloatField(help_text='商品价格', max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name': '商品列表',
                'verbose_name_plural': '商品列表',
                'db_table': 'Product_list',
            },
        ),
        migrations.CreateModel(
            name='TestDemo',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_str', models.CharField(max_length=30)),
                ('test_bool', models.BooleanField(null=True)),
                ('test_dec', models.DecimalField(decimal_places=2, max_digits=3)),
                ('test_email', models.EmailField(blank=True, default='', max_length=254)),
                ('test_flo', models.FloatField()),
                ('test_text', models.TextField()),
                ('test_img', models.ImageField(upload_to='')),
                ('test_file', models.FilePathField()),
                ('test_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_details', models.CharField(help_text='商品详情', max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productlist')),
            ],
            options={
                'verbose_name': '商品详情',
                'verbose_name_plural': '商品详情',
                'db_table': 'Product_details',
            },
        ),
    ]