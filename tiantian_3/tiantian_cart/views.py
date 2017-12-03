# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt # $.post() django 403
def add_cart(request):
    # 1.获取传来的商品id，要添加到购物车的商品数量
    # 2.查找是否有这个商品信息，有，在这个商品的基础上加，没有，新建一条数据加
    # 3.把对应用户的购物车信息写入购物车表中

    try:
        # 1
        dict = request.POST
        g_id = int(dict.get('g_id'))
        count = int(dict.get('count')) #　进行加法运算的要转成int类型(unicode)

        # 2
        obj_list = CartInfo.objects.filter(c_user_id = request.session.get('u_id'), c_goods_id = g_id)

        if len(obj_list) == 0: #　没有这条商品数据
            # 3
            cart = CartInfo()
            cart.c_user_id = request.session.get('u_id')
            cart.c_goods_id = g_id
            cart.c_count = count
            cart.save()
        else: #　有这条商品数据
            obj_list[0].c_count += count
            obj_list[0].save()

        ok = 1

    except Exception as e:
        print(e)
        ok = 0

    context = {'ok': ok}
    return JsonResponse(context)

def cart_show(request):
    # 获取对应用户购物车所有的商品总数
    count = 0
    try:
        u_id = request.session.get('u_id')
        obj_list = CartInfo.objects.filter(c_user_id = u_id)

        for i in obj_list:
            count += int(i.c_count)
    except Exception as e:
        print(e)

    context = {'count': count}
    return JsonResponse(context)

def index(request):
    # 1.返回用户的购物车列表信息
    cart_list = CartInfo.objects.filter(c_user_id = request.session.get('u_id'))
    context ={'title': '购物车', 'search_bar': '0', 'cart_list': cart_list}
    return render(request, 'tiantian_cart/cart.html', context)

@csrf_exempt
def edit(request):
    # 1.获取传来的购物车id，商品数量
    # 2.获取这条数据，并做修改
    # 3.返回ok=1,或ok=0

    try:
        # 1
        dict = request.POST
        c_id = dict.get('c_id')
        count = dict.get('count')
        print(c_id)

        # 2
        obj = CartInfo.objects.get(id = c_id)
        obj.c_count = int(count)
        obj.save()
        ok = 1
    except Exception as e:
        print(e)
        ok = 0

    return JsonResponse({'ok': ok})

@csrf_exempt
def delete_cart(request):
    # 1.获取要删除的购物车商品
    # 2.获取这条数据并删除
    # 3.获取购物车商品数
    # 4.返回ok=1，或ok=0
    try:
        # 1
        c_id = request.POST.get('c_id')

        # 2
        obj = CartInfo.objects.get(id = c_id)
        obj.delete()

        # 3
        ok = 1
    except Exception as e:
        print(e)
        ok = 0
    cart_len = CartInfo.objects.filter(c_user_id = request.session.get('u_id')).count()
    context = {'ok': ok, 'cart_len': cart_len}
    return JsonResponse(context)
