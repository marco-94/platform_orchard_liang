from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list, name="商品列表"),
    path('product_details/<int:product_id>', views.product_details, name="商品详情"),
]
