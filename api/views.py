from django.http import HttpResponse, JsonResponse
from api.models import ProductList, ProductDetails
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from django.views import View
from rest_framework import viewsets
from api.serializers import ProductListSerializer


# from api.serializers import ProductDetailsSerializer


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
    return render(request, 'app/index.html', {'error_msg': error_msg, 'response': search_data_list})


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
        product_id = request.POST.get('product_id', None)
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


class ProductListView(viewsets.ModelViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer


# class ProductDetailsView(viewsets.ModelViewSet):
#     queryset = ProductDetails.objects.all()
#     serializer_class = ProductDetailsSerializer

class PdList(View):
    def get_pd(self, request):
        pd_all = ProductList.objects.all()
        pd_list = []
        for pd in pd_all:
            pd_list.append({'product_id': pd.product_id, 'product_name': pd.product_name,
                            'product_description': pd.product_description, 'product_price': pd.product_price})
        return JsonResponse(pd_list, safe=False)
