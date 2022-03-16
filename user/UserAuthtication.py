"""__author__ = 干友恒"""
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from user.models import AXFUser
from utils.error import PramsException


class UserTokenAuthentication(BaseAuthentication):
    # 认证功能
    def authenticate(self, request):
        try:
            # 三元运算
            token = request.query_params.get('token') if request.query_params.get('token') else request.data.get('token')

            user_id = cache.get(token)
            user = AXFUser.objects.get(pk=user_id)

            # request.user  ==> user
            # request.auth  ==> token
            return user, token
        except:
            raise PramsException({'code': 1009, 'msg': '用户没有登录，没有操作权限'})

 
