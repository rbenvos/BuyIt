# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20150822_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='private_user',
            field=models.ForeignKey(blank=True, to='private_user.PrivateUser', null=True),
        ),
    ]
