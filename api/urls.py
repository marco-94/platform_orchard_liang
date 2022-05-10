from django.urls import path, re_path
from django.conf.urls import include
from . import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register('product_list_router', views.ProductListView, basename='')
# router.register('product_details_router', views.ProductDetailsView, basename='')


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
    path('login/', obtain_jwt_token),
    path('', include(router.urls)),
]
