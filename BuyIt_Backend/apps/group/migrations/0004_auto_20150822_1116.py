# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_groupsetting_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='settings',
        ),
        migrations.AddField(
            model_name='group',
            name='settings',
            field=models.ManyToManyField(to='group.GroupSetting', blank=True),
        ),
    ]
