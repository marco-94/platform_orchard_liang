"""
自定义分页
"""
from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination


class PageNumber(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = None

    # 重写方法，去掉next等字段，自定义返回
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('list', data),
            ('total_page', self.page.paginator.num_pages),
        ]))
