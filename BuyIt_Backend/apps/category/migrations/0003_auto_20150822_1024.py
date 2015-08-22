# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20150822_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=None, blank=True, to='category.Category'),
            preserve_default=False,
        ),
    ]
