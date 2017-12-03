# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from haystack.generic_views import SearchView
from django.http import HttpResponseRedirect
from models import *

# Create your views here.
def index(request):
    # 1.获取商品分类信息
    # 2.根据分类信息查取所对应的最热商品和最新商品各4个
    # 3.传到模板中去

    # 1
    t_list = TypeInfo.objects.all()

    # 2
    goods_list = []
    for i in t_list:
        h_list = i.goodsinfo_set.order_by('g_click')[:4]
        n_list = i.goodsinfo_set.order_by('-id')[:4]

        goods_list.append({'type': i, 'h_list': h_list, 'n_list': n_list})


    context = {'title': '首页', 'goods_list': goods_list}
    return render(request, 'tiantian_goods/index.html', context)

def list(request, type, sort, p_index):
    # type, sort, p_index，不是int
    # type--->分类id，sort--->排序规则，p_index--->第几页，list1_1_1

    # 1.根据传来的分类id，并获取分类信息及所对应的商品信息
    # 2.获取分类所对应的最新商品2个
    # 3.获取默认排序商品--->1
    # 4.获取按照价格排序商品--->2, 3
    # 5.获取按照人气排序商品--->4
    # 6.分页，分１５个每页
    # 7.页标最大显示为５个
    # 8.不足５个，全部显示
    # 9.大于５个，当显示为１，２页时，显示前５页，显示为最后两页时，显示后５页
    # 10.其它时候正常

    try:
        # 1
        type_obj = TypeInfo.objects.get(id = int(type))

        # 2
        n_list = type_obj.goodsinfo_set.order_by('-id')[:2]

        sort = int(sort)
        order = '-id'
        # 3
        if sort == 1:
            order = '-id'
        # 4
        elif sort == 2:
            order = 'g_price'
        elif sort == 3:
            order = '-g_price'
        # 5
        else:
            order = '-g_click'
        # 3，4，5
        goods_list = type_obj.goodsinfo_set.order_by(order)

        # 6
        if int(p_index) == 0:
            p_index = 1
        page_list = Paginator(goods_list, 15) # 对得到的对象列表进行分页
        current_page_list = page_list.page(int(p_index)) #　取第一页的所有对象数据

        # 7
        # 8
        page_num_list = [] # [1, 2, 3, 4, 5]
        if page_list.num_pages < 5: #　不足５页，全部显示
            page_num_list = page_list.page_range
        # 9
        elif current_page_list.number < 2:
            page_num_list = range(1, 6)
        elif current_page_list.number > page_list.num_pages - 2:
            page_num_list = range(page_list.num_pages - 5, page_list.num_pages + 1)
        # 10
        else:
            page_num_list = range(current_page_list.number -2, current_page_list.number + 3)

        context = {'title': '商品列表', 'type_obj': type_obj, 'n_list': n_list, 'goods_list': goods_list,
                   'current_page_list': current_page_list, 'p_index': int(p_index), 'sort': sort, 'page_num_list':
                       page_num_list}
        return render(request, 'tiantian_goods/list.html', context)

    except Exception as e:
        print(e)
        return render(request, '404.html')

def detail(request, goods_id):
    # 1.获取传来的商品id
    # 2.查找这个商品所对应的信息
    # 2.1这个商品点击量加一
    # 3.查找这个商品所对应的分组
    # 4.查找这个分类所对应的最新商品２个
    # 5.返回页面
    # 6.为用户添加浏览记录，添加这个商品id到cookie(look_for)
    # 6.1判断用户是否登陆
    # 7.获取cookie(look_for)
    # 8.用cookie，保持浏览记录在５个
    # 9.里面有没有这个商品的记录，有，删除原来的记录，并添加这个记录到最新位置
    # 10.没有，添加这条记录到最新位置

    try:
        # 1
        goods_id = int(goods_id)

        # 2
        obj = GoodsInfo.objects.get(id = goods_id)

        # 2.1
        obj.g_click +=1
        obj.save()

        # 3
        type_obj = obj.g_type

        # 4
        n_goods = type_obj.goodsinfo_set.order_by('-id')[:2]

        context = {'title': '商品详情', 'obj': obj, 'type_obj': type_obj, 'n_goods': n_goods}
        response = render(request, 'tiantian_goods/detail.html', context)

        # 6
        # 6.1
        if request.session.get('u_id'): #　已登陆
            # 7
            if request.COOKIES.get('look_for'): #　有这个cookie
                look_for_list = request.COOKIES.get('look_for').split(',')
                if str(goods_id) in look_for_list: #　查找有没有这个商品id
                    look_for_list.remove(str(goods_id))

                look_for_list.insert(0, str(goods_id))
                if len(look_for_list) > 5:
                    look_for_list.pop()

            # 10
            else: #　没有这个cookie
                look_for_list = []
                look_for_list.append(str(goods_id))

            response.set_cookie('look_for', ','.join(look_for_list))

            print(look_for_list)
        # 5
        return response
    except Exception as e:
        print(e)
        return render(request, '404.html')

def has_login(request):
    # 查看客户端用户是否登陆
    user = request.session.get('u_id', '')
    ok = 0
    if user:
        ok = 1
    else:
        ok = 0
    context = {'ok': ok}
    return JsonResponse(context)

class MySearchView(SearchView):
    """My custom search view."""

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        # 返回页标，一页多少个数据，多少页
        context['title'] = '搜索结果'
        page = context.get('page_obj')
        # 分页
        # 1.如果小于５页，全部显示页码
        # 2.大于５页，当前页小于２时，显示前５页，大于后２页是，显示后５页
        # 3.其它，正常显示
        if page.paginator.num_pages < 5:
            page_num_list = page.paginator.page_range
        elif page.number <= 2:
            page_num_list = range(1, 6)
        elif page.number >= page.paginator.num_pages - 2:
            page_num_list = range(page.paginator.num_pages - 4, page.paginator.num_pages + 1)
        else:
            page_num_list = range(page.number - 2, page.number + 3)

        if len(page) == 0:
            page_num_list = []

        context['page_num_list'] = page_num_list
        return context

