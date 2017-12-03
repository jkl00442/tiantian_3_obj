# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiantian_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermain',
            name='o_total_all',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
        ),
    ]
