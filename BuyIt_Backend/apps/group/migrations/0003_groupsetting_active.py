# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20150822_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupsetting',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]