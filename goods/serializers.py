"""__author__ = 干友恒"""
 
from rest_framework import serializers

from goods.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods


class MainWheelSerializer(serializers.ModelSerializer):

    class Meta:
        # 序列化模型
        model = MainWheel
        # 序列化字段
        fields = '__all__'


class MainNavSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainNav
        fields = '__all__'


class MainMustBuySerializer(serializers.ModelSerializer):

    class Meta:
        model = MainMustBuy
        fields = '__all__'


class MainShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainShop
        fields = '__all__'


class MainShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainShow
        fields = '__all__'


class FoodTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodType
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = '__all__'






