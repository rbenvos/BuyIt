# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('private_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
                ('group', models.ForeignKey(blank=True, to='group.Group', null=True)),
                ('private_user', models.ForeignKey(blank=True, to='private_user.PrivateUser', null=True)),
            ],
        ),
    ]
