# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(related_name='user', to='private_user.PrivateUser', null=True),
        ),
        migrations.AlterField(
            model_name='privateuser',
            name='device',
            field=models.ManyToManyField(related_name='device', to='device.Device', blank=True),
        ),
        migrations.AlterField(
            model_name='privateuser',
            name='friends',
            field=models.ManyToManyField(related_name='friends', to='private_user.Friend', blank=True),
        ),
        migrations.AlterField(
            model_name='privateuser',
            name='phones',
            field=models.ForeignKey(related_name='phones', blank=True, to='private_user.Phone', null=True),
        ),
    ]
