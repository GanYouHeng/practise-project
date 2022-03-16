from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.core.cache import cache

from user.models import AXFUser
from user.serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from utils.error import PramsException


class UserView(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin):

    # 用户相关的数据
    queryset = AXFUser.objects.all()
    # 序列化
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        # 从redis中获取数据
        user_id = cache.get(token)
        user = AXFUser.objects.filter(id=user_id).first()
        # 序列化， 调用UserSerializer进行序列化user对象
        serializer = self.get_serializer(user)
        res = {
            'user_info': serializer.data
        }
        return Response(res)

    @list_route(methods=['POST'], serializer_class=UserRegisterSerializer)
    def register(self, request):
        # /api/user/user/register/  POST
        # 校验参数
        serializers = self.get_serializer(data=request.data)
        # 如果校验失败，直接往外抛异常
        result = serializers.is_valid(raise_exception=False)
        if not result:
            raise PramsException({'code': 1004, 'msg': '注册参数有误'})
        # 注册功能
        data = serializers.register_data(serializers.data)
        return Response(data)

    @list_route(methods=['POST'], serializer_class=UserLoginSerializer)
    def login(self, request):
        serializers = self.get_serializer(data=request.data)
        result = serializers.is_valid(raise_exception=False)
        if not result:
            raise PramsException({'code': 1007, 'msg': '参数出错'})
        # 登录功能
        res = serializers.login_data(serializers.data)
        return Response(res)




 
