# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiantian_goods', '0002_auto_20171126_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscomment',
            name='c_pic',
            field=models.ImageField(default=False, upload_to=b'tiantian_goods/'),
        ),
    ]
