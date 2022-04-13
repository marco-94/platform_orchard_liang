from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('product_list/', views.product_list, name="product_list"),
    path('product_details/<int:product_id>', views.product_details, name="product_details"),
    path('add_product/', views.add_product, name="add_product"),
    path('insert_product/', views.insert_product, name="insert_product"),
]
