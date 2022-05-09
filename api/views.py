from django.http import HttpResponse
from api.models import ProductList, ProductDetails, UserInfo, UserRights
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from django_filters import rest_framework
from api.serializers import ProductListSerializer, ProductDetailsSerializer, UserInfoSerializer, UserRightsSerializer
from api.filter import ProductListFilter, UserListFilter, UserRightsFilter
from api.common.page_number import PageNumber
from rest_framework.decorators import action
import uuid


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


class UserListView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.filter(is_delete=0).all()
    serializer_class = UserInfoSerializer
    filter_class = UserListFilter
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering = ['-created_tm']


class UserRightsView(viewsets.ModelViewSet):
    queryset = UserRights.objects.filter().all()
    serializer_class = UserRightsSerializer
    filter_class = UserRightsFilter
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering = ['-created_tm']


class ProductListView(viewsets.ModelViewSet):
    queryset = ProductList.objects.filter(is_delete=0).all()
    serializer_class = ProductListSerializer
    filter_class = ProductListFilter
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering = ['-created_tm']


class ProductDetailsView(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    pagination_class = PageNumber
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering = ['-pub_date']


class UserView(APIView):
    def get_user(self, request):
        if request.method == 'GET':
            user_all = UserInfo.objects.all()
            user_list = PageNumber()
            user_obj = user_list.paginate_queryset(queryset=user_all, request=request, view=self)
            serializer = UserInfoSerializer(user_obj, many=True)
            return Response(serializer.data)

    @staticmethod
    def create_user(request, *args, **kwargs):
        if request.method == "POST":
            serializer = UserInfoSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)


class LoginView(APIView):
    @staticmethod
    def login_in(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = UserInfo.objects.filter(user_name=username, user_psd=password).first()
        print(user)
        if request.method == "POST":
            if user:
                token = uuid.uuid4()
                UserRights.objects.update_or_create(default={'token': token}, user=user)
                return Response({'code': 100, 'msg': '成功', 'token': token})
            else:
                return Response({'code': 101, 'msg': '失败，账号错误或密码错误'})


class PdList(APIView):
    def get_product_list(self, request, *args, **kwargs):
        """
        商品列表信息
        """
        if request.method == "GET":
            pd_all = ProductList.objects.all()
            pd_product_list = PageNumber()
            pd_obj = pd_product_list.paginate_queryset(queryset=pd_all, request=request, view=self)
            serializer = ProductListSerializer(pd_obj, many=True)
            return Response(serializer.data)

    @staticmethod
    def create_product(request, *args, **kwargs):
        if request.method == "POST":
            serializer = ProductListSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)

    @staticmethod
    def update_product(request, pk):
        if request.method == "PUT":
            product = ProductList.objects.filter(pk=pk).first()
            serializer = ProductListSerializer(data=request.data, instance=product)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)

    @action(methods=['delete'], detail=False)
    def delete_product(self, request, pk):
        if request.method == "DELETE":
            product = ProductList.objects.filter(id=pk).first()
            if product:
                product.delete()

    # def get_pd_details(self, request):
    #     pd_details_all = ProductDetails.objects.all()
    #     pd_details = []
