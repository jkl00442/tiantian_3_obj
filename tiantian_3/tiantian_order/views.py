# -*- coding:utf-8 -*-
from django.shortcuts import render
from tiantian_user.models import UserInfo, UserAddress
from tiantian_cart.models import CartInfo
from tiantian_goods.models import GoodsInfo
from models import *
from django.db import transaction
from datetime import datetime
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    # 1.获取用户id
    # 2.获取用户所有收件人
    # 3.获取传过来的所有购物车id，到数据库中查找这些id传入模板

    # 1
    u_id = request.session.get('u_id')

    # 2
    addr_list = UserAddress.objects.filter(u_user_id = u_id)

    # 3
    check_list = request.POST.getlist('check_cart') # [u'12', u'14', u'15']
    cart_list = CartInfo.objects.filter(id__in = check_list)
    check_list = ','.join(check_list)

    context = {'title': '提交订单', 'search_bar': '0', 'addr_list': addr_list, 'cart_list': cart_list, 'id_list': check_list}
    return render(request, 'tiantian_order/order.html', context)

@transaction.atomic
def order_handle(request):
    # 事务操作，成功，提交，有一步不成功，回滚--->保存点，提交保存点或回滚保存点

    # １．新建主表，id,user_id,创建日期时间，(状态？金额,在后面写)
    # 2.建立从表
    # 2.1获取传过来的购物车id
    # 2.2获取对应的购物车数据
    # 2.3查看库存是否满足购买数量，
    # 2.4满足，则建表，减库存，删购物车数据
    # 2.5不满足，回滚
    # 2.4与哪个主表相关联， goods_id, count, 单价

    ok = False
    sid = transaction.savepoint()
    try:
        # 1
        order_main = OrderMain()
        this_time = datetime.now().strftime('%Y%m%d%H%M%S')
        u_id = request.session.get('u_id')
        order_main.o_id = this_time + str(u_id)
        order_main.o_user_id = u_id
        order_main.save()

        # 2.1
        cart_id_list = request.POST.get('id_list').split(',')

        # 2.2
        cart_list = CartInfo.objects.filter(id__in = cart_id_list) # 购物车对象列表
        total_all = 0
        for i in cart_list: #　循环每一项购物车判断库存是否满足
            goods_obj = GoodsInfo.objects.get(id = i.c_goods_id)

            # 2.3
            if i.c_count <= goods_obj.g_has:

                # 2.4
                order_detail = OrderDetail()
                order_detail.o_main = order_main
                order_detail.o_goods_id = i.c_goods_id
                order_detail.o_count = i.c_count
                order_detail.o_price = i.c_goods.g_price

                total = i.c_count * i.c_goods.g_price
                total_all += total

                order_detail.o_total = total
                order_detail.save()

                goods_obj.g_has -= i.c_count
                goods_obj.save()


                cart_obj = CartInfo.objects.get(id = i.id)
                cart_obj.delete()
                ok = True

            # 2.5
            else:
                transaction.savepoint_rollback(sid)
                ok = False
                break

        if ok:
            order_main.o_status = 1
            order_main.o_total_all = total_all
            order_main.save()
            transaction.savepoint_commit(sid)
            # transaction.savepoint_rollback(sid)
        else:
            transaction.savepoint_rollback(sid)
    except Exception as e:
        print(e)
        ok = False
        transaction.savepoint_rollback(sid)
    if ok:
        return HttpResponseRedirect('/user/order/')
    else:
        return HttpResponseRedirect('/cart/')

