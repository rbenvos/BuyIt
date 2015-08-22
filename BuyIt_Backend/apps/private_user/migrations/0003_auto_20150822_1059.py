# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_user', '0002_auto_20150822_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(default=False, to='private_user.PrivateUser', null=True),
        ),
    ]
