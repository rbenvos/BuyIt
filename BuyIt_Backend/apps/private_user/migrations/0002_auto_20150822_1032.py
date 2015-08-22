# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='admin',
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(default=False, to='private_user.PrivateUser'),
        ),
    ]
