from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from api.models import ProductList, ProductDetails
from django.template import loader
from django.shortcuts import render, reverse, redirect
from django.utils import timezone
from django.db.models import Q
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


# def insert_product(request):
#     # result = ""
#     if request.method == 'POST' and request.POST:
#         list_data = ProductList()
#         list_data.product_id = request.POST["product_id"]
#         list_data.product_name = request.POST["product_name"]
#         list_data.product_price = request.POST["product_price"]
#         list_data.product_description = request.POST["product_description"]
#         list_data.pub_date = timezone.now()
#         list_data.save()
#         # result = 'success'
#     return redirect(reverse('api:product_list'))

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
        result = '商品添加成功！'
    return render(request, 'app/add_product.html', {'result': result})


def search_product(request):
    product_id = request.GET.get('product_id', None)
    product_name = request.GET.get('product_name', None)
    error_msg = ''
    if not product_id or product_name:
        search_data_list = ProductList.objects.filter(Q(product_id=product_id) | Q(product_name=product_name))
    elif product_id and product_name:
        search_data_list = ProductList.objects.filter(product_id=product_id, product_name=product_name)
    else:
        search_data_list = ProductList.objects.all()
    return render(request, 'app/index.html', {'error_msg': error_msg, 'search_data_list': search_data_list})


def edit_product(request):
    product_id = request.GET.get('product_id')
    product_obj = ProductList.objects.get(product_id=product_id)
    product_objs = ProductList.objects.all()
    content = {
        'product_obj': product_obj,
        'product_objs': product_objs
    }
    return render(request, 'app/edit.html', content)


def edit_save_product(request):
    result = ""
    if request.method == 'POST' and request.POST:
        # 两种修改方法
        product_id = request.POST.get('product_id', None)
        # product_name = request.POST.get('product_name', None)
        # product_price = request.POST.get('product_price', None)
        # product_description = request.POST.get('product_description', None)
        # ProductList.objects.filter(product_id=product_id).update(product_id=product_id,
        #                                                          product_name=product_name,
        #                                                          product_price=product_price,
        #                                                          product_description=product_description)
        product = dict(
            product_id=request.POST.get('product_id', None),
            product_name=request.POST.get('product_name', None),
            product_price=request.POST.get('product_price', None),
            product_description=request.POST.get('product_description', None)
        )
        ProductList.objects.filter(product_id=product_id).update(**product)
        result = '商品修改成功！'
    return render(request, 'app/edit.html', {'result': result})


def delete_product(request):
    product_id = request.GET.get('product_id', None)

    if product_id:
        ProductList.objects.filter(product_id=product_id).delete()
        del_result = '商品删除成功！'
        return render(request, 'app/index.html', {'del_result': del_result})
    else:
        return HttpResponse("商品不存在")
