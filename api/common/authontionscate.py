from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.models import UserRights


class CommAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('token')
        if token:
            token_user = UserRights.objects.filter(token=token).first()
            if token_user:
                return token_user.user, token
            else:
                return AuthenticationFailed('token认证失败')
        else:
            return AuthenticationFailed('token不存在')
