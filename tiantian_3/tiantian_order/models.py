# -*- coding:utf-8 -*-
from django.db import models
from tiantian_user.models import UserInfo
from tiantian_goods.models import GoodsInfo

# Create your models here.
class OrderMain(models.Model):
    # 主表，主键--->2017 11 30 10 40 30 user_id
    # 订单创建时间,用户id，订单总价，订单状态，逻辑删除
    o_id = models.CharField(primary_key=True, max_length=20)
    o_create_time = models.DateTimeField(auto_now_add=True)
    o_user = models.ForeignKey(UserInfo)
    o_total_all = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    o_status = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

class OrderDetail(models.Model):
    # 从表，这一个订单所对应的购物车商品
    # 商品id,商品数量，商品单价，这一类商品总价，对应的哪一个订单
    o_goods = models.ForeignKey(GoodsInfo)
    o_count = models.IntegerField(default=0)
    o_price = models.DecimalField(max_digits=6, decimal_places=2)
    o_total = models.DecimalField(max_digits=6, decimal_places=2)
    o_main = models.ForeignKey(OrderMain)
