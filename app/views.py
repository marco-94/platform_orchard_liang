from django.shortcuts import render
from django.http import HttpResponse
from app.models import ProductList, ProductDetails
from django.template import loader
from django.shortcuts import render
from django.utils import timezone
import time


# Create your views here.
def product_list(request):
    response = ProductList.objects.all()
    context = {'response': response}
    return render(request, 'app/index.html', context)


def product_details(request, product_id):
    response = ProductDetails.objects.all()
    for product in response:
        if product.product_id == product_id:
            return render(request, 'app/details.html', {'response': product})


def add_product(request):
    return render(request, 'app/add_product.html')


def insert_product(request):
    result = ""
    if request.method == 'POST' and request.POST:
        list_data = ProductList()
        list_data.product_id = request.POST["product_id"]
        list_data.product_name = request.POST["product_name"]
        list_data.product_price = request.POST["product_price"]
        list_data.product_description = request.POST["product_description"]
        list_data.pub_date = timezone.now()
        list_data.save()
        result = 'success'
    return render(request, 'app/add_product.html', {'result': result})

