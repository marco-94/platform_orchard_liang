from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('product_list/', views.product_list, name="product_list"),
    path('product_details/<int:product_id>', views.product_details, name="product_details"),
    path('add_product/', views.add_product, name="add_product"),
    path('insert_product/', views.insert_product, name="insert_product"),
    path('search_product/', views.search_product, name="search_product"),
    path('delete_product/', views.delete_product, name="delete_product"),
    path('edit_product/', views.edit_product, name="edit_product"),
    path('edit_save_product/', views.edit_save_product, name="edit_save_product"),
]
