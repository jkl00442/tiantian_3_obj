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
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_count', models.IntegerField()),
                ('c_goods', models.ForeignKey(to='tiantian_goods.GoodsInfo')),
                ('c_user', models.ForeignKey(to='tiantian_user.UserInfo')),
            ],
        ),
    ]
