# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiantian_goods', '0004_auto_20171126_1414'),
        ('tiantian_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('o_count', models.IntegerField(default=0)),
                ('o_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('o_total', models.DecimalField(max_digits=6, decimal_places=2)),
                ('o_goods', models.ForeignKey(to='tiantian_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('o_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('o_create_time', models.DateTimeField(auto_now_add=True)),
                ('o_total_all', models.DecimalField(max_digits=7, decimal_places=2)),
                ('o_status', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
                ('o_user', models.ForeignKey(to='tiantian_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='o_main',
            field=models.ForeignKey(to='tiantian_order.OrderMain'),
        ),
    ]
