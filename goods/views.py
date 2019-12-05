import json

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_redis import get_redis_connection

from goods.filters import GoodsFilter
from goods.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods
from goods.serializers import MainWheelSerializer, MainNavSerializer, MainMustBuySerializer, MainShopSerializer, \
    MainShowSerializer, FoodTypeSerializer, GoodsSerializer


# def home(request):
#     if request.method == 'GET':
#         return JsonResponse()


@api_view(['GET'])
def home(request):
    # 如果使用redis缓存数据， 类型: hash散列
    # hset key field value
    # hset goods main_wheels MainWheelSerializer(main_wheels, many=True).data
    # hset goods main_navs MainNavSerializer(main_navs, many=True).data
    conn = get_redis_connection()
    redis_main_wheels = conn.hget('goods', 'main_wheels')
    if not redis_main_wheels:
        main_wheels = MainWheel.objects.all()
        new_main_wheels = MainWheelSerializer(main_wheels, many=True).data
        # 存储结果为json格式数据，json.dumps()
        value_wheels = json.dumps(new_main_wheels)
        conn.hset('goods', 'main_wheels', value_wheels)

    redis_main_wheels = conn.hget('goods', 'main_wheels')
    # 存储为字符串类型的结果值，需转换为字典，json.loads()
    old_main_wheels = json.loads(redis_main_wheels)

    redis_main_navs = conn.hget('goods', 'main_navs')
    if not redis_main_navs:
        main_navs = MainNav.objects.all()
        new_main_navs = MainNavSerializer(main_navs, many=True).data
        # 存储结果为json格式数据，json.dumps()
        value_navs = json.dumps(new_main_navs)
        conn.hset('goods', 'main_navs', value_navs)

    redis_main_navs = conn.hget('goods', 'main_navs')
    # 存储为字符串类型的结果值，需转换为字典，json.loads()
    old_main_navs = json.loads(redis_main_navs)

    redis_main_mustbuys = conn.hget('goods', 'main_mustbuys')
    if not redis_main_mustbuys:
        main_mustbuys = MainMustBuy.objects.all()
        new_main_mustbuys = MainMustBuySerializer(main_mustbuys, many=True).data
        # 存储结果为json格式数据，json.dumps()
        value_mustbuys = json.dumps(new_main_mustbuys)
        conn.hset('goods', 'main_mustbuys', value_mustbuys)

    redis_main_mustbuys = conn.hget('goods', 'main_mustbuys')
    # 存储为字符串类型的结果值，需转换为字典，json.loads()
    old_main_mustbuys = json.loads(redis_main_mustbuys)

    redis_main_shops = conn.hget('goods', 'main_shops')
    if not redis_main_shops:
        main_shops = MainShop.objects.all()
        new_main_shops = MainShopSerializer(main_shops, many=True).data
        # 存储结果为json格式数据，json.dumps()
        value_shops = json.dumps(new_main_shops)
        conn.hset('goods', 'main_shops', value_shops)

    redis_main_shops = conn.hget('goods', 'main_shops')
    # 存储为字符串类型的结果值，需转换为字典，json.loads()
    old_main_shops = json.loads(redis_main_shops)

    redis_main_shows = conn.hget('goods', 'main_shows')
    if not redis_main_shows:
        main_shows = MainShow.objects.all()
        new_main_shows = MainShowSerializer(main_shows, many=True).data
        # 存储结果为json格式数据，json.dumps()
        value_shows = json.dumps(new_main_shows)
        conn.hset('goods', 'main_shows', value_shows)

    redis_main_shows = conn.hget('goods', 'main_shows')
    # 存储为字符串类型的结果值，需转换为字典，json.loads()
    old_main_shows = json.loads(redis_main_shows)

    # main_wheels = MainWheel.objects.all()
    # main_navs = MainNav.objects.all()
    # main_mustbuys = MainMustBuy.objects.all()
    # main_shops = MainShop.objects.all()
    # main_shows = MainShow.objects.all()

    res = {
        'main_wheels': old_main_wheels,
        'main_navs': old_main_navs,
        'main_mustbuys': old_main_mustbuys,
        'main_shops': old_main_shops,
        'main_shows': old_main_shows,
    }

    return Response(res)


class FoodTypeView(viewsets.GenericViewSet,
                   mixins.ListModelMixin):

    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class MarketView(viewsets.GenericViewSet,
                 mixins.ListModelMixin):

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_class = GoodsFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        # 分类
        typeid = self.request.query_params.get('typeid')
        foodtype = FoodType.objects.filter(typeid=typeid).first()
        foodtypenames = foodtype.childtypenames.split('#')
        foodtypenames_list = []
        for i in foodtypenames:
            # i ==> '全部分类:0'

            data = {
                'child_name': i.split(':')[0],
                'child_value': i.split(':')[1]
            }
            foodtypenames_list.append(data)

        # 推导式写法
        # foodtypenames_list = [{'child_name': i.split(':')[0], 'child_value': i.split(':')[1]} for i in foodtypenames]

        rule_list = [
            {'order_name': '综合排序', 'order_value': 0},
            {'order_name': '价格升序', 'order_value': 1},
            {'order_name': '价格降序', 'order_value': 2},
            {'order_name': '销量升序', 'order_value': 3},
            {'order_name': '销量降序', 'order_value': 4},
        ]
        res = {
            'goods_list': serializer.data,
            'foodtype_childname_list': foodtypenames_list,  # 需要child_name和child_value
            'order_rule_list': rule_list
        }

        return Response(res)




