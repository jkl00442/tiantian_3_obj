# -*- coding:utf-8 -*-

class PageFromMiddleware(object):
    '''中间件，用户登陆后返回请求页面'''
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path not in [
            '/user/register/',
            '/user/handle_name/',
            '/user/handle_register/',
            '/user/login/',
            '/user/handle_login/',
            '/user/order/',
            '/user/site/',
            '/user/handle_recv/',
            '/user/logout/',
        ]:
            request.session['page_from'] = request.get_full_path()
