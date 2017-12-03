# -*- coding:utf-8 -*-
from haystack import indexes
from models import GoodsInfo

#指定对于某个类的某些数据建立索引
class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self): #　对哪个模型类
        return GoodsInfo

    def index_queryset(self, using=None): #　对哪个模型类的哪几条数据
        return self.get_model().objects.all()