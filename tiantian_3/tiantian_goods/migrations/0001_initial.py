# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tiantian_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_comment_time', models.DateTimeField(auto_now=True)),
                ('c_content', models.TextField()),
                ('c_pic', models.ImageField(upload_to=b'tiantian_goods/')),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('g_name', models.CharField(max_length=40)),
                ('g_pic', models.ImageField(upload_to=b'goods/')),
                ('g_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('g_click', models.IntegerField(default=0)),
                ('g_unit', models.CharField(max_length=10)),
                ('is_delete', models.BooleanField(default=False)),
                ('g_subtitle', models.CharField(max_length=100)),
                ('g_has', models.IntegerField(default=100)),
                ('g_detail', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(to='tiantian_goods.TypeInfo'),
        ),
        migrations.AddField(
            model_name='goodscomment',
            name='c_goods',
            field=models.ForeignKey(to='tiantian_goods.GoodsInfo'),
        ),
        migrations.AddField(
            model_name='goodscomment',
            name='c_name',
            field=models.ForeignKey(to='tiantian_user.UserInfo'),
        ),
    ]
