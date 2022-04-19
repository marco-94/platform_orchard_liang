"""
自定义异常处理
"""
from rest_framework.views import exception_handler
from rest_framework.views import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    global message
    response = exception_handler(exc, context)

    for index, value in enumerate(response.data):
        if index == 0:
            key = value
            value = response.data[key]

            if isinstance(value, str):
                message = value
            else:
                message = key + value[0]

    if response is None:
        return Response({
            'message': '服务器错误'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)

    else:
        return Response({
            'message': message,
        }, status=response.status_code, exception=True)

    return response
