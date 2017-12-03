# -*- coding:utf-8 -*-
from django.db import models
from tiantian_user.models import UserInfo
from tiantian_goods.models import GoodsInfo

# Create your models here.
class CartInfo(models.Model):
    '''购物车模型类'''
    # 谁买了什么多少个
    # 所对应的用户id,商品id，商品数量，商品单价
    c_user = models.ForeignKey(UserInfo)
    c_goods = models.ForeignKey(GoodsInfo)
    c_count = models.IntegerField()
