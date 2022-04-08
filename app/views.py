from django.shortcuts import render
from django.http import HttpResponse
from app.models import ProductList, ProductDetails
from django.template import loader
from django.shortcuts import render


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
