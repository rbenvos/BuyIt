# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product',
            field=models.ForeignKey(blank=True, to='product.Product', null=True),
        ),
    ]
