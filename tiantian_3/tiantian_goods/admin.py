from django.contrib import admin
from models import *

# Register your models here.
class TypeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'title', 'is_delete']

class GoodsAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['g_name', 'g_pic', 'g_price', 'g_unit', 'g_click', 'g_subtitle', 'g_has', 'g_type',
                    'is_delete']

class CommentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['c_goods', 'c_name', 'c_comment_time', 'c_content', 'c_pic', 'is_delete']

admin.site.register(TypeInfo, TypeAdmin)
admin.site.register(GoodsInfo, GoodsAdmin)
admin.site.register(GoodsComment, CommentAdmin)
